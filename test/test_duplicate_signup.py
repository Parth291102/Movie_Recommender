def test_duplicate_signup():
    users = {"existing_user": {"email": "test@example.com", "password": "hashed_password"}}
    with pytest.raises(Exception, match="Username or email already exists."):
        validate_signup("existing_user", "new_password", users)
