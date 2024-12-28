from django.urls import path
from .views import CommunityAPIView, CommunitySearchAPIView, CommunityListAPIView

app_name = 'subreddit'

urlpatterns = [
    path("search-communities/<str:keyword>/", CommunitySearchAPIView.as_view()),
    path("subreddit/", CommunityAPIView.as_view()),
    path("subreddit/<str:name>", CommunityAPIView.as_view()),
    path('communities/<str:name>/', CommunityAPIView.as_view(), name='community-detail'),
    path('communities/', CommunityListAPIView.as_view(), name='community-list'),
]



