from celery import shared_task
from .topic_modeling import create_topic_model, train_topic_model
from .models import Subreddit, Topic, Post
from .reddit_client import get_subreddit_posts

@shared_task
def process_subreddit_topics(subreddit_id):
    try:
        subreddit = Subreddit.objects.get(id=subreddit_id)

        # get all posts from subreddit
        posts = get_subreddit_posts(subreddit)

        # Get topics using the existing topic modeling function
        try:
            topic_model = create_topic_model()
            topics, probs = train_topic_model(topic_model, posts)
        except Exception as e:
            return f"Error during topic model creation: {str(e)}"

        # print the topics for the first post
        print("Post 1", posts[0])
        print("Topic 1", topic_model.get_topic(topics[0]))
        
        # Save new posts to db
        for post in posts:
            post.save()
        
        # Save topics to db
        for topic, prob in zip(topics, probs):
            print(topic, prob)



        return f"Successfully processed topics for r/{subreddit.name}"
    except Exception as e:
        return f"Error processing topics for r/{subreddit.name}: {str(e)}"