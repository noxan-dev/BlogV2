from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, filters
from blog.models import User, Post, Comments
from .serializers import UserSerializer, PostSerializer, CommentsSerializer

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
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        queryset = User.objects.all()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # get object by id and username
    def get_object(self, queryset=None, **kwargs):
        user = self.request.filter('username')
        return get_object_or_404(Post, pk=user)

    def get_queryset(self):
        return Post.objects.all()


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def get_object(self, queryset=None, **kwargs):
        user = self.request.filter('username')
        return get_object_or_404(Comments, pk=user)

    def get_queryset(self):
        return Comments.objects.all()
