def test_update_feedback():
    st.session_state["feedback"] = {}
    update_feedback("Sample Movie", "like")
    assert st.session_state["feedback"]["Sample Movie"] == "like"
