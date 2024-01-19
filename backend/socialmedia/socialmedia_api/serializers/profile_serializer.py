from socialmedia_api.models import Profile
from rest_framework import serializers

class ProfileSeliazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'fullname', 'avatar', 'phone_number','email', 'user_id']