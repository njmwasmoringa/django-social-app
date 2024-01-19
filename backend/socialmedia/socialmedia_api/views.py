from django.shortcuts import render
from socialmedia_api.models import Profile
from rest_framework import permissions, viewsets

# Create your views here.

from socialmedia_api.serializers.profile_serializer import ProfileSeliazer
from socialmedia_api.serializers.serializer import *

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSeliazer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSeliazer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSeliazer
    permission_classes = [permissions.IsAuthenticated]
    