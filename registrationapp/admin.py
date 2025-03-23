from django.contrib import admin
from .models import registrationModel ,messageModel
@admin.register(registrationModel)
class registrationModelAdmin(admin.ModelAdmin):
     list_display=['name','email' ,'password' ]
# Register your models here.

     
@admin.register(messageModel)
class messageModelAdmin(admin.ModelAdmin):
     list_display=['user','ai_message','user_message' ]