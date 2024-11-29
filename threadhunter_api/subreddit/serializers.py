from rest_framework.serializers import ModelSerializer
from threadhunter_api.subreddit.models import Subreddit
class SubredditSerializer(ModelSerializer):
    class Meta:
        model = Subreddit
        fields = '__all__'
    
