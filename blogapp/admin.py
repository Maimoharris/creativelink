from django.contrib import admin
from .models import Post,Project
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','pub_date']
    list_per_page=10
    date_hierarchy='pub_date'
    ordering=['title','author','pub_date']
    search_fields=['title','author','pub_date']
    list_filter=['author','pub_date']

admin.site.site_header="Creative Link Admin Portal"
admin.site.index_title=f"Welcome Back {User.username}"

@admin.register(Project)
class projectAdmin(admin.ModelAdmin):
    list_display=['title','category','pub_date','client']
    list_per_page=10
    date_hierarchy='pub_date'
    ordering=['title','category','pub_date','client']
    search_fields=['title','category','pub_date','client']
    list_filter=['category','pub_date','client']