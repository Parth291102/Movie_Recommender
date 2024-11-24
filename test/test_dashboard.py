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

def test_feedback_summary(mock_movies_data, mock_credits_data):
    with patch("main.st.session_state", {"feedback": {"Inception": "like"}}):
        main_dashboard(mock_movies_data, mock_credits_data)
        assert "Movies You Liked:" in st.write.call_args[0][0]

def test_invalid_movie_selection(mock_movies_data, mock_credits_data):
    with patch("main.st.session_state", {"selected_movie_name": "Invalid Movie"}):
        main_dashboard(mock_movies_data, mock_credits_data)

def test_display_movie_details(mocker):
    mocker.patch("preprocess.get_details", return_value=["Poster", "Overview", ["Genre1", "Genre2"]])
    display_movie_details("Sample Movie")
    assert st.image.called_once_with("Poster")
        assert st.error.called  # Expect an error for invalid selection

def test_invalid_movie_name():
    with pytest.raises(ValueError, match="Movie not found in the dataset."):
        preprocess.recommend(mock_df, "Invalid Movie", "sample.pkl")

def test_navigation_buttons(mocker):
    mocker.patch("streamlit.button", side_effect=["Dashboard", "Logout"])
    assert st.button.called_with("Dashboard")
    assert st.button.called_with("Logout")

def test_next_page():
    st.session_state['movie_number'] = 0
    next_page(movies)
    assert st.session_state['movie_number'] == 10

def test_data_loading(mock_movies_data, mock_credits_data):
    assert not mock_movies_data.empty, "Movies data is empty"
    assert not mock_credits_data.empty, "Credits data is empty"

def test_movie_search_functionality(mock_movies_data, mock_credits_data):
    with patch("main.st.selectbox", return_value="The Matrix"):
        main_dashboard(mock_movies_data, mock_credits_data)
        assert st.session_state["selected_movie_name"] == "The Matrix"

def test_empty_movie_data():
    empty_movie_data = pd.DataFrame(columns=["movie_id", "title", "genre"])
    with patch("main.st.selectbox", return_value="Inception"):
        main_dashboard(empty_movie_data, mock_credits_data)
        assert st.write.called_with("No movies available.")

def test_movie_poster_display(mock_movies_data, mock_credits_data):
    with patch("main.st.selectbox", return_value="Inception"):
        main_dashboard(mock_movies_data, mock_credits_data)
        assert st.image.called, "Movie poster is not displayed"
