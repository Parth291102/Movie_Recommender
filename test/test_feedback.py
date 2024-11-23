import pytest
from unittest.mock import patch
from main import update_feedback

# Test for liking a movie
def test_like_movie():
    with patch("main.st.session_state", {"feedback": {}}):
        update_feedback("Inception", "like")
        assert st.session_state["feedback"]["Inception"] == "like"