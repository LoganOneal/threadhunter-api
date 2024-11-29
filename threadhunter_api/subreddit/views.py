from django.shortcuts import render
from rest_framework.views import APIView
from threadhunter_api.subreddit.models import Subreddit
from threadhunter_api.subreddit.serializers import SubredditSerializer

class SubredditAPIView(APIView):
    """
    API View to get subreddit data
    """
    def get(self, request, name):
        # check if subreddit exists in db 
        subreddit = Subreddit.objects.filter(name=name).first() 
        if not subreddit:
            # if not, create it
            subreddit = Subreddit.objects.create(name=name)

        # get subreddit data from reddit
        #subreddit_data = get_subreddit_data(name)

        
        serializer = SubredditSerializer(subreddit)
        return Response(serializer.data)
