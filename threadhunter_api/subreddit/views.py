from django.shortcuts import render
from rest_framework.views import APIView
from threadhunter_api.subreddit.models import Subreddit
from threadhunter_api.subreddit.extensions import reddit
from rest_framework.response import Response
from .tasks import process_subreddit_topics
from threadhunter_api.users.tasks import get_users_count
from prawcore.exceptions import Redirect

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
            try:
                reddit_subreddit = reddit.subreddit(name)
                subreddit = Subreddit.objects.create(name=name, 
                                                     description=reddit_subreddit.description, 
                                                     url=reddit_subreddit.url, 
                                                     num_members=reddit_subreddit.subscribers)
                # Trigger the Celery task to process topics
                process_subreddit_topics.delay(subreddit.id)
            except Redirect:
                return Response({"error": "Subreddit not found"}, status=404)
            except Exception as e:
                return Response({"error": str(e)}, status=500)

        return Response({"message": "success"})