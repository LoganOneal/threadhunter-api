from rest_framework.serializers import ModelSerializer
from threadhunter_api.subreddit.models import Subreddit
from rest_framework import serializers
from .models import Collection

class SubredditSerializer(ModelSerializer):
    class Meta:
        model = Subreddit
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

