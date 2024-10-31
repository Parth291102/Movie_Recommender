# import pandas as pd
# import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel


# def get_data(movie_length):
#     metadata = pd.read_csv("movies_metadata.csv", low_memory=False)
#     return metadata[:movie_length]


# def compute_tfidfmatrix(metadata):
#     # Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
#     tfidf = TfidfVectorizer(stop_words="english")

#     # Replace NaN with an empty string
#     metadata["overview"] = metadata["overview"].fillna("")

#     # Construct the required TF-IDF matrix by fitting and transforming the data
#     tfidf_matrix = tfidf.fit_transform(metadata["overview"])

#     cosine_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)
#     np.savez("cosine_similarity_10k", matrix=cosine_similarity)


# # def get_recommendations(title, indices, cosine_sim):
# #     # Get the index of the movie that matches the title

# #     if title not in indices:
# #         return None

# #     idx = indices[title]
# #     print("type")
# #     print(type(indices))
# #     print("indices")
# #     print(indices)
# #     # Get the pairwsie similarity scores of all movies with that movie
# #     sim_scores = list(enumerate(cosine_sim[idx]))

# #     # Sort the movies based on the similarity scores
# #     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

# #     # Get the scores of the 10 most similar movies
# #     sim_scores = sim_scores[1:11]

# #     # Get the movie indices
# #     movie_indices = [i[0] for i in sim_scores]

# #     # Return the top 10 most similar movies
# #     return metadata["title"].iloc[movie_indices]

# def get_recommendations(titles, indices, cosine_sim, metadata):
#     """Returns a list of recommended movie titles based on similarity to a list of input movies."""
#     movie_indices = [indices[title] for title in titles if title in indices]

#     if not movie_indices:
#         return None

#     # Sum the similarity scores across all selected movies
#     sim_scores = np.sum(cosine_sim[movie_indices], axis=0)
    
#     # Sort by the highest scores and exclude selected movies from results
#     sim_scores = list(enumerate(sim_scores))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

#     # Filter out movies that were in the input list
#     sim_scores = [score for score in sim_scores if score[0] not in movie_indices]

#     # Get the top 10 recommended movie indices
#     top_similar_indices = [i[0] for i in sim_scores[:10]]

#     # Return the top 10 most similar movie titles
#     return metadata["title"].iloc[top_similar_indices]

# if __name__ == "__main__":
#     # Load data and compute similarity matrix
#     metadata = get_data(movie_length=10000)

#     # Uncomment below line if you need to generate the similarity matrix
#     compute_tfidfmatrix(metadata)

#     # Load precomputed cosine similarity matrix
#     data = np.load("cosine_similarity_10k.npz", allow_pickle=True)
#     cosine_similarity = data["matrix"]

#     # Map movie titles to their respective index in the DataFrame
#     indices = pd.Series(metadata.index, index=metadata["title"]).drop_duplicates()

#     # Main loop for user interaction
#     play = True
#     while play:
#         movie_input = input("Enter movie titles separated by commas: ")
#         movies = [movie.strip() for movie in movie_input.split(",")]
        
#         recommendations = get_recommendations(movies, indices, cosine_similarity, metadata)

#         if recommendations is None:
#             print("None of the movies are in the database. Please try again.")
#             continue

#         print(f"Movies recommended based on your interest in {', '.join(movies)}:")
#         print(recommendations.to_string(index=False))
        
#         response = input("Do you want another recommendation? (yes/no): ")
#         if response.lower() == "no":
#             play = False



# # if __name__ == "__main__":
# #     metadata = get_data(movie_length=5000)

# #     # compute_tfidfmatrix(metadata)

# #     # Cosine similarity matrix is already saved.
# #     data = np.load("cosine_similarity_5k.npz", allow_pickle=True)
# #     cosine_similarity = data["matrix"]

# #     indices = pd.Series(metadata.index, index=metadata["title"]).drop_duplicates()
# #     play = True
# #     while play != False:
# #         movie = input("Name of movie from movie list: ")
# #         recommendations = get_recommendations(movie, indices, cosine_similarity)
# #         if recommendations is None:
# #             print("Given movie not in database, try again")
# #             continue

# #         print("Following are the recommended movies if you like : ", movie)
# #         print(recommendations)
# #         response = input("Do you want to continue?(yes/no)")
# #         if response == "no":
# #             play = False

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

# # Example of using get_recommendations
# if __name__ == "__main__":
#     example_titles = ["Toy Story", "Jumanji"]
#     recommendations = get_recommendations(example_titles)
#     print("Recommended movies:", recommendations)
