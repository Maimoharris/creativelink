from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Technology', 'Technology'),
        ('Lifestyle', 'Lifestyle'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Finance', 'Finance'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),)
    title=models.CharField(max_length=255,null=False)
    content=models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    category=models.CharField(choices=CATEGORY_CHOICES,default='Technology',max_length=50)
    image=models.ImageField(upload_to='posts/',blank=True,null=True)
    slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Project(models.Model):
    CATEGORY_CHOICES = (
        ('Technology', 'Technology'),
        ('Lifestyle', 'Lifestyle'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Finance', 'Finance'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),)
    title=models.CharField(max_length=255,null=False)
    description=models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)
    category=models.CharField(choices=CATEGORY_CHOICES,default='Technology',max_length=50)
    client=models.CharField(max_length=255,null=True,blank=True)
    slug=models.SlugField(max_length=255,unique=True,null=True,blank=True)
    image=models.ImageField(upload_to='projects/',blank=True,null=True)
    link=models.URLField(max_length=255,blank=True,null=True)

    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)