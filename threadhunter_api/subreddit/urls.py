from django.urls import path
from .views import CommunityAPIView, CollectionAPIView, CollectionsAPIView, CommunitySearchAPIView

app_name = 'subreddit'

urlpatterns = [
    path("search/<str:keyword>/", CommunitySearchAPIView.as_view()),
    path("subreddit/", CommunityAPIView.as_view()),
    path("subreddit/<str:name>", CommunityAPIView.as_view()),
    path('community/<str:name>/', CommunityAPIView.as_view(), name='community-detail'),
    path('collection/', CollectionAPIView.as_view(), name='collection-create'),
    path('collection/<int:collection_id>/', CollectionAPIView.as_view(), name='collection-detail'),
    path('collections/', CollectionsAPIView.as_view(), name='user-collections'),
]



