from django.urls import path
from .views import BlogListView, BlogAboutView

urlpatterns = [
    path("", BlogListView.as_view(), name='home'),
    path("about/", BlogAboutView.as_view(), name='about')
]