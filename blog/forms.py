from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.forms import ModelForm
from .models import User, Post, Comments
from django import forms
from ckeditor.widgets import CKEditorWidget


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


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
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'username': False,
            'email': False,
            'first_name': False,
            'last_name': False,
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
        }


class CreatePostForm(ModelForm):
    body = forms.CharField(label=False, max_length=1000, min_length=5,
                           widget=CKEditorWidget(config_name='post-form', attrs={'placeholder': 'Body'}))

    title = forms.CharField(label='Title', max_length=50, min_length=5,
                            widget=forms.TextInput(attrs={'placeholder': 'Title'}))

    subtitle = forms.CharField(label='Subtitle', max_length=100, min_length=5, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Subtitle'}))

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'body')


class CommentForm(ModelForm):
    comment = forms.CharField(label=False, max_length=150, min_length=5,
                              widget=CKEditorWidget(config_name='comment-form', attrs={'placeholder': 'Comment'}))

    class Meta:
        model = Comments
        fields = ('comment',)
