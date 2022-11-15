from django.db import models


# Create your models here.

class Post(models.Model):
    created_on = models.DateTimeField()
    title = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title

