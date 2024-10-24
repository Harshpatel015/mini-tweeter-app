from django.db import models
from django.contrib.auth.models import User   # admin user access throught this..
from django.utils import timezone

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    Photo = models.ImageField(upload_to="Tweet_photos/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username}-{self.text}'
    