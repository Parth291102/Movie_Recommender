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
