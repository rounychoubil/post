from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class BlogListView(ListView):
    model = Post
    template_name = "blog/home.html"

class BlogCreateView(LoginRequiredMixin,CreateView):
    form_class = PostForm
    template_name = "blog/post_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_update.html"
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    #form_class = PostForm
    fields = "__all__"
    success_url= reverse_lazy("home")
    template_name = "blog/post_delete.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
