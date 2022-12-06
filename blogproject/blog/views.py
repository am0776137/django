from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
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


from django.urls import reverse_lazy

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    # reverse_lazy is used in place of reverse, so that this will not execute redirecting 
    # until the view has fisihed deleting the specified post object
    success_url = reverse_lazy('home')
    # In update view, we are redirected to post_detail url which is a detailed post and it uses the 
    # default : get_absolute_url defined in the Post Model to redirect to.
    # But after deletion this redirection is not possible as there is no detailed view available
    # for the deleted post. Hence it is redirected to home using success_url.






