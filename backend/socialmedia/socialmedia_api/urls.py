from django.urls import include, path
from rest_framework import routers

from  socialmedia_api.views import *
from socialmedia_api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewSet)
# router.register(r'auth/signin', AuthViewSet, action="signin", basename='auth')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/signin', AuthViewSet.as_view({'post': 'signin'}), name='signin'),
    path('auth/signup', AuthViewSet.as_view({'post': 'signup'}), name='signup'),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]