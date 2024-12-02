from celery import shared_task
from .topic_modeling import create_topic_model, train_topic_model
from .models import Subreddit
from .reddit_client import get_subreddit_posts

@shared_task
def process_subreddit_topics(subreddit_name):
    try:
        # get all posts from subreddit
        posts = get_subreddit_posts(subreddit_name)
        print("posts[0]", posts[0])

        # Get topics using the existing topic modeling function
        topic_model = create_topic_model(posts)
        topics, probs = train_topic_model(topic_model, posts)  

        # print the topics for the first post
        print("Post 1", posts[0])
        print("Topic 1", topic_model.get_topic(topics[0]))



        
        # Update the subreddit with the topics
        #subreddit = Subreddit.objects.get(name=subreddit_name)
        #subreddit.topics = topics
        #subreddit.save()
        
        return f"Successfully processed topics for r/{subreddit_name}"
    except Exception as e:
        return f"Error processing topics for r/{subreddit_name}: {str(e)}" 