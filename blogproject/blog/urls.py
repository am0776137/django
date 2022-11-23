from django.urls import path
from .views import BlogListView, BlogAboutView, BlogDetailView

urlpatterns = [
    path("", BlogListView.as_view(), name='home'),
    path("about/", BlogAboutView.as_view(), name='about'),
    path("post/<int:pk>", BlogDetailView.as_view(), name='post_detail')# to show individual blogposts, this expects to be passed an argument which is a primary key/id
]
