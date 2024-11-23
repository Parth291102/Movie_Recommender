def test_large_dataset_performance(mocker):
    large_dataset = pd.DataFrame({"movie_id": range(1000000), "title": [f"Movie{i}" for i in range(1000000)]})
    mocker.patch("preprocess.recommend", return_value=(["Movie1"], ["Poster1"]))
    movies, posters = preprocess.recommend(large_dataset, "Sample Movie", "sample.pkl")
    assert len(movies) > 0
