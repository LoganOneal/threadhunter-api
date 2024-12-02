from bertopic import BERTopic
from typing import Dict, Any, List
from sklearn.feature_extraction.text import CountVectorizer
from bertopic.vectorizers import ClassTfidfTransformer
from bertopic.representation import KeyBERTInspired

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
    vectorizer_model = CountVectorizer(stop_words="english")
    ctfidf_model = ClassTfidfTransformer(reduce_frequent_words=True)
    representation_model = KeyBERTInspired()

    topic_model = BERTopic(vectorizer_model=vectorizer_model, 
                           ctfidf_model=ctfidf_model, 
                           representation_model=representation_model)

    return topic_model

def train_topic_model(topic_model: BERTopic, texts: List[str]) -> tuple[List[int], List[float]]:
    """
    Train topic model and return topics and probabilities

    Args:
        topic_model (BERTopic): BERTopic model
        
    Returns:
        Tuple[List[int], List[float]]: Topics and probabilities
    """
    topics, probs = topic_model.fit_transform(texts)

    return topics, probs
