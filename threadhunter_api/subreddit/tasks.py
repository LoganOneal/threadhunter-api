from celery import shared_task
from .utils import update_topics

@shared_task
def process_topics(subreddit_id):
    return update_topics(subreddit_id)

