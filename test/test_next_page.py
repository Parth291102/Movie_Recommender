def test_next_page():
    st.session_state['movie_number'] = 0
    next_page(movies)
    assert st.session_state['movie_number'] == 10
