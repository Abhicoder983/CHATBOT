const container = document.getElementById("content");

container.scrollLeft = container.scrollWidth;
document.addEventListener("keydown" , function(event){
    if(event.key==="Enter"){
        let welcome=document.getElementById("welcome");
        let searching=document.getElementById("searching");
        let completed=document.getElementById("completed");
        let loading=document.getElementById("loading");
        
        
        
        let closelink=document.getElementById("link");
        let openlink=document.getElementById("openlink");
        
        
        if(closelink.classList.contains("flex")){
            closelink.classList.remove("opacity-100", "max-h-40");
            closelink.classList.add("opacity-0", "max-h-0");
            setTimeout(() => {
                closelink.style.display = "none";
                openlink.style.opacity=100; // Show the link
                openlink.style.display = "block";
            }, 300);
        }
        let user_msg= document.getElementById('user_msg')
        let user_link=document.getElementById('user_link')
        
        if(user_msg.value=="" || user_link.value==""){
            if(user_msg.value=="" && user_link.value==""){
                alert("!Please provide the link and question")
                return false;
            }
            else if(user_link.value==""){
                alert("Enter the Link")
                return false
            }
    
            else{
                alert("Ask the question ")
                return false
            }
           
        }
    
        const urlRegx=/^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w.-]*)*\/?$/;
        if(!urlRegx.test(user_link.value)){
            alert("!Please Enter the valid link")
            return false;
        }
        welcome.style.display="none";
        searching.style.display="block";
        completed.style.display="none";
        loading.classList.remove("invisible");
        loading.classList.add("visible");
        let now = new Date();
        let csrftoken = getCookie('csrftoken');
        let  user_msg_div=document.createElement('div');
        let user_ai_box=document.createElement('div');
        let userTimeDiv=document.createElement('p')
        let uMsg=document.createElement('p')
        uMsg.className="p-2 break-words"
    
        let link=document.createElement('p')
        link.className="text-right text-blue-600 font-bold bg-white p-1 rounded-md break-words"
       
    
    
        user_ai_box.classList.add("flex", "flex-col", "w-full", "mt-2" ,"mb-2" ,"gap-2")
        user_msg_div.classList.add("Content", "text-base" ,"bg-gray-700", "text-white", "p-3", "w-fit", "max-w-[90%]", "md:max-w-[80%]" ,"ml-auto", "rounded-xl", "shadow-md" ,"break-words", "whitespace-normal")
        
        userTimeDiv.classList.add("text-right", "text-slate-400" ,"text-sm")
                                
       
        user_ai_box.appendChild(user_msg_div)
        user_msg_div.appendChild(link)
        link.innerText=user_link.value
        user_msg_div.appendChild(uMsg)
        uMsg.innerText=user_msg.value;
        user_msg_div.appendChild(userTimeDiv)
        userTimeDiv.innerText = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true });
        const container=document.getElementById("content")
        container.appendChild(user_ai_box)

        console.log("abhishek",container.scrollHeight)
        console.log("abhishek3",container.scrollTop)
        container.scrollTop = container.scrollHeight;
        console.log(container.scrollHeight)
        console.log(container.scrollTop)
        const userTimeZone=Intl.DateTimeFormat().resolvedOptions().timeZone
        

        // https://chatbot-alpha-mauve-80.vercel.app/ai/info/ai_983/ai_info/
        fetch('https://website-chatbot-7el7.onrender.com/ai/info/ai_983/ai_info/' ,{
            method:'POST',
            headers:{'Content-Type':'application/json',
                "X-CSRFToken": csrftoken
            },
            body:JSON.stringify({'user_msg':user_msg.value, 'user_link':user_link.value,'user_time':now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true }) , 'time_zone':userTimeZone})
        }).then(response=> response.json())
        .then(data=>{
            
            let ai_msg_div=document.createElement('div');
            let aiTimeDiv=document.createElement('p')
            let ailink=document.createElement('p')
            let aiMsg=document.createElement('p')
            aiMsg.className="p-2 break-words"
            ailink.className=" text-blue-600 font-bold bg-white p-1 rounded-md break-words"
            ai_msg_div.classList.add("Content", "text-base", "bg-gray-800", "text-white", "p-3", "w-fit", "max-w-[90%]", "md:max-w-[80%]", "rounded-xl", "shadow-md","break-words" ,"whitespace-normal")
            aiTimeDiv.className="text-right text-slate-400 text-sm"
            user_ai_box.appendChild(ai_msg_div)
           
            ailink.innerText=data.url
            ai_msg_div.appendChild(ailink)
    
           
            ai_msg_div.appendChild(aiMsg)
            aiMsg.innerText=data.info
    
            ai_msg_div.appendChild(aiTimeDiv)
            aiTimeDiv.innerText=data.time
            container.scrollTop = container.scrollHeight;
            welcome.style.display="none";
            searching.style.display="none";
            completed.style.display="block";
            loading.classList.remove("visible");
            loading.classList.add("invisible");
        });
        
       
    
      
    }
}

)


