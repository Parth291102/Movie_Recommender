import pytest
from unittest.mock import patch
import streamlit as st
from main import Main

# Mock data for movies
@pytest.fixture
def mock_movies_data():
    # Simulate movie data
    movies_df = pd.DataFrame({
        'movie_id': [1, 2, 3, 4, 5],
        'title': ['Inception', 'The Matrix', 'The Dark Knight', 'Interstellar', 'The Prestige'],
        'tags': ['dream, mind, heist', 'virtual reality, action, hacking', 'batman, joker, crime', 
                 'space, love, science', 'magic, rivalry, illusion']
    })
    return movies_df

@pytest.fixture
def mock_main_class():
    # Initialize Main class
    main_instance = Main()
    main_instance.movies = mock_movies_data()
    main_instance.movies2 = mock_movies_data()
    main_instance.new_df = mock_movies_data()
    return main_instance
