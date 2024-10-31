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

# Load metadata
metadata = get_data()

# Define the path to the cosine similarity matrix file
cosine_file_path = os.path.join(os.path.dirname(__file__), "cosine_similarity_10k.npz")

# Check if the cosine similarity matrix file exists; if not, create it
if not os.path.exists(cosine_file_path):
    compute_tfidfmatrix(metadata)

# Load the precomputed cosine similarity matrix
data = np.load(cosine_file_path, allow_pickle=True)
cosine_similarity = data["matrix"]
indices = pd.Series(metadata.index, index=metadata["title"]).drop_duplicates()

def get_recommendations(titles):
    """Returns a list of recommended movie titles based on similarity to a list of input movies."""
    movie_indices = [indices[title] for title in titles if title in indices]

    if not movie_indices:
        return []

    # Sum similarity scores across all selected movies
    sim_scores = np.sum(cosine_similarity[movie_indices], axis=0)
    
    # Sort by the highest scores and exclude selected movies from results
    sim_scores = list(enumerate(sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [score for score in sim_scores if score[0] not in movie_indices]

    # Get the top 10 recommended movie indices
    top_similar_indices = [i[0] for i in sim_scores[:10]]

    # Return the top 10 most similar movie titles
    return metadata["title"].iloc[top_similar_indices].tolist()
