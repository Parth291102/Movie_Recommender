def test_empty_login_input():
    username = ""
    password = ""
    with pytest.raises(Exception, match="All fields are required."):
        validate_login(username, password)
