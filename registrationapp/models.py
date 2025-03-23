from django.db import models

# Create your models here.
class registrationModel(models.Model):
    name = models.CharField( max_length=50, default='NULL' )
    password = models.CharField(max_length=50,default='NULL')
    email=models.CharField(max_length=50,primary_key=True)
   




class messageModel(models.Model):
    user=models.ForeignKey(registrationModel,on_delete=models.CASCADE)
    ai_message=models.JSONField()
    user_message=models.JSONField()

    def __str__(self):
        return f"{self.user} at {self.ai_message.get('timestamp')} said {self.user_message} at {self.user_message.get('timestamp')}"
 
 
    