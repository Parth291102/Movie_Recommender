def test_recommendation_tags(mocker):
    mocker.patch("preprocess.recommend", return_value=(["Movie1", "Movie2"], ["Poster1", "Poster2"]))
    displayed.clear()
    movies, posters = preprocess.recommend(mock_df, "Sample Movie", "sample.pkl")
    assert len(set(movies)) == 2
    assert movies == ["Movie1", "Movie2"]
