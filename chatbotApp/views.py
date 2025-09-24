from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import JsonResponse
from chatbotApp.models import registrationModel , messageModel
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import random
from .utils import scraping_web
from datetime import datetime, timezone

import pytz
t=0
def home2(request):

     request.session.flush()
     return render(request, 'chatbot.html')


def registration(request):
     if request.method=="POST":
          name= request.POST.get('name')
          password= request.POST.get('password')
          email1= request.POST.get('email')
          recipient_list=[email1]
          request.session['name']=name
          request.session['email1']=email1
          request.session['password']=password

     
          checking=registrationModel.objects.filter(email=email1)
          
          if checking:
                msg={
                    'email': email1,
                    's1':1}
                return render(request,'registration.html', msg)
          else:
               
               
               # Generate a random number for the email content
               randomNum = random.randint(111111, 999999)

     # Create the email message
               
               try:
                    email2=EmailMessage(
                              'ChatBot registeration OTP',
                              'To verify your email, your otp is {}'.format(randomNum),
                              'kumarabhishekasdf1234@gmail.com',
                              recipient_list
                         )
                         
                    email2.send()

     # Print a success message and store data in the session
                    
                    request.session['randomNum'] = randomNum
                    request.session['access'] = True
               except:
                    return render(request, 'registration.html', {'msg':'Something went wrong please try again later'})
     # Redirect to the confirmation page
               return HttpResponseRedirect('/confirm/')
          
             
     else:
          return render(request, 'registration.html')

              


         
          
          
         

def login(request):
     if request.method=='POST':
          email1= request.POST.get('email',None)
          password1= request.POST.get('password',None)
          if(email1==None and password1==None):
               return render(request, 'login.html',{'msg':'Please enter the email and password','condition':1})
          elif(email1==None):
               return render(request, 'login.html',{'msg':'Please enter the email','condition':1})
          elif(password1==None):
               return render(request, 'login.html',{'msg':'Please enter the password','condition':1})
          data=registrationModel.objects.filter(email=email1)
          
          if data.exists()==False:
               return render(request, 'login.html', {'msg':'Please enter the correct email','condition':1})
               
              
          else:
               if (data[0].password==password1):
                    request.session['auth_email']=email1
                    return HttpResponseRedirect('/loggedIn/')
               else:
                    return render(request,'login.html',{'msg':'Please enter the correct password', 'condition':1})            
     else:
          return render(request, 'login.html')
          

def confirm(request):
     
     if(request.session.get('access',None)==None):
          return HttpResponseRedirect('/registration/')
     

     if request.method=='POST':
          otp= int(request.POST.get('otp'))
          name=request.session.get('name', None)
         
          email1=request.session.get('email1', None)
          password=request.session.get('password', None)
          randomNum=request.session.get('randomNum', None)
          
          if(randomNum==otp):
               try:
                    en=registrationModel(name=name,password=password,email=email1)
                    en.save()
                    request.session['randomNum']=None
                    request.session['auth_email']=email1
                    messageModel.objects.create(user=en,ai_message={},user_message={})     
                     
                    return HttpResponseRedirect('/loggedIn/')
               except:
                    return render(request, 'otp2.html', {'msg':'Something went wrong please try again later'})
          else:
          
               return render(request,'otp2.html',{'msg':'!Wrong OTP'})
               
     else:
     
          return render(request,'otp2.html')
     
     

def reset(request):
    
     if request.method == 'POST':
          resetEmail = request.POST.get('resetEmail')
          recipient_list = [resetEmail]
          resetChecking = registrationModel.objects.filter(email=resetEmail)
          if resetEmail==None:
               randomNumber= request.session.get('randomnumbers')
               resetOTP = int(request.POST.get('otp'))
               if resetOTP == randomNumber:
                    request.session['confirmPassword']=True
                    return HttpResponseRedirect('/resetpassword')
               else:
                    return render(request, 'resetPasswordOTP.html', {'wrongOTP': 'Please enter the correct OTP'})   
          elif not resetChecking:
               return render(request, 'resetPasswordOTP.html', {'wrongEmail': 'Please enter the correct registered email','condition': 0})
          else:
               try:
               
                    randomNumber = random.randint(111111, 999999)
                    
                    

                    email2 = EmailMessage(
                    'To change the password',
                    'The OTP is {}'.format(randomNumber),
                    'kumarabhishekasdf1234@gmail.com',
                    recipient_list,
                    )

                    email2.send()
                    request.session['randomnumbers'] = randomNumber
                    request.session['resetEmail2'] = resetEmail     
                    return render(request, 'resetPasswordOTP.html', {'condition': 1})     
               except:
                    return render(request , 'resetPasswordOTP.html', {'errors':'something went wrong', 'condition': 0})
       
          
          
     else:
          return render(request, 'resetPasswordOTP.html', {'condition': 0})

                    # registerationModel.objects.filter(email=resetEmail).update(password=resetPassword)
     
