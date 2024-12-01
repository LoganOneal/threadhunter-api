from typing import List
from .extensions import reddit

def get_subreddit_posts(subreddit_name: str, limit: int = 100) -> List[str]:
    """
    Fetch recent posts from a subreddit
    
    Args:
        subreddit_name (str): Name of the subreddit to fetch posts from
        limit (int): Maximum number of posts to fetch
        
    Returns:
        List[str]: List of post texts (title + content)
    """
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    
    for post in subreddit.hot(limit=limit):
        # Combine title and selftext for better context
        text = f"{post.title} {post.selftext}".strip()
        if text:  # Only add non-empty posts
            posts.append(text)
    
    return posts 