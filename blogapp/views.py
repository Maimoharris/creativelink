from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .models import Post,Project,Contact
from .serializers import PostSerializer,ProjectSerializer,ContactSerializer
from rest_framework import status
from django.utils.timezone import now
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
def blog_view(request):
    queryset=Post.objects.all()
    serializer=PostSerializer(queryset,many=True)
    data=serializer.data
    return Response(data,template_name='blog.html',status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def blog_post_view(request,id):
    post=get_object_or_404(Post,pk=id)
    serializer=PostSerializer(post)
    data=serializer.data
    return Response(data,template_name='post_details.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def projects_view(request):
    project=Project.objects.all()
    serializer=ProjectSerializer(project,many=True)
    data=serializer.data
    return Response(data,template_name='projects.html',status=status.HTTP_200_OK)

@api_view(['GET'])
def project_detail(request,slug):
    project=get_object_or_404(Project,slug=slug)
    serializer=ProjectSerializer(project)
    data=serializer.data
    return Response(data,template_name='project_detail.html',status=status.HTTP_200_OK )

@api_view(['POST'])
def contact_form(request):
    serializer=ContactSerializer(data=request.data)
    if request.method == 'POST':
        if serializer.is_valid():
            serializer.save()
               
        
        # Here you would typically save the contact form data to the database or send an email
        # For now, we will just return a success response
            return Response({
            'message': 'Contact form submitted successfully!',
            'submitted_at': now().strftime("%Y-%m-%d %H:%M:%S"),
            'next_steps': 'Our team will get back to you within 24 hours.'
        }, status=status.HTTP_201_CREATED)
    
    return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def contact_view(request):
    return Response(template_name='contact.html')