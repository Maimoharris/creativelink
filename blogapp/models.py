from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255,null=False)
    content=models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.title