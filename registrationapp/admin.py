from django.contrib import admin
from .models import registrationModel
@admin.register(registrationModel)
class registrationModelAdmin(admin.ModelAdmin):
     list_display=['name','roll_no','password','email']
# Register your models here.
