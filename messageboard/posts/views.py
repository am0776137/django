from django.shortcuts import render

from django.views.generic import TemplateView

from django.views.generic import ListView   # to list the contents of our DB Model : Post
from .models import Post

# Create your views here.

# class HomePageView(TemplateView):
#     template_name = 'home.html'

class HomePageView(ListView):
    # subclass HomePageView from ListView
    # and specify/mention the correct model and template
    
    # ListView automatically returns to us a context variable called object_list that we can
    # loop over via the built-in 'for' template tag. 
    model = Post
    template_name = 'home.html'
    # a customized name for the context in place of object_list
    context_object_name = 'all_posts_list'
    

class AboutPageView(TemplateView):
    template_name = 'about.html'


