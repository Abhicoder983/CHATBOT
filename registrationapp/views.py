from django.shortcuts import render, redirect
from registrationapp.models import registrationModel
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
import subprocess
import os
import random
import streamlit
t=0
def home2(request):
     if request.method=="POST":

     
          return render(request, "registration.html")
     else:
         return render(request, "chatbot.html") 


def registration(request):
     
    
     if request.method=="POST":
          
     
          name= request.POST.get('name')
          password= request.POST.get('password')
          roll_no= request.POST.get('roll_no')
          email1= request.POST.get('email')
          recipient_list=[email1]
          request.session['name']=name
          request.session['roll_no']=roll_no
          request.session['email1']=email1
          request.session['password']=password
              
     
          

          
          email=""
          checking=registrationModel.objects.filter(roll_no=roll_no)
          print(checking)
          for i in checking:

               if i.roll_no==roll_no:
                    email="no_data"
                    
               else:
                    email=""
          if email=="no_data":
                msg={
                    'roll': roll_no,
                    'email': email1,
                    's1':1}
                return render(request,'registration.html', msg)
          else:
               
               

           
    
               randomNum = random.randint(111111,999999)
               
               email2=EmailMessage(
                    'testing mail',
                    'the otp is {}'.format(randomNum),
                    'kumarabhishekasdf1234@gmail.com',
                    recipient_list,
               )
               
               email2.send()
               request.session['randomNum']= randomNum
               
               return redirect('/confrim/')
     
     else:
          return render(request, 'registration.html')

              


         
          
          
         

def login(request):
     s=0
     try:
          data=registrationModel.objects.all().values()
          roll_no1= request.POST.get('roll_no')
          password1= request.POST.get('password')
          
     

          for i in data:
               
               if( i['roll_no']==roll_no1 and i['password']==password1):
                    s=1
                    
          if(s==1):
               return redirect('/loggedIn/')   
          else:
               return render(request,'login.html') 
               
     except:
          return render(request, 'login.html') 


def confrim(request):
     
     
     
     if request.method=='POST':
          otp= int(request.POST.get('otp'))
          name=request.session.get('name', None)
          roll_no=request.session.get('roll_no', None)
          email1=request.session.get('email1', None)
          password=request.session.get('password', None)
          randomNum=request.session.get('randomNum', None)
          
          if(randomNum==otp):
               en=registrationModel(name=name,password=password,roll_no=roll_no,email=email1)
               en.save()
               return redirect('/loggedIn/')
          else:
          
               return render(request,'otp2.html',{'wrongOtp':1})
               
     else:
          
          return render(request,'otp2.html')
     
     
def home(request):

     return render(request , 'home.html')
def reset(request):
     if request.method=='POST':
          resetEmail=request.POST.get('resetEmail')
          request.session['resetEmail2']=resetEmail
          recipient_list=[resetEmail]
          
          
         
          resetChecking=registrationModel.objects.filter(email=resetEmail)
          for i in resetChecking:
               if i.email=='':
                    return render(request,'resetPasswordOTP.html',{'wrongEmail':'please enter the correct registered email'})
               else:
                    
                    
                    randomNum = random.randint(111111,999999)
                    request.session


                    
                    # file_path= r'C:\Users\abhishek\Desktop\registration page1\registration\image\phone.png'
                    email2=EmailMessage(
                    'to changing the password',
                    'the otp is {}'.format(randomNum),
                    'kumarabhishekasdf1234@gmail.com',
                    recipient_list,)
                    
                    email2.send()
                    
                    return render(request, 'resetPasswordOTP.html',{'condition':1})
                    resetOTP= request.POST.get('otp')
                    if resetOTP==randomNum:
                         return redirect('/home/')
                    else:
                         return render(request, 'resetPasswordOTP.html', {'worngOTP':'please Enter the correct OTP'})



                    # registerationModel.objects.filter(email=resetEmail).update(password=resetPassword)
     else:
          return render(request, 'resetPasswordOTP.html')
def resetPassword(request):
     
     if request.method=='POST':
               resetPassword=request.POST.get('password')
               reemail=request.session.get('resetemail2')
               udateField = registrationModel.objects.get(email=reemail)
               udateField.password=resetPassword
               udateField.save()
               

               return render(request, 'home.html')
     else:
          return render(request, 'resetPassword.html')
def loggedIn(request):
     
     return render(subprocess.run(['streamlit', 'run', 'templates/chatWeb.py']))

    
     
# Create your views here.
