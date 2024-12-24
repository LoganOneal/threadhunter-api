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

        for i in range(0, len(posts)):
            # create the post and add topics to it
            post = Post.objects.create(
                title=posts[i].title,
                content=posts[i].content,
                reddit_id=posts[i].reddit_id,
                subreddit=subreddit
            )
            post_topics = topic_model.get_topic(topics[i])
            for topic_name, probability in post_topics:
                topic, created = Topic.objects.get_or_create(name=topic_name)
                topic.probability = probability
                post.topics.add(topic)
                topic.posts.add(post)
                topic.save()

            post.save()
            
        return f"Successfully processed topics for r/{subreddit.name}"
    except Exception as e:
        return f"Error processing topics for r/{subreddit.name}: {str(e)}"