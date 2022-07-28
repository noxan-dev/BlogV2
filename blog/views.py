from django.shortcuts import render
from django.contrib.auth.views import LoginView, FormView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from .forms import CustomLoginForm, CustomUserCreationForm, CreatePostForm
from .models import User, Post

# Create your views here.


class Login(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm


class Register(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class Profile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(id=self.kwargs['id'])
        return context


class CreatePosts(CreateView):
    template_name = 'create-post.html'
    model = Post
    fields = ['title', 'subtitle', 'body']
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(CreatePosts, self).form_valid(form)


class EditPosts(UpdateView):
    model = Post
    template_name = 'create-post.html'
    pk_url_kwarg = 'id'
    form_class = CreatePostForm
    success_url = reverse_lazy('blog:home')


class DeletePosts(DeleteView):
    model = Post
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('blog:home')


