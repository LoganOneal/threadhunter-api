from django.db import models
from django.contrib.postgres.fields import ArrayField

class Community(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    url = models.URLField()
    num_members = models.IntegerField()
    
    topic_labeling_task_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Subreddit(Community):
    pass

class Post(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.TextField()
    selftext = models.TextField()
    topics = ArrayField(models.CharField(), max_length=255, blank=True, null=True)
    probs = ArrayField(models.FloatField(), blank=True, null=True)
    
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Collection(models.Model):
    name = models.CharField(max_length=255)
    communities = models.ManyToManyField(Subreddit)
    user_id = models.CharField(max_length=255)  # Add this line
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name