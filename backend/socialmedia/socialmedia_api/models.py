from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete = models.PROTECT,
        blank = False
    )
    fullname = models.CharField(max_length=50)
    avatar = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=200)


class Post(models.Model):
    user = models.ForeignKey(
        User,
        related_name="posts",
        on_delete = models.PROTECT,
        blank = False
    )
    message = models.CharField(max_length=100)
    media = models.CharField(max_length=32)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, blank=False)
    message = models.CharField(max_length=100)


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, blank=False)
    name = models.CharField(max_length=10)
    reaction = models.CharField(max_length=6)


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    follower_id = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=False)