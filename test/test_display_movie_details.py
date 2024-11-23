def test_display_movie_details(mocker):
    mocker.patch("preprocess.get_details", return_value=["Poster", "Overview", ["Genre1", "Genre2"]])
    display_movie_details("Sample Movie")
    assert st.image.called_once_with("Poster")
