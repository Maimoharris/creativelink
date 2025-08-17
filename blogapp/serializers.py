from rest_framework import serializers
from .models import Post,Project,Contact

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['title','content','author','pub_date']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'