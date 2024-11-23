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