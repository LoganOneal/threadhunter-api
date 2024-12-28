from celery import shared_task
from .utils import update_topics
from .models import Subreddit

@shared_task
def process_topics(subreddit_id):
                        
    # Add task id to subreddit 
    subreddit = Subreddit.objects.get(id=subreddit_id)
    subreddit.topic_labeling_task_id = process_topics.request.id
    subreddit.save()
                   
    return update_topics(subreddit_id)

