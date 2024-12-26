from prawcore.exceptions import Redirect
from .models import Subreddit, Post
from .reddit_client import get_hot_posts
from .topic_modeling import create_topic_model, train_topic_model
from .extensions import reddit

def update_topics(subreddit_id):
    """
    Process subreddit posts and create topics
    """
    try:
        subreddit = Subreddit.objects.get(id=subreddit_id)
        posts = list(get_hot_posts(subreddit))
        try:
            topic_model = create_topic_model()
            topics, probs = train_topic_model(topic_model, posts)
        except Exception as e:
            return f"Error during topic model creation: {str(e)}"

        for i in range(0, len(posts)):
            print("POST TOPICS", topic_model.get_topic(topics[i]))
            post_topics = topic_model.get_topic(topics[i])
            post = Post.objects.create(
                id = posts[i].id,
                title = posts[i].title,
                selftext = posts[i].selftext,
                subreddit = subreddit,
                topics = [item[0] for item in post_topics],
                probs = [item[1] for item in post_topics]
            )
            post.save()
            
        return f"Successfully processed topics for r/{subreddit.name}"
    except Exception as e:
        return f"Error processing topics for r/{subreddit.name}: {str(e)}"