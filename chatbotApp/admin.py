from django.contrib import admin
from .models import registrationModel, messageModel
# Register your models here.
@admin.register(registrationModel)
class registrationModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')

@admin.register(messageModel)
class messageModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'ai_message', 'user_message')
    search_fields = ('user', 'ai_message')
    list_filter = ('user', 'ai_message')
