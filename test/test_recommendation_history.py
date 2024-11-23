def test_recommendation_history():
    st.session_state['recommendation_history'] = []
    update_history("Sample Movie", ["Rec1", "Rec2"])
    assert len(st.session_state['recommendation_history']) == 1
    assert st.session_state['recommendation_history'][0]['movie'] == "Sample Movie"
