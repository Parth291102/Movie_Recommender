def test_feedback_persistence():
    st.session_state["feedback"] = {}
    update_feedback("Sample Movie", "like")
    update_feedback("Sample Movie", "dislike")
    assert st.session_state["feedback"]["Sample Movie"] == "dislike"
