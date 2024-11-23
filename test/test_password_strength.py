def test_password_strength():
    with pytest.raises(Exception, match="Password must be at least 8 characters."):
        validate_password("12345")
