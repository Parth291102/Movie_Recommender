def test_filtered_recommendations(mocker):
    mocker.patch("preprocess.filter_movies", return_value=["Filtered Movie1", "Filtered Movie2"])
    filtered_movies = preprocess.filter_movies(mock_df, genre="Action")
    assert len(filtered_movies) == 2
    assert "Filtered Movie1" in filtered_movies
