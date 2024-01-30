
from django.urls import path, include
from registrationapp import views
import registrationapp


urlpatterns = [
    path("",views.home2, name="home2"), 
    path('registration/',views.registration , name="registration"),
    path('login/', views.login, name='login'),
     path('home/', views.home, name='home'),
    path('confirm/', views.confirm, name='confirm'),
    path('reset/',views.reset, name='reset'),
    path('resetpassword/',views.resetPassword,name='resetPassword'),
    path('loggedIn/',views.loggedIn, name='loggedIn'),
    path('redirect/' ,views.redirect, name='redirect')
   

    

]
