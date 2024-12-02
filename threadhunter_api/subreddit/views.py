from django.shortcuts import render
from rest_framework.views import APIView
from threadhunter_api.subreddit.models import Subreddit
from threadhunter_api.subreddit.serializers import SubredditSerializer
from threadhunter_api.subreddit.extensions import reddit
from rest_framework.response import Response
from .tasks import process_subreddit_topics


from celery.result import EagerResult

from threadhunter_api.users.tasks import get_users_count
from threadhunter_api.users.tests.factories import UserFactory

class SubredditAPIView(APIView):
    """
    API View to get subreddit data
    """

    def get(self, request, name):
        batch_size = 3
        UserFactory.create_batch(batch_size)
        task_result = get_users_count.delay()
        print("task_result", task_result)

        return Response({"message": "success"})
    # old get methodg
    def getold(self, request, name):
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
