import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os

def get_data(movie_length=10000):
    """Loads movie metadata and returns a subset."""
    file_path = os.path.join(os.path.dirname(__file__), "movies_metadata.csv")
    metadata = pd.read_csv(file_path, low_memory=False)
    return metadata[:movie_length]

def compute_tfidfmatrix(metadata):
    """Computes and saves the cosine similarity matrix using TF-IDF on the 'overview' column."""
    tfidf = TfidfVectorizer(stop_words="english")
    metadata["overview"] = metadata["overview"].fillna("")  # Handle NaN values
    tfidf_matrix = tfidf.fit_transform(metadata["overview"])
    
    cosine_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)
    cosine_file_path = os.path.join(os.path.dirname(__file__), "cosine_similarity_10k.npz")
    np.savez(cosine_file_path, matrix=cosine_similarity)

# Load metadata and cosine similarity matrix
metadata = get_data()
cosine_file_path = os.path.join(os.path.dirname(__file__), "cosine_similarity_10k.npz")

if not os.path.exists(cosine_file_path):
    compute_tfidfmatrix(metadata)

data = np.load(cosine_file_path, allow_pickle=True)
cosine_similarity = data["matrix"]
indices = pd.Series(metadata.index, index=metadata["title"]).drop_duplicates()

def generate_weighted_recommendations(history_data):
    """
    Generates movie recommendations based on past recommendations with weighted frequency.

    Args:
        history_data (list of dict): Each entry contains keys: 'movie_title', 'frequency'.

    Returns:
        list: A list of recommended movie titles.
    """
    # Prepare titles with weights based on frequency
    titles_with_weights = {entry['movie_title']: entry['frequency'] for entry in history_data}
    weighted_titles = list(titles_with_weights.keys())
    weighted_values = list(titles_with_weights.values())

    # Map titles to indices and apply weights
    movie_indices = [indices[title] for title in weighted_titles if title in indices]
    if not movie_indices:
        return []

    # Calculate weighted similarity scores
    sim_scores = np.zeros(cosine_similarity.shape[0])
    for i, idx in enumerate(movie_indices):
        sim_scores += cosine_similarity[idx] * weighted_values[i]  # Apply frequency weight

    # Sort movies by highest scores and exclude already recommended movies
    sim_scores = list(enumerate(sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [score for score in sim_scores if score[0] not in movie_indices]

    # Get top 10 recommendations
    top_similar_indices = [i[0] for i in sim_scores[:10]]
    return metadata["title"].iloc[top_similar_indices].tolist()

# Example usage
if __name__ == "__main__":
    # Sample history data in the specified format
    sample_history_data = [
        {"movie_title": "Election", "frequency": 2},
        {"movie_title": "Radio", "frequency": 2},
        {"movie_title": "The Official Story", "frequency": 2},
        {"movie_title": "Some Girl", "frequency": 1},
        {"movie_title": "Blackboard Jungle", "frequency": 2},
        {"movie_title": "The Five Venoms", "frequency": 1},
        {"movie_title": "Sidekicks", "frequency": 1},
        {"movie_title": "Home Room", "frequency": 2},
        {"movie_title": "Masques", "frequency": 1},
        {"movie_title": "Mona Lisa Smile", "frequency": 2},
        {"movie_title": "Trippin'", "frequency": 1},
        {"movie_title": "Storytelling", "frequency": 1},
        {"movie_title": "The Breakfast Club", "frequency": 1},
        {"movie_title": "The Substitute", "frequency": 1}
    ]
    
    recommendations = generate_weighted_recommendations(sample_history_data)
    print("Weekly personalized recommendations:", recommendations)
