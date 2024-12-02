from celery import shared_task
from .topic_modeling import create_topic_model
from .models import Subreddit
from .reddit_client import get_subreddit_posts

@shared_task
def process_subreddit_topics(subreddit_name):
    try:
        # get all posts from subreddit
        posts = get_subreddit_posts(subreddit_name)

        # Get topics using the existing topic modeling function
        topics = create_topic_model(posts)

        print(topics)
        
        # Update the subreddit with the topics
        #subreddit = Subreddit.objects.get(name=subreddit_name)
        #subreddit.topics = topics
        #subreddit.save()
        
        return f"Successfully processed topics for r/{subreddit_name}"
    except Exception as e:
        return f"Error processing topics for r/{subreddit_name}: {str(e)}" 