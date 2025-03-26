from django.db import models
from django_mongodb_backend.fields import EmbeddedModelField
from django_mongodb_backend.models import EmbeddedModel

class registrationModel(models.Model):
    name = models.CharField(max_length=50, default='NULL')
    password = models.CharField(max_length=50, default='NULL')
    email = models.EmailField(unique=True)
    
    class Meta:
        db_table = "registration"  # This is fine
        # Remove 'managed = False' to allow migrations
    
    def __str__(self):
        return self.email

class messageModel(models.Model):
    user = models.ForeignKey(registrationModel, on_delete=models.CASCADE)
    ai_message = models.JSONField()
    user_message = models.JSONField()
    
    class Meta:
        db_table = "messages"  
        # Remove 'managed = False'
    
    def __str__(self):
        return f"{self.user.email} - {self.ai_message.get('timestamp', 'N/A')}"
