from django.shortcuts import render
from rest_framework.views import APIView
from threadhunter_api.subreddit.models import Subreddit
from threadhunter_api.subreddit.serializers import SubredditSerializer
from threadhunter_api.subreddit.extensions import reddit
from rest_framework.response import Response
from .reddit_client import get_subreddit_posts
from .tasks import process_subreddit_topics

class SubredditAPIView(APIView):
    """
    API View to get subreddit data
    """
    def get(self, request, name):
        # check if subreddit exists in db 
        subreddit = Subreddit.objects.filter(name=name).first() 
        
        # create subreddit if not exists
        if not subreddit:
            print(f"Creating subreddit {name}")
            reddit_subreddit = reddit.subreddit(name)
            subreddit = Subreddit.objects.create(name=name, 
                                                description=reddit_subreddit.description, 
                                                url=reddit_subreddit.url, 
                                                num_members=reddit_subreddit.subscribers)
            
            # Trigger the Celery task to process topics
            process_subreddit_topics.delay(name)

        response_data = SubredditSerializer(subreddit).data
        return Response(response_data)
