from django.contrib import admin
from .models import Post
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

