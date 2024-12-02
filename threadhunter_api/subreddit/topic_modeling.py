from bertopic import BERTopic
from typing import Dict, Any, List

def create_topic_model(texts: List[str], n_topics: int = 10) -> Dict[str, Any]:
    """
    Create topic model from texts using BERTopic
    
    Args:
        texts (List[str]): List of text documents to analyze
        n_topics (int): Number of topics to generate
        
    Returns:
        Dict[str, Any]: Topic analysis results including topics and summary statistics
    """

    print("texts[0]", texts[0])
    
    # Initialize and fit BERTopic model
    topic_model = BERTopic(n_gram_range=(1, 2), 
                          min_topic_size=5, 
                          nr_topics=n_topics)
    
    topics, probs = topic_model.fit_transform(texts)
    
    # Get topic info
    topic_info = topic_model.get_topic_info()
    
    # Format results
    results = {
        "topics": [],
        "summary": {}
    }
    
    # Add each topic's keywords and representative docs
    for topic_id in range(min(n_topics, len(topic_info)-1)):  # -1 to skip outlier topic (-1)
        if topic_id == -1:  # Skip outlier topic
            continue
            
        topic_keywords = topic_model.get_topic(topic_id)
        topic_docs = topic_model.get_representative_docs(topic_id)
        
        results["topics"].append({
            "id": topic_id,
            "keywords": [word for word, _ in topic_keywords[:5]],  # Top 5 keywords
            "sample_posts": topic_docs[:3]  # 3 example posts
        })
    
    # Add summary statistics
    results["summary"] = {
        "total_posts": len(texts),
        "total_topics": len(results["topics"]),
        "avg_posts_per_topic": len(texts) / max(len(results["topics"]), 1)
    }
    
    return results 