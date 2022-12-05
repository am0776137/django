from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # to get absolute url through url template name


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # we are setting post_detail as we want to redirect to detailed post view
        # right after creating it.
        return reverse('post_detail', args=[str(self.id)]) # post_detail takes id of the post as argument. So it is provided


    
    