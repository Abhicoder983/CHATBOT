
from django.urls import path, include
from . import views



urlpatterns = [
    path("",views.home2, name="home"), 
    path('registration/',views.registration , name="registration"),
    path('login/', views.login, name='login'),
    path('confirm/', views.confirm, name='confirm'),
    path('reset/',views.reset, name='reset'),
    path('resetpassword/',views.resetPassword,name='resetpassword'),
    path('loggedIn/',views.loggedIn, name='loggedIn'),
    path('ai/info/ai_983/ai_info/' ,views.get_ai_info), 
    path('login2/', views.login2 , name='login2')
    
   

    

]
