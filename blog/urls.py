from django.urls import path
from .views import (
    BlogListView, 
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView)

urlpatterns = [
    path("",BlogListView.as_view(),name="home"),
    path("post/new/",BlogCreateView.as_view(),name='post_new'),
    path("post/<int:pk>/",BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/",BlogUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/",BlogDeleteView.as_view(), name="post_delete"),
]


