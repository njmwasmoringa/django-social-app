from django.contrib import admin
from socialmedia_api.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reaction)
admin.site.register(Follower)
