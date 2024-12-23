from typing import List
from .extensions import reddit
from .models import Post, Subreddit

def get_subreddit_posts(subreddit: Subreddit, limit: int = 100) -> List[Post]:
    """
    Fetch recent posts from a subreddit
    
    Args:
        subreddit_name (str): Name of the subreddit to fetch posts from
        limit (int): Maximum number of posts to fetch
        
    Returns:
        List[str]: List of post texts (title + content)
    """
    subreddit_query = reddit.subreddit(subreddit.name)
    posts = []
    
    for post in subreddit_query.hot(limit=limit):
        # Combine title and selftext for better context
        posts.append(Post(title=post.title, content=post.selftext, reddit_id=post.id, subreddit=subreddit))
        
    return posts 