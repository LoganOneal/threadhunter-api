from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..extensions import reddit

class CommunitySearchAPIView(APIView):
    """
    API View to search for communities by keyword
    """
    
    def get(self, request, keyword):
        try:
            subreddits = reddit.subreddits.search(keyword)
            results = []
            for subreddit in subreddits:
                results.append({
                    "name": subreddit.display_name,
                    "title": subreddit.title,
                    "description": subreddit.public_description,
                    "url": subreddit.url,
                    "num_members": subreddit.subscribers,
                })
            return Response(results, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
