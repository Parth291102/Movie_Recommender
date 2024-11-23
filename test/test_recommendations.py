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

@pytest.fixture
def mock_credits_data():
    # Example of credits data from tmbd_5000_credits.csv
    credits_df = pd.DataFrame({
        'movie_id': [1, 2],
        'cast': ['Leonardo DiCaprio, Joseph Gordon-Levitt', 'Keanu Reeves, Laurence Fishburne'],
        'crew': ['Christopher Nolan', 'The Wachowskis']
    })
    return credits_df

def test_initial_options_display(mock_movies_data, mock_credits_data):
    with patch("main.st.selectbox", return_value="Inception"), patch("main.st.button", return_value=True):
        main_dashboard(mock_movies_data, mock_credits_data)
        # Test if the movie options are displayed correctly
        assert st.session_state["selected_movie_name"] == "Inception"

def test_movie_details_display(mock_movies_data, mock_credits_data):
    with patch("main.st.selectbox", return_value="Inception"):
        main_dashboard(mock_movies_data, mock_credits_data)
        # Check if movie details like cast and crew are shown
        assert "Leonardo DiCaprio" in st.write.call_args[0][0]  # Cast details
        assert "Christopher Nolan" in st.write.call_args[0][0]  # Director

def test_recommend_display(mock_movies_data, mock_credits_data):
    with patch("main.st.session_state", {}), patch("main.st.selectbox", return_value="Inception"):
        main_dashboard(mock_movies_data, mock_credits_data)
        # Test if movie recommendation feature is working
        assert st.session_state["selected_movie_name"] == "Inception"