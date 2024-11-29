from django.db import models

# Create your models here.

class Subreddit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(unique=True)
    num_members = models.IntegerField()
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
