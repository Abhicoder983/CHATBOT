from django.shortcuts import render,HttpResponseRedirect
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
      
          email1= request.POST.get('email')
          recipient_list=[email1]
          request.session['name']=name
         
          request.session['email1']=email1
          request.session['password']=password
              
     
          

          
          
          checking=registrationModel.objects.filter(email=email1)
          print(type(checking))
         
          if checking:
                msg={
                    'email': email1,
                    's1':1}
                return render(request,'registration.html', msg)
          else:
               
               

               try:
    
                    randomNum = random.randint(111111,999999)
                    
                    email2=EmailMessage(
                         'testing mail',
                         'the otp is {}'.format(randomNum),
                         'kumarabhishekasdf1234@gmail.com',
                         recipient_list
                    )
                    
                    email2.send()
                    
                    request.session['randomNum'] = randomNum
                    return HttpResponseRedirect('/confirm/')
               except:
                    return render(request , 'registration.html',{'msg':'something went wrong please try again'})
     
     else:
          return render(request, 'registration.html')

              


         
          
          
         

def login(request):
     s=0
     try:
          
          email1= request.POST.get('email')
          password1= request.POST.get('password')
          if email1==None:
               email1=''
          data=registrationModel.objects.filter(email=email1)
          
          
     
           
          # for i in data:
               
          #      if i.password == password1:
          #           return HttpResponseRedirect('/loggedIn/')
          #      else:
          #           return render(request,'login.html',{'msg':'please enter the valid email and password', 'condition':1}) 
          if (data[0].email==''):
               
               if email1 =='':
                    return render(request, 'login.html')
               
              
          else:
               if (data[0].password==password1):
                    return HttpResponseRedirect('/loggedIn/')
               else:
                    return render(request,'login.html',{'msg':'please enter the correct password', 'condition':1}) 

               
          # print(data)
          
     

          # for i in data:
               
               
          #      if( i['email']==roll_no1 and i['password']==password1):
                    
          #           s=1
          #           break
          #      else:
          #           s=2
          # if(s==1):

               
          #      return HttpResponseRedirect('/loggedIn/')   
          # elif(s==2):
          #      return render(request,'login.html',{'msg':'please enter the enter the valid email and password', 'condition':1}) 
               
     except Exception as e:
          print(e)
          print('error')
          if email1=='':
               return render(request,'login.html',{'msg':'please enter the valid email', 'condition':1})
          else:
               return render(request, 'login.html', {'msg':'please enter the email and password','condition':1})

def confirm(request):
     
     

     if request.method=='POST':
          otp= int(request.POST.get('otp'))
          name=request.session.get('name', None)
         
          email1=request.session.get('email1', None)
          password=request.session.get('password', None)
          randomNum=request.session.get('randomNum', None)
          
          if(randomNum==otp):
               en=registrationModel(name=name,password=password,email=email1)
               en.save()
               return HttpResponseRedirect('/loggedIn/')
          else:
          
               return render(request,'otp2.html',{'wrongOtp':1})
               
     else:
     
          return render(request,'otp2.html')
     
     
def home(request):

     return render(request , 'home.html')
def reset(request):
    
     if request.method == 'POST':
          resetEmail = request.POST.get('resetEmail')
          


          recipient_list = [resetEmail]

          resetChecking = registrationModel.objects.filter(email=resetEmail)
          
         
         
          if resetEmail==None:
               randomNumber= request.session.get('randomnumbers')
              
               resetOTP = int(request.POST.get('otp'))
               
               if resetOTP == randomNumber:
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
     try :
     
          if request.method=='POST':
               resetPassword=request.POST.get('resetPassword')
               reemail=request.session.get('resetEmail2')
               udateField = registrationModel.objects.get(email=reemail)
               udateField.password=resetPassword
               udateField.save()
               return HttpResponseRedirect('/')
          else:
               return render(request, "resetPassword.html")
     except:
          return render(request, 'resetPassword.html')
def loggedIn(request):
     return subprocess.run(['streamlit', 'run','templates\chatWeb.py'])
     

     