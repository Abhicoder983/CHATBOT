from rest_framework.response import Response
from rest_framework.decorators import api_view
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import re
import time


class UniversalWebScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.selenium_driver = None
    
    def __del__(self):
        if self.selenium_driver:
            self.selenium_driver.quit()
    
    def _requires_selenium(self, url):
        """Check if the URL needs JavaScript rendering (e.g., social media, SPAs)"""
        js_dependent_domains = [
            'instagram.com', 'twitter.com', 'facebook.com',
            'linkedin.com', 'tiktok.com', 'reddit.com',
            'youtube.com', 'pinterest.com'
        ]
        domain = urlparse(url).netloc.lower()
        return any(js_domain in domain for js_domain in js_dependent_domains)
    
    def _scrape_with_requests(self, url):
        """Fetch HTML using requests (for static websites)"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            raise Exception(f"Failed to fetch URL with requests: {str(e)}")
    
    def _scrape_with_selenium(self, url):
        """Fetch HTML using Selenium (for dynamic websites)"""
        try:
            if not self.selenium_driver:
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--window-size=1920x1080")
                self.selenium_driver = webdriver.Chrome(options=chrome_options)
            
            self.selenium_driver.get(url)
            
            # Wait for JavaScript to load
            WebDriverWait(self.selenium_driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Additional delay for social media sites
            if any(domain in url for domain in ['instagram.com', 'twitter.com']):
                time.sleep(3)
            
            return self.selenium_driver.page_source
        except Exception as e:
            raise Exception(f"Failed to fetch URL with Selenium: {str(e)}")
    
    def _clean_text(self, text):
        """Remove extra whitespace and clean text"""
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def _extract_metadata(self, soup):
        """Extract title, description, and other metadata"""
        title = soup.title.string if soup.title else "No title found"
        
        meta_description = ""
        meta_tag = soup.find('meta', attrs={'name': 'description'})
        if meta_tag:
            meta_description = meta_tag.get('content', '')
        
        return title, meta_description
    
    def scrape_website(self, url):
        """Main method to scrape any public website"""
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            # Check if JavaScript rendering is needed
            if self._requires_selenium(url):
                html = self._scrape_with_selenium(url)
            else:
                html = self._scrape_with_requests(url)
            
            # Parse HTML with BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            
            # Remove unwanted elements
            for element in soup(['script', 'style', 'meta', 'link', 'nav', 'footer', 'header', 'iframe']):
                element.decompose()
            
            # Get clean text
            text = soup.get_text(separator=' ', strip=True)
            text = self._clean_text(text)
            
            # Extract metadata
            title, meta_description = self._extract_metadata(soup)
            
            # Return structured data
            return {
                'url': url,
                'domain': urlparse(url).netloc,
                'title': title,
                'meta_description': meta_description,
                'content': text[:8000],  # Limit content length
                'status': 'success'
            }
        except Exception as e:
            return {
                'url': url,
                'status': 'error',
                'error_message': str(e)
            }

def format_result(data):
    """Format scraped data into readable output"""
    if data['status'] != 'success':
        return f"❌ Error scraping {data['url']}: {data['error_message']}"
    
    output = f"🌐 Website: {data['url']}\n"
    output += f"🔍 Title: {data['title']}\n"
    
    if data['meta_description']:
        output += f"📝 Description: {data['meta_description']}\n"
    
    output += f"\n📄first 8000 character Content:\n{data['content']}\n"
    
    if len(data['content']) >= 5000:
        output += "... [Content truncated]"
    
    return output

# Example Usagee
def scraping_web(url,question):
    scraper = UniversalWebScraper()
    user_input =url.strip()
        
        
        
        
    result = scraper.scrape_website(user_input)
    content= format_result(result)
     
    
    return Response({"answer": get_answer_from_website(content,question)})


# Configure Gemini
genai.configure(api_key=config("API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")




def get_answer_from_website(content , question):
    
    
    if not content or not question:
        return Response({"error": "Both content or question are required"}, status=400)
   
    
    # Ask Gemini
    prompt = f"""
I am providing the content of a publicly accessible website. Please follow the instructions below step-by-step to generate an accurate and concise answer:

---

### Step 1: Content Intake  
Read and analyze the content provided below carefully: 

Content:{content}



---

### Step 2: Structure the Content  
Organize the content into a clear and well-structured format. Break it down into meaningful sections such as headings, descriptions, services, features, FAQs, contact information, etc., if applicable.

---

### Step 3: Match Content with the Question  
Question: "{question}"

Based on the structured content, check whether it contains any information relevant to the above question.

- If relevant information is found:  
  Write a **concise and informative paragraph (maximum 400 words)** that clearly answers the question based only on the information from the website content provided.

- If no relevant information is found:  
  Respond with:  
  "Sorry, I am not able to find any information related to the question asked in the website."

- If any error occurs while processing the content:  
  Respond with:  
  "Sorry, I am not able to fetch the information related to it."

- If the website requires login access, denies scraping, or displays a privacy restriction message such as 'Sorry, I am unable to access this website':  
  Respond with:  
  "Sorry, I have no access to that website. Please try with another website that is publicly available and accessible to all."

---

### Important Notes for the Model:
- Do not hallucinate or add any information that is not present in the content.  
- Focus only on the content provided.  
- Maintain a professional tone in the final response.
"""



    print('prompt ready')
    response = model.generate_content(prompt)
    return response.text
   
