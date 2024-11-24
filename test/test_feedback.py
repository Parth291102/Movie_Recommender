import pytest
from unittest.mock import patch
from main import update_feedback

# Test for liking a movie
def test_like_movie():
    with patch("main.st.session_state", {"feedback": {}}):
        update_feedback("Inception", "like")
        assert st.session_state["feedback"]["Inception"] == "like"

# Test for disliking a movie
def test_dislike_movie():
    with patch("main.st.session_state", {"feedback": {}}):
        update_feedback("Inception", "dislike")
        assert st.session_state["feedback"]["Inception"] == "dislike"

# Test for providing feedback for multiple movies
def test_multiple_feedback():
    with patch("main.st.session_state", {"feedback": {}}):
        update_feedback("Inception", "like")
        update_feedback("The Matrix", "dislike")
        assert st.session_state["feedback"]["Inception"] == "like"
        assert st.session_state["feedback"]["The Matrix"] == "dislike"

# Test for clearing or overwriting feedback
def test_clear_feedback():
    with patch("main.st.session_state", {"feedback": {"Inception": "like"}}):
        update_feedback("Inception", "dislike")
        assert st.session_state["feedback"]["Inception"] == "dislike"  # Test overwriting previous feedback

# Test for no feedback on unselected movie
def test_no_feedback_on_unselected_movie():
    with patch("main.st.session_state", {"feedback": {}}):
        update_feedback("Inception", "like")
        update_feedback("The Matrix", "dislike")
        assert "The Matrix" in st.session_state["feedback"]

def test_feedback_persistence():
    st.session_state["feedback"] = {}
    update_feedback("Sample Movie", "like")
    update_feedback("Sample Movie", "dislike")
    assert st.session_state["feedback"]["Sample Movie"] == "dislike"

def test_update_feedback():
    st.session_state["feedback"] = {}
    update_feedback("Sample Movie", "like")
    assert st.session_state["feedback"]["Sample Movie"] == "like"

def test_dislike_movie_from_csv():
    with patch("main.st.session_state", {"feedback": {}}):
        movie_data = pd.read_csv("tmdb_5000_movies.csv")
        movie_title = movie_data.iloc[1]["title"]  # Second movie in the dataset
        update_feedback(movie_title, "dislike")
        assert st.session_state["feedback"][movie_title] == "dislike"

def test_like_movie_from_csv():
    with patch("main.st.session_state", {"feedback": {}}):
        movie_data = pd.read_csv("tmdb_5000_movies.csv")  
        movie_title = movie_data.iloc[0]["title"]  
        update_feedback(movie_title, "like")
        assert st.session_state["feedback"][movie_title] == "like"        