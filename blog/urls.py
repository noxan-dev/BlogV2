from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),

    path('create-post/', views.CreatePosts.as_view(), name='create-post'),
    path('edit-post/<uuid:id>', views.EditPosts.as_view(), name='edit-post'),
    path('delete-post/<uuid:id>', views.DeletePosts.as_view(), name='delete-post'),

    path('post/<uuid:id>', views.ViewPost.as_view(), name='post'),

    path('profile/<uuid:id>/<str:username>/', views.Profile.as_view(), name='profile'),
]
