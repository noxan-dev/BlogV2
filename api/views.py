from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, filters
from blog.models import User, Post, Comments
from .serializers import UserSerializer, PostSerializer, CommentsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
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
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['username']

    @action(detail=True, methods=['get', 'post'])
    def reset_password(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.method == 'GET':
            return Response({'password': user.password})
        elif request.method == 'POST':
            user.set_password(request.data['password'])
            user.save()
            return Response({'password': user.password})


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    search_fields = ('title', 'author')

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    search_fields = ('user',)

