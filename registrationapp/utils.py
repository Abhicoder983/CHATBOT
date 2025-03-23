from rest_framework.response import Response
from rest_framework.decorators import api_view
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
from decouple import config

# Configure Gemini
genai.configure(api_key=config("API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def scrape_website(url):
    """Fetches and extracts text from a website"""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        
        content = "\n".join([p.get_text() for p in paragraphs])
        print("scrape")
        return content[:5000]  # Limit text to avoid exceeding API token limits
    except Exception as e:
        return f"Error fetching website: {str(e)}"


def get_answer_from_website(url , question):
    
    
    if not url or not question:
        return Response({"error": "Both URL and question are required"}, status=400)
    
    # Scrape the website content
    website_content = scrape_website(url)
    
    if website_content.startswith("Error"):
        print('error')
        return Response({"error": website_content}, status=400)
    
    # Ask Gemini
    prompt = f"under this company or organization in this website link or under this link please answer this question: {question}\n\nlink:\n{url} \n\n Answer should be in 100 words."
    print('prompt ready')
    response = model.generate_content(prompt)
    print(response.text)
    return Response({"answer": response.text})
