from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..extensions import reddit
from rest_framework.response import Response
from rest_framework import status
from ..tasks import process_topics
from ..extensions import reddit
from ..models import Subreddit

class CommunityListAPIView(APIView):
    """
    API View to query list of communities by their ids
    """
    
    def post(self, request, *args, **kwargs):
        subreddit_names = request.data.get('subreddit_names')
        
        print("Subreddit names:", subreddit_names)
    
        if not subreddit_names or not isinstance(subreddit_names, list):
            return Response({"error": "subreddit_names must be a list of subreddits"}, status=status.HTTP_400_BAD_REQUEST)
        
        response_data = []
        
        for subreddit_name in subreddit_names:
            # Check if subreddit already exists in database
            subreddit = Subreddit.objects.filter(name=subreddit_name).first()
            
            # If subreddit exists, add data to response
            if subreddit:
                response_data.append({
                        "task_status": "Processed",
                        "topic_modeling_task_id": -1,
                        "id": subreddit.id,
                })
            else: 
                # Create the subreddit if it doesn't exist
                try:
                    reddit_subreddit = reddit.subreddit(subreddit_name)
                    subreddit = Subreddit.objects.create(
                        id=reddit_subreddit.id,
                        name=reddit_subreddit.display_name,
                        description=reddit_subreddit.description,
                        url=reddit_subreddit.url,
                        num_members=reddit_subreddit.subscribers
                    )
                    
                    # Trigger the Celery task
                    task = process_topics.delay(subreddit.id)
                    
                    response_data.append({
                        "task_status": "Processing",
                        "topic_modeling_task_id": task.id,
                        "id": subreddit.id,
                    })
                except Exception as e:
                    response_data.append({"error": str(e), "subreddit_name": subreddit_name})
        
        return Response(response_data, status=status.HTTP_200_OK)
