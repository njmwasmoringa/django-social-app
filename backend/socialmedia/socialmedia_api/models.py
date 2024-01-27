from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        blank = False,
        null = True
    )
    fullname = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='images', null=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=200)


class Post(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        blank=False,
        null = True
    )
    message = models.CharField(max_length=100)
    media = models.ImageField(upload_to='images', null=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.PROTECT, blank=False)
    profile = models.ForeignKey(Profile, null=True, on_delete=models.PROTECT, blank=False)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, blank=False)
    message = models.CharField(max_length=100)


class Reaction(models.Model):
    Profile = models.ForeignKey(Profile, null=True, on_delete=models.PROTECT, blank=False)
    post = models.ForeignKey(Post, null=True, on_delete=models.PROTECT, blank=False)
    name = models.CharField(max_length=10)
    reaction = models.CharField(max_length=6)


class Follower(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT, blank=False)
    follower_id = models.ForeignKey(Profile, null=True, on_delete=models.PROTECT, blank=False)