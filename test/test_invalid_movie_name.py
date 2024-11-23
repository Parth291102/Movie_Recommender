def test_invalid_movie_name():
    with pytest.raises(ValueError, match="Movie not found in the dataset."):
        preprocess.recommend(mock_df, "Invalid Movie", "sample.pkl")
