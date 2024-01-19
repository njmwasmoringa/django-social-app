from django.urls import include, path
from rest_framework import routers

from  socialmedia_api.views import *

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
# router.register(r'Reactions', Rea)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]