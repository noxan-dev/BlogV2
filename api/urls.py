from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'comments', views.CommentsViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls))
]
