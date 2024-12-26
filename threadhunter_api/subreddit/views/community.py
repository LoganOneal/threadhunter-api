from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..tasks import process_topics
from ..extensions import reddit
from ..models import Subreddit


class CommunityAPIView(APIView):
    """
    API View to get subreddit data
    """
    
    def get(self, request, name):        
        # Check if subreddit already exists in database
        subreddit = Subreddit.objects.filter(name=name).first()
        
        # If subreddit exists, return data
        if subreddit:
            return Response({
                "name": subreddit.name,
                "description": subreddit.description,
                "url": subreddit.url,
                "num_members": subreddit.num_members,
            })
        else: 
            # Create the subreddit if it doesn't exist
            try:
                reddit_subreddit = reddit.subreddit(name)
                subreddit = Subreddit.objects.create(
                    id=reddit_subreddit.id,
                    name=name,
                    description=reddit_subreddit.description,
                    url=reddit_subreddit.url,
                    num_members=reddit_subreddit.subscribers
                )
                
                # Trigger the Celery task
                task = process_topics.delay(subreddit.id)
                return Response({"message": "Subreddit created, topic analysis task started", "task_id": task.id}, status=202)
            except Exception as e:
                return Response({"error": str(e)}, status=500)

