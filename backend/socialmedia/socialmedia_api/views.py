from django.shortcuts import render
from socialmedia_api.models import Profile
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
import ipdb

# Create your views here.

from socialmedia_api.serializers.profile_serializer import ProfileSeliazer
from socialmedia_api.serializers.serializer import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from http import HTTPMethod


# @api_view(['POST'])
class AuthViewSet(viewsets.ModelViewSet):
    serializer_class = UserViewSet

    @action(detail=False, methods=[HTTPMethod.POST], 
            permission_classes=[permissions.AllowAny],
            url_path=r'signin',
        )
    def signin(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if the username and password are valid
        user = authenticate(username=username, password=password)
        # ipdb.set_trace()
        if user is not None:
            # Generate or retrieve the token for the authenticated user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = User.objects.all()
    serializer_class = UserViewSet
    permission_classes = [permissions.IsAuthenticated]
    

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
    