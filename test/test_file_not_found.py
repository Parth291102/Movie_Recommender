def test_file_not_found(mocker):
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    with pytest.raises(FileNotFoundError, match="File not found"):
        load_users()
