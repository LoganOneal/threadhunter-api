
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import  Collection
from ..serializers import CollectionSerializer


class CollectionAPIView(APIView):
    """
    API View to create and query a single collection of communities
    """

    def post(self, request):
        """
        Create a new collection of communities
        """
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            collection = serializer.save(user_id=user_id)
            return Response({"message": "Collection created", "collection_id": collection.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, collection_id):
        """
        Retrieve a collection of communities by ID
        """
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            collection = Collection.objects.get(id=collection_id, user_id=user_id)
            serializer = CollectionSerializer(collection)
            return Response(serializer.data)
        except Collection.DoesNotExist:
            return Response({"error": "Collection not found"}, status=status.HTTP_404_NOT_FOUND)

