def test_trending_movies_limit(mocker):
    mock_movies = pd.DataFrame({"movie_id": range(15), "title": [f"Movie{i}" for i in range(15)]})
    trending = get_trending_top_10(mock_movies)
    assert len(trending) == 10
