from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from blog.models import User, Post, Comments
from .serializers import UserSerializer, PostSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_object(self, queryset=None, **kwargs):
        user = self.kwargs.get('pk')
        return get_object_or_404(User, pk=user)

    def get_queryset(self):
        return User.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # get object by id and username
    def get_object(self, queryset=None, **kwargs):
        user = self.request.filter('username')
        return get_object_or_404(Post, pk=user)

    def get_queryset(self):
        return Post.objects.all()
