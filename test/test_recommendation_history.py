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

# Test case for adding a new recommendation to the history
def test_recommendation_history(mock_main_class):
    # Mock recommendation return values
    with patch("main.preprocess.recommend", return_value=(["The Matrix", "Interstellar"], ["poster_url1", "poster_url2"])):
        with patch("main.st.session_state", {"selected_movie_name": "Inception"}):
            # Simulate recommending movies
            main_instance = mock_main_class
            main_instance.recommendation_tags(main_instance.new_df, "Inception", "file_path", "on the basis of genres")

            # Check if the recommendation history is updated correctly
            recommendation_history = st.session_state.get("recommendation_history", [])
            assert len(recommendation_history) == 1  # History should contain one entry
            assert recommendation_history[0]["movie"] == "Inception"  # Correct movie title
            assert "The Matrix" in recommendation_history[0]["recommendations"]  # "The Matrix" should be in recommendations
            assert "Interstellar" in recommendation_history[0]["recommendations"]  # "Interstellar" should be in recommendations

# Test case for multiple recommendations being added to the history
def test_multiple_recommendations_history(mock_main_class):
    # Mock recommendation return values
    with patch("main.preprocess.recommend", return_value=(["The Matrix", "Interstellar"], ["poster_url1", "poster_url2"])):
        with patch("main.st.session_state", {"selected_movie_name": "Inception"}):
            # First recommendation
            main_instance = mock_main_class
            main_instance.recommendation_tags(main_instance.new_df, "Inception", "file_path", "on the basis of genres")
            
            # Second recommendation for a different movie
            with patch("main.st.session_state", {"selected_movie_name": "The Matrix"}):
                main_instance.recommendation_tags(main_instance.new_df, "The Matrix", "file_path", "on the basis of genres")
            
            # Check if recommendation history has both entries
            recommendation_history = st.session_state.get("recommendation_history", [])
            assert len(recommendation_history) == 2  # History should now contain two entries
            assert recommendation_history[1]["movie"] == "The Matrix"  # Second entry should be for "The Matrix"
            assert "Inception" not in recommendation_history[1]["recommendations"]  # "Inception" should not be recommended again

# Test case for recommendation history retention across multiple runs
def test_recommendation_history_retention(mock_main_class):
    # Mock session state with a pre-existing history
    with patch("main.st.session_state", {"recommendation_history": [
        {"movie": "Inception", "recommendations": ["The Matrix", "Interstellar"]},
        {"movie": "The Matrix", "recommendations": ["Inception", "The Dark Knight"]}
    ]}):
        # Simulate a new recommendation for a different movie
        with patch("main.preprocess.recommend", return_value=(["The Prestige", "Interstellar"], ["poster_url3", "poster_url4"])):
            main_instance = mock_main_class
            main_instance.recommendation_tags(main_instance.new_df, "The Prestige", "file_path", "on the basis of genres")
            
            # Check if history is retained and updated correctly
            recommendation_history = st.session_state.get("recommendation_history", [])
            assert len(recommendation_history) == 3  # History should contain three entries now
            assert recommendation_history[2]["movie"] == "The Prestige"  # Last entry should be for "The Prestige"
            assert "Interstellar" in recommendation_history[2]["recommendations"]  # "Interstellar" should be in recommendations