from celery import shared_task
from .topic_modeling import create_topic_model
from .models import Subreddit

@shared_task
def process_subreddit_topics(subreddit_name):
    try:
        # Get topics using the existing topic modeling function
        topics = create_topic_model(subreddit_name)

        print(topics)
        
        # Update the subreddit with the topics
        #subreddit = Subreddit.objects.get(name=subreddit_name)
        #subreddit.topics = topics
        #subreddit.save()
        
        return f"Successfully processed topics for r/{subreddit_name}"
    except Exception as e:
        return f"Error processing topics for r/{subreddit_name}: {str(e)}" 