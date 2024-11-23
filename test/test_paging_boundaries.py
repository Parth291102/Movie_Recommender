def test_paging_boundaries():
    st.session_state['movie_number'] = 0
    movies = ["Movie1", "Movie2", "Movie3"]
    prev_page(movies)
    assert st.session_state['movie_number'] == 0  # Cannot go below 0

    st.session_state['movie_number'] = 3
    next_page(movies)
    assert st.session_state['movie_number'] == 3  # Cannot go beyond dataset length
