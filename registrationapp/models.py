from django.db import models

# Create your models here.
class registrationModel(models.Model):
    name = models.CharField( max_length=50, default='NULL' )
    password = models.CharField(max_length=50,default='NULL')
    email=models.CharField(max_length=50,primary_key=True)

    # def __str__(self):
         
    #      return f"{self.email}"

 
 
