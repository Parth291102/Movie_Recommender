def test_no_recommendations():
    displayed.clear()
    movies, posters = preprocess.recommend(mock_df, "Unknown Movie", "sample.pkl")
    assert len(movies) == 0
    assert st.text.called_with("No recommendations available.")
