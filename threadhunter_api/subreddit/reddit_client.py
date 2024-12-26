from typing import List
from .extensions import reddit
from .models import Post, Subreddit

def query_subreddit(subreddit_name: str) -> Subreddit:
    """Fetch subreddit data from Reddit API"""
    reddit_subreddit = reddit.subreddit(subreddit_name)
    return Subreddit(
        name=reddit_subreddit.display_name,
        description=reddit_subreddit.description,
        url=reddit_subreddit.url,
        num_members=reddit_subreddit.subscribers
    )

def get_hot_posts(subreddit: Subreddit, limit: int = 100) -> List[Post]:
    """
    Fetch recent posts from a subreddit
    
    Args:
        subreddit_name (str): Name of the subreddit to fetch posts from
        limit (int): Maximum number of posts to fetch
        
    Returns:
        List[str]: List of post texts (title + content)
    """
    sub = reddit.subreddit(subreddit.name)
    
    return sub.hot(limit=limit)
        
    return posts 

def get_top_subreddits(limit: int = 100) -> List[Subreddit]:
    """
    Fetch top subreddits based on subscribers
    
    Args:
        limit (int): Maximum number of subreddits to fetch
        
    Returns:
        List[dict]: List of subreddit data
    """
    return reddit.subreddits.popular(limit=limit)
    