document.addEventListener("keydown",function(event){
    if(event.altKey && event.key === "l"){
        let linkDiv = document.getElementById("link");
        let openlink=document.getElementById("openlink");
        console.log('abhishek2')
        console.log(openlink.style.display)
        if(openlink.style.display=="none"){
            console.log('closelink')
        if (linkDiv.classList.contains("opacity-100")) {
            linkDiv.classList.remove("opacity-100", "max-h-40");
            linkDiv.classList.add("opacity-0", "max-h-0");
            setTimeout(() => {
                linkDiv.style.display = "none";
                openlink.style.opacity=100;
                 openlink.style.display="flex"; // Show the link
               // Show the link
            }, 300); // Match the transition duration
        } 
    }
        
        else {
            console.log('openlink')
            linkDiv.style.display = "flex";
            setTimeout(() => {
                linkDiv.classList.remove("opacity-0", "max-h-0");
                linkDiv.classList.add("opacity-100", "max-h-40");
                openlink.style.display="none"; // Hide the link
                openlink.style.opacity=0; // Hide the link
              
            }, 2);
        }
    }
    
})

function openLink(e){
    let linkDiv = document.getElementById("link");
    let openlink=document.getElementById("openlink");
    console.log(e);
    if(e.target.id=="closelink"){
    if (linkDiv.classList.contains("opacity-100")) {
        linkDiv.classList.remove("opacity-100", "max-h-40");
        linkDiv.classList.add("opacity-0", "max-h-0");
        setTimeout(() => {
            linkDiv.style.display = "none";
            openlink.style.opacity=100;
             openlink.style.display="flex"; // Show the link
           // Show the link
        }, 300); // Match the transition duration
    } 
}
    
    else {
        linkDiv.style.display = "flex";
        setTimeout(() => {
            
            linkDiv.classList.remove("opacity-0", "max-h-0");
            linkDiv.classList.add("opacity-100", "max-h-40");
            openlink.style.display="none"; // Hide the link
            openlink.style.opacity=0; // Hide the link
          
        }, 2);
    }
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



// getting ai information from the server

function getAiInfo(e){
    console.log("getAiInfo called", e);
    let welcome=document.getElementById("welcome");
    let searching=document.getElementById("searching");
    let completed=document.getElementById("completed");
    let loading=document.getElementById("loading");
    
    
    
    let closelink=document.getElementById("link");
    let openlink=document.getElementById("openlink");
    console.log(e);
    if(closelink.classList.contains("flex")){
        closelink.classList.remove("opacity-100", "max-h-40");
        closelink.classList.add("opacity-0", "max-h-0");
        setTimeout(() => {
            closelink.style.display = "none";
            openlink.style.opacity=100; 
            openlink.style.display="block"; // Show the link
        }, 300);
    }
    let user_msg= document.getElementById('user_msg')
    let user_link=document.getElementById('user_link')
    console.log(typeof(user_msg.value))
    if(user_msg.value=="" || user_link.value==""){
        if(user_msg.value=="" && user_link.value==""){
            alert("!Please provide the link and question")
            return false;
        }
        else if(user_link.value==""){
            alert("Enter the Link")
            return false
        }

        else{
            alert("Ask the question ")
            return false
        }
       
    }

    const urlRegx=/^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w.-]*)*\/?$/;
    if(!urlRegx.test(user_link.value)){
        alert("!Please Enter the valid link")
        return false;
    }
    welcome.style.display="none";
    searching.style.display="block";
    completed.style.display="none";
    console.log("loadingrem",loading.classList)
    loading.classList.remove("invisible");
    loading.classList.add("visible")
    console.log("laodingadd",loading.classList)
    let now = new Date();
    let csrftoken = getCookie('csrftoken');
    let  user_msg_div=document.createElement('div');
    let user_ai_box=document.createElement('div');
    let userTimeDiv=document.createElement('p')
    let uMsg=document.createElement('p')
    uMsg.className="p-2 break-words"

    let link=document.createElement('p')
    link.className="text-right text-blue-600 font-bold bg-white p-1 rounded-md break-words"
   


    user_ai_box.classList.add("flex", "flex-col", "w-full", "mt-2" ,"mb-2" ,"gap-2")
    user_msg_div.classList.add("Content", "text-base" ,"bg-gray-700", "text-white", "p-3", "w-fit", "max-w-[90%]", "md:max-w-[80%]" ,"ml-auto", "rounded-xl", "shadow-md" ,"break-words", "whitespace-normal")
    
    userTimeDiv.classList.add("text-right", "text-slate-400" ,"text-sm")
                            
   
    user_ai_box.appendChild(user_msg_div)
    user_msg_div.appendChild(link)
    link.innerText=user_link.value
    user_msg_div.appendChild(uMsg)
    uMsg.innerText=user_msg.value;
    user_msg_div.appendChild(userTimeDiv)
    userTimeDiv.innerText = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true });
    const container=document.getElementById("content")
    container.appendChild(user_ai_box)
    
   
    const userTimeZone=Intl.DateTimeFormat().resolvedOptions().timeZone
    container.scrollTop = container.scrollHeight;
    // https://chatbot-alpha-mauve-80.vercel.app/ai/info/ai_983/ai_info/
    fetch('https://website-chatbot-7el7.onrender.com/ai/info/ai_983/ai_info/' ,{
        method:'POST',
        headers:{'Content-Type':'application/json',
            "X-CSRFToken": csrftoken
        },
        body:JSON.stringify({'user_msg':user_msg.value, 'user_link':user_link.value,'user_time':now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true }) , 'time_zone':userTimeZone})
    }).then(response=> response.json())
    .then(data=>{
    
        let ai_msg_div=document.createElement('div');
        let aiTimeDiv=document.createElement('p')
        let ailink=document.createElement('p')
        let aiMsg=document.createElement('p')
        aiMsg.className="p-2 break-words"
        ailink.className=" text-blue-600 font-bold bg-white p-1 rounded-md break-words"
        ai_msg_div.classList.add("Content", "text-base", "bg-gray-800", "text-white", "p-3", "w-fit", "max-w-[90%]", "md:max-w-[80%]", "rounded-xl", "shadow-md","break-words" ,"whitespace-normal")
        aiTimeDiv.className="text-right text-slate-400 text-sm"
        user_ai_box.appendChild(ai_msg_div)
        
        ailink.innerText=data.url
        ai_msg_div.appendChild(ailink)

       
        ai_msg_div.appendChild(aiMsg)
        aiMsg.innerText=data.info

        ai_msg_div.appendChild(aiTimeDiv)
        aiTimeDiv.innerText=data.time
        container.scrollTop = container.scrollHeight;
        welcome.style.display="none";
        searching.style.display="none";
        completed.style.display="block";
        loading.classList.remove("visible");
        loading.classList.add("invisible");
    });
   
    
   

  
    

}