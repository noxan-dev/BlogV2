from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView, TemplateView
from django.views.generic import UpdateView, DeleteView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import CustomLoginForm, CustomUserCreationForm, CreatePostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import User, Post, Comments
from django.contrib import messages

# Create your views here.


class Login(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blog:home')


class Register(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('blog:login')
    redirect_authenticated_user = True


class Home(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 4

    def get_context_object_name(self, object_list):
        return 'posts'


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(id=self.kwargs['id'])
        return context


class CreatePosts(PermissionRequiredMixin, CreateView):
    model = Post
    permission_required = 'is_staff'
    template_name = 'create-post.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.title = form.cleaned_data['title']
        obj.subtitle = form.cleaned_data['subtitle']
        obj.body = form.cleaned_data['body']
        obj.save()
        return super(CreatePosts, self).form_valid(form)


class EditPosts(PermissionRequiredMixin, UpdateView):
    model = Post
    permission_required = 'is_staff'
    template_name = 'edit-post.html'
    pk_url_kwarg = 'id'
    form_class = CreatePostForm
    success_url = reverse_lazy('blog:home')


class DeletePosts(PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = 'is_staff'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('blog:home')


class ViewPost(DetailView):
    model = Post
    template_name = 'view-post.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ViewPost, self).get_context_data()
        context['post'] = Post.objects.get(id=self.kwargs.get('id'))
        context['comments'] = Post.objects.get(id=self.kwargs.get('id')).comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if len(request.POST.get('comment')) > 150:
            messages.error(request, 'The word count should not exceed 150 characters')
            return HttpResponseRedirect(request.path)
        elif len(request.POST.get('comment')) < 5:
            messages.error(request, 'Comments should be at least 5 characters long')
            return HttpResponseRedirect(request.path)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.post = Post.objects.get(id=self.kwargs.get('id'))
            obj.save()
            return HttpResponseRedirect(reverse_lazy('blog:post', kwargs={'id': self.kwargs.get('id')}))
        else:
            return HttpResponseRedirect(reverse_lazy('blog:post', kwargs={'id': self.kwargs.get('id')}))


