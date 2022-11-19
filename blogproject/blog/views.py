from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_blog_posts'



class BlogAboutView(TemplateView):
    template_name = 'about.html'




