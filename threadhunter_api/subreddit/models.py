from django.db import models


class Subreddit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    url = models.URLField()
    num_members = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    reddit_id = models.CharField(max_length=255, unique=True)

    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    topics = models.ManyToManyField('Topic', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    probability = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name