from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView 
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class BlogListView(ListView):
    model = Post
    template_name = "blog/home.html"

class BlogCreateView(CreateView):
    form_class = PostForm
    template_name = "blog/post_new.html"
    #fields = "__all__"

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
