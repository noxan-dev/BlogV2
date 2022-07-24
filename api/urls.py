from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('posts', views.PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]
