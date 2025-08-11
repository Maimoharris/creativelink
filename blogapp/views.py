from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
# Create your views here.

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def home_view(request):

    return Response(template_name='home.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def services_view(request):

    return Response(template_name='services.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def about_view(request):
    return Response(template_name='about.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def contact_view(request):
    return Response(template_name='contact.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def projects_view(request):
    return Response(template_name='projects.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def blog_view(request):
    queryset=Post.objects.all()
    serializer=PostSerializer(queryset)
    data=serializer.data
    return Response(data,template_name='blog.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def blog_post_view(request,id):
    post=get_object_or_404(Post,pk=id)
    serializer=PostSerializer(post)
    data=serializer.data
    return Response(data,template_name='post.html')