const container = document.getElementById("content");

container.scrollLeft = container.scrollWidth;

const USER_AVATAR_SVG = '<svg class="w-4 h-4 text-mint" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" /></svg>';
const AI_AVATAR_SVG = '<svg class="w-4 h-4 text-mint" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z" /><path stroke-linecap="round" stroke-linejoin="round" d="M18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456z" /></svg>';

// Builds the user's message group (url chip + avatar, bubble, timestamp) —
// same visual structure as the server-rendered messages in chatting.html
function buildUserGroup(linkValue, msgValue, timeText) {
    let user_group = document.createElement('div');
    user_group.classList.add("flex", "flex-col", "items-end", "gap-1.5");

    let user_meta_row = document.createElement('div');
    user_meta_row.classList.add("flex", "items-center", "gap-2", "max-w-[90%]", "md:max-w-[70%]");

    let link = document.createElement('span');
    link.classList.add("url-chip", "bg-black/20", "text-mint", "px-2.5", "py-1", "rounded-full", "truncate");
    link.innerText = linkValue;

    let userAvatar = document.createElement('div');
    userAvatar.classList.add("w-7", "h-7", "rounded-full", "bg-black/25", "border", "divider", "flex", "items-center", "justify-center", "shrink-0");
    userAvatar.innerHTML = USER_AVATAR_SVG;

    user_meta_row.appendChild(link);
    user_meta_row.appendChild(userAvatar);

    let user_msg_div = document.createElement('div');
    user_msg_div.classList.add("bubble-user", "px-4", "py-3", "rounded-2xl", "rounded-tr-sm", "max-w-[90%]", "md:max-w-[70%]");

    let uMsg = document.createElement('p');
    uMsg.classList.add("break-words", "leading-relaxed", "whitespace-normal");
    uMsg.innerText = msgValue;
    user_msg_div.appendChild(uMsg);

    let userTimeDiv = document.createElement('p');
    userTimeDiv.classList.add("text-xs", "text-muted", "font-mono", "pr-1");
    userTimeDiv.innerText = timeText;

    user_group.appendChild(user_meta_row);
    user_group.appendChild(user_msg_div);
    user_group.appendChild(userTimeDiv);

    return user_group;
}

// Builds the AI's message group — mirrors buildUserGroup but left-aligned
// with the bot avatar/tag on the left, matching chatting.html's bubble-ai style
function buildAiGroup(urlValue, infoValue, timeValue) {
    let ai_group = document.createElement('div');
    ai_group.classList.add("flex", "flex-col", "items-start", "gap-1.5");

    let ai_meta_row = document.createElement('div');
    ai_meta_row.classList.add("flex", "items-center", "gap-2", "max-w-[90%]", "md:max-w-[70%]");

    let aiAvatar = document.createElement('div');
    aiAvatar.classList.add("w-7", "h-7", "rounded-full", "bg-[rgba(110,231,183,0.1)]", "border", "divider", "flex", "items-center", "justify-center", "shrink-0");
    aiAvatar.innerHTML = AI_AVATAR_SVG;

    let ailink = document.createElement('span');
    ailink.classList.add("url-chip", "tag", "px-2.5", "py-1", "rounded-full", "truncate");
    ailink.innerText = urlValue;

    ai_meta_row.appendChild(aiAvatar);
    ai_meta_row.appendChild(ailink);

    let ai_msg_div = document.createElement('div');
    ai_msg_div.classList.add("bubble-ai", "px-4", "py-3", "rounded-2xl", "rounded-tl-sm", "max-w-[90%]", "md:max-w-[70%]");

    let aiMsg = document.createElement('p');
    aiMsg.classList.add("break-words", "leading-relaxed", "whitespace-normal");
    aiMsg.style.color = "rgba(255,255,255,0.9)";
    aiMsg.innerText = infoValue;
    ai_msg_div.appendChild(aiMsg);

    let aiTimeDiv = document.createElement('p');
    aiTimeDiv.classList.add("text-xs", "text-muted", "font-mono", "pl-1");
    aiTimeDiv.innerText = timeValue;

    ai_group.appendChild(ai_meta_row);
    ai_group.appendChild(ai_msg_div);
    ai_group.appendChild(aiTimeDiv);

    return ai_group;
}

document.addEventListener("keydown" , function(event){
    if(event.key==="Enter"){
        let welcome=document.getElementById("welcome");
        let searching=document.getElementById("searching");
        let completed=document.getElementById("completed");
       
        
        
        
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
        let now = new Date();
        let csrftoken = getCookie('csrftoken');

        let user_ai_box=document.createElement('div');
        user_ai_box.classList.add("space-y-5", "w-full", "mt-2", "mb-2");

        let nowTimeText = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true });
        let user_group = buildUserGroup(user_link.value, user_msg.value, nowTimeText);
        user_ai_box.appendChild(user_group);

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

            let ai_group = buildAiGroup(data.url, data.info, data.time);
            user_ai_box.appendChild(ai_group);

            container.scrollTop = container.scrollHeight;
            welcome.style.display="none";
            searching.style.display="none";
            completed.style.display="block";
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
    let now = new Date();
    let csrftoken = getCookie('csrftoken');

    let user_ai_box=document.createElement('div');
    user_ai_box.classList.add("space-y-5", "w-full", "mt-2", "mb-2");

    let nowTimeText = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true });
    let user_group = buildUserGroup(user_link.value, user_msg.value, nowTimeText);
    user_ai_box.appendChild(user_group);

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

        let ai_group = buildAiGroup(data.url, data.info, data.time);
        user_ai_box.appendChild(ai_group);

        container.scrollTop = container.scrollHeight;
        welcome.style.display="none";
        searching.style.display="none";
        completed.style.display="block";
    });
   
    
   

  
    

}