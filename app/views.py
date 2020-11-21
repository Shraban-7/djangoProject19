from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,DeleteView,UpdateView
from .models import Post
from .forms import PostForm
# Create your views here.
class Home(TemplateView):
    template_name = 'tuition/home.html'
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex ['msg'] = 'Welcome to our website '
        return contex

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'tuition/create.html'
    success_url = '/'
    # redirect('home')

class PostList(ListView):
    model = Post
    template_name = 'tuition/list.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'tuition/detail.html'

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'tuition/update.html'