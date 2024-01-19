from socialmedia_api.models import *

from rest_framework import serializers

class CommentSeliazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'message']

class PostsSeliazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'media', 'message']

class ReactionSeliazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reaction
        fields = ['id', 'reaction', 'name']


