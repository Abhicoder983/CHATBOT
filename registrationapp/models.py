from django.db import models

# Create your models here.
class registrationModel(models.Model):
    name = models.CharField( max_length=50, default='NULL' )
    roll_no = models.CharField( max_length=50, default='NULL',primary_key=True)
    password = models.CharField(max_length=50, default= 'NULL')
    email=models.CharField(max_length=50, default='NULL',unique=True)

 
 
