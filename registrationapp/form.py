from django import forms
from .models import registrationModel



class loginForm(forms.ModelForm):
    
    class Meta:
        model=registrationModel
        fields=['email','password']
        labels={
            'email':'Enter Email',
            'password':'Enter Password'
        }
        help_texts={
            'email':'Enter your Email',
            'password':'Enter your Password'
        }
       



