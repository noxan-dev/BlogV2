from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.forms import ModelForm
from .models import User, Post, Comments
from django import forms


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'name': 'username',
                                                                          'placeholder': 'Username'
                                                                          }))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                              'name': 'password',
                                                                              'placeholder': 'Password',
                                                                              'autocomplete': 'new-password',
                                                                              }))


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                               'name': 'password1',
                                                                               'placeholder': 'Password',
                                                                               'autocomplete': 'new-password',
                                                                               }))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                               'name': 'password2',
                                                                               'placeholder': 'Confirm Password',
                                                                               'autocomplete': 'new-password',
                                                                               }))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'email': False,
            'first_name': False,
            'last_name': False,
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'body')
        labels = {
            'title': False,
            'subtitle': False,
            'body': False,
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitle'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
        labels = {
            'comment': False,
        }
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }
