def test_save_users(tmp_path):
    users = {"test_user": {"email": "test@example.com", "password": "hashed_password"}}
    users_file = tmp_path / "users.json"
    save_users(users)
    assert json.loads(users_file.read_text()) == users
