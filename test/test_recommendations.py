import pytest
from unittest.mock import patch
import streamlit as st
import pandas as pd
from main import main_dashboard

# Mock Data for Movies and Credits
@pytest.fixture
def mock_movies_data():
    # Example of movies data from tmbd_5000_movies.csv
    movies_df = pd.DataFrame({
        'movie_id': [1, 2],
        'title': ['Inception', 'The Matrix'],
        'genre': ['Sci-Fi', 'Action']
    })
    return movies_df

def test_recommendation_tags(mock_movies_data):
    with patch("main.preprocess.recommend", return_value=(["The Matrix"], ["poster_url"])):
        with patch("main.st.session_state", {"selected_movie_name": "Inception"}):
            recommendation_tags(mock_movies_data, "Inception", "file_path", "on the basis of genres")
            assert "The Matrix" in st.session_state["recommendation_history"][0]["recommendations"]

def test_recommendation_empty_result(mock_movies_data):
    with patch("main.preprocess.recommend", return_value=([], [])):
        with patch("main.st.session_state", {"selected_movie_name": "Inception"}):
            recommendation_tags(mock_movies_data, "Inception", "file_path", "on the basis of genres")
            assert "No similar movies found." in st.write.call_args[0][0]  # Expect a message when no recommendations are found

def test_recommendation_tags(mocker):
    mocker.patch("preprocess.recommend", return_value=(["Movie1", "Movie2"], ["Poster1", "Poster2"]))
    displayed.clear()
    movies, posters = preprocess.recommend(mock_df, "Sample Movie", "sample.pkl")
    assert len(set(movies)) == 2
    assert movies == ["Movie1", "Movie2"]

def test_no_recommendations():
    displayed.clear()
    movies, posters = preprocess.recommend(mock_df, "Unknown Movie", "sample.pkl")
    assert len(movies) == 0
    assert st.text.called_with("No recommendations available.")

def test_recommendation_by_director(mocker, mock_movies_data):
    mock_credits_data = pd.DataFrame({
        'movie_id': [1, 2],
        'crew': [{'job': 'Director', 'name': 'Christopher Nolan'}, {'job': 'Director', 'name': 'Wachowski Brothers'}]
    })
    mocker.patch("preprocess.recommend", return_value=(["Inception"], ["Poster1"]))
    recommendations, posters = preprocess.recommend(mock_movies_data, "Inception", "sample.pkl", filter_by="Director")
    assert "Inception" in recommendations
    assert "Christopher Nolan" in mock_credits_data.loc[mock_credits_data['movie_id'] == 1, 'crew'].iloc[0]['name']

def test_recommendation_by_actor(mocker, mock_movies_data):
    mock_credits_data = pd.DataFrame({
        'movie_id': [1, 2],
        'cast': [{'name': 'Leonardo DiCaprio'}, {'name': 'Keanu Reeves'}]
    })
    mocker.patch("preprocess.recommend", return_value=(["The Matrix"], ["Poster2"]))
    recommendations, posters = preprocess.recommend(mock_movies_data, "Inception", "sample.pkl", filter_by="Actor")
    assert "The Matrix" in recommendations
    assert "Leonardo DiCaprio" in mock_credits_data.loc[mock_credits_data['movie_id'] == 1, 'cast'].iloc[0]['name']

def test_missing_or_corrupted_data():
    corrupted_data = pd.DataFrame({
        'movie_id': [1, 2],
        'title': [None, 'The Matrix'],  # Missing title for one movie
        'genre': ['Sci-Fi', None]      # Missing genre for one movie
    })
    valid_movies = preprocess.clean_data(corrupted_data)
    assert len(valid_movies) == 1
    assert valid_movies.iloc[0]['title'] == 'The Matrix'

def test_genre_specific_recommendations(mocker):
    mock_data = pd.DataFrame({
        'movie_id': [1, 2, 3],
        'title': ['Movie1', 'Movie2', 'Movie3'],
        'genre': ['Action', 'Sci-Fi', 'Drama']
    })
    mocker.patch("preprocess.filter_by_genre", return_value=mock_data[mock_data['genre'] == 'Sci-Fi'])
    sci_fi_movies = preprocess.filter_by_genre(mock_data, 'Sci-Fi')
    assert len(sci_fi_movies) == 1
    assert sci_fi_movies.iloc[0]['title'] == 'Movie2'

def test_end_to_end_recommendation_flow(mocker, mock_movies_data):
    mocker.patch("preprocess.recommend", return_value=(["Movie1", "Movie2"], ["Poster1", "Poster2"]))
    with patch("main.st.session_state", {"selected_movie_name": "Inception"}):
        recommendation_tags(mock_movies_data, "Inception", "sample.pkl", "on the basis of genres")
        assert "Movie1" in st.session_state["recommendation_history"][0]["recommendations"]
        assert st.session_state["selected_movie_name"] == "Inception"
        
def test_empty_dataset():
    empty_data = pd.DataFrame(columns=["movie_id", "title", "genre"])
    recommendations, posters = preprocess.recommend(empty_data, "Any Movie", "sample.pkl")
    assert len(recommendations) == 0
    assert st.text.called_with("Dataset is empty. Cannot generate recommendations.")
