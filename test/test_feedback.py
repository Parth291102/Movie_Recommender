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