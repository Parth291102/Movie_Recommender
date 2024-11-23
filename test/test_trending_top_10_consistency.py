def test_trending_top_10_consistency(mocker):
    mocker.patch("pd.Timestamp.now", return_value=pd.Timestamp("2024-11-23"))
    mock_movies = pd.DataFrame({"movie_id": [1, 2, 3, 4, 5], "title": ["A", "B", "C", "D", "E"]})
    trending = get_trending_top_10(mock_movies)
    assert len(trending) == 10
    assert trending[0]["title"] == "A"
