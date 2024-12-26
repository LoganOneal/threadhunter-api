from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Collection
from ..serializers import CollectionSerializer
from django.http import JsonResponse

class CollectionsAPIView(APIView):
    """
    API View to query all collections for a user
    """

    def get(self, request):
        """
        Retrieve all collections for a user
        """
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        collections = Collection.objects.filter(user_id=user_id)
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)