def test_prev_page():
    st.session_state['movie_number'] = 10
    prev_page(movies)
    assert st.session_state['movie_number'] == 0
