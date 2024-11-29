from django.urls import path
from .views import SubredditAPIView

app_name = 'subreddit'

urlpatterns = [
    path("subreddit/", SubredditAPIView.as_view()),
    path("subreddit/<str:name>", SubredditAPIView.as_view()),

]



