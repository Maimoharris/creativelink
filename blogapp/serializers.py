from rest_framework import serializers
from .models import Post,Project

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['title','content','author','pub_date']
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'