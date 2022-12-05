from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_blog_posts'



class BlogAboutView(TemplateView):
    template_name = 'about.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    # context_object_name = 'post'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
    # fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = "__all__"






