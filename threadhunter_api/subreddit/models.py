from django.db import models

# Create your models here.

class Subreddit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    url = models.URLField()
    num_members = models.IntegerField()
    # topics = models.JSONField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
