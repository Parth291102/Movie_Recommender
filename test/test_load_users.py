def test_load_users(tmp_path):
    sample_data = {"test_user": {"email": "test@example.com", "password": "hashed_password"}}
    users_file = tmp_path / "users.json"
    users_file.write_text(json.dumps(sample_data))
    assert load_users() == sample_data
