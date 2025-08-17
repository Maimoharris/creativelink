from django.urls import path
from .views import *
urlpatterns = [
    path('',home_view,name='home'),
    path('services/',services_view,name='services'),
    path('about/',about_view,name='about'),
    path('contact/',contact_view,name='contact'),
    path('projects',projects_view, name='projects'),
    path('project/<slug:slug>/',project_detail,name='project_detail'),
    path('blog/',blog_view,name='blog'),
    path('blog/post/<int:id>/',blog_post_view,name='blog_post')
]