def resetPassword(request):
     if request.session.get('confirmPassword', None)==None:
          return HttpResponseRedirect('/reset/')
     try:
          if request.method=='POST':
               resetPassword=request.POST.get('resetPassword')
               reemail=request.session.get('resetEmail2')
               udateField = registrationModel.objects.get(email=reemail)
               udateField.password=resetPassword
               udateField.save()
               request.session.flush()
               return HttpResponseRedirect('/')
          else:
               return render(request, "resetPassword.html")
     except:
          return render(request, 'resetPassword.html')
def loggedIn(request):
    email = request.session.get('auth_email')
    
    if not email:
        return redirect('login')  
    

    request.session['auth_email2'] = email
    try:
          user_obj = registrationModel.objects.get(email=email)
          user_id = user_obj.id  # MongoDB me ObjectId store hota hai
    except registrationModel.DoesNotExist:
         
          user_id = None
    request.session['user_email_id'] = str(user_id)
    # Fetch user messages
    data = messageModel.objects.filter(user=user_id).values('ai_message', 'user_message')
    
    # Fetch user name correctly
    user = user_obj
    name = user.name if user else 'Guest'
    if not data[0]['ai_message'] :
         send_data = {
        'ai_message': None,
            'user_message': None,
            'name':name,
            'api_url':settings.API_URL}
         return render(request, 'chatting.html', send_data)
      # Handle missing user case

    send_data = {
        'ai_message': data[0]['ai_message']['content'] if data else None,  # Handle empty QuerySet
        'user_message': data[0]['user_message']['content'] if data else None,
        'name': name   
    }
  

    return render(request, 'chatting.html', send_data)


@csrf_exempt  
def get_ai_info(request):
    auth_login=request.session.get('user_email_id',None)
  
#     https://chatbot-alpha-mauve-80.vercel.app/loggedIn/
    allowed_referrer = "https://website-chatbot-7el7.onrender.com/loggedIn/"  
    request_referrer = request.META.get("HTTP_REFERER", "")

    if not request_referrer.startswith(allowed_referrer):
        return JsonResponse({"error": "Forbidden"}, status=403)
    if(auth_login==None):
          return redirect('login')
    if(request.method=='POST'):
        data= json.loads(request.body)
    
        user_timezone=data.get('time_zone',"UTC")
        utc_now = datetime.now(timezone.utc)
        user_url=data['user_link']
        user_message=data['user_msg']
        user_message_time=data['user_time']
        user_content={'msg':user_message,
                      'time':user_message_time,
                      'url':user_url}
        ai_info = scraping_web(user_url,user_message).data.get('answer')
    
        try:
             user_tz=pytz.timezone(user_timezone)
             local_time=utc_now.astimezone(user_tz)
            
        except pytz.exceptions.UnknownTimeZoneError:
             local_time=utc_now  
             
             
        
        user= messageModel.objects.get(user=auth_login)
        time=local_time.strftime("%I:%M:%S %p")
       
        ai_content={'msg':ai_info,
                    'time':time,
                    'url':user_url}


        if(user.ai_message=={}):
             user.ai_message={'content':[ai_content]}
             if(user.user_message=={}):
                  user.user_message={'content':[user_content]}
                  user.save()
                  return JsonResponse({'info':ai_info,'time':time,'url':user_url}, status=200)
     
        user.ai_message['content'].append(ai_content)
        user.user_message['content'].append(user_content)
        user.save()
        return JsonResponse({'info':ai_info,'time':time, 'url':user_url}, status=200)



    return JsonResponse({"error": "something went wrong"}, status=400)
   



     



          

     
     

     