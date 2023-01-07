from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.template.response import TemplateResponse
from .models import Post
from account.models import CustomUser
from .forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.shortcuts import get_object_or_404

# home view
class BlogListView(ListView):
    queryset = Post.objects.filter(status="Publique")
    template_name = "blog/home.html"
    
# personal user view
class PostListView(LoginRequiredMixin,View):
    def get_queryset(self, request):
        return Post.objects.filter(author=request.user)
    
    def get(self, request):
        posts = self.get_queryset(request)
        context = {'user': request.user, 'post_list': posts}
        return TemplateResponse(request, 'blog/post_list.html', context)
    
    
#@@@@@@_____Create data form view
class BlogCreateView(LoginRequiredMixin,CreateView):
    form_class = PostForm
    template_name = "blog/post_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# comment on detail view
class CommentGetView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm
        return context

class CommentPostView(SingleObjectMixin,FormView):
    model = Post
    form_class = CommentForm
    template_name = "blog/post_detail.html"

    def post(self, request, *args: str, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self,form):
        comment = form.save(commit=False)
        comment.post =self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("post_detail", kwargs={"pk":post.pk})

class BlogDetailView(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        view = CommentGetView.as_view()
        return view(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        view = CommentPostView.as_view()
        return view(request,*args, **kwargs)

# updat date form view
class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_update.html"
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
# dele data
class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    #form_class = PostForm
    fields = "__all__"
    success_url= reverse_lazy("home")
    template_name = "blog/post_delete.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
