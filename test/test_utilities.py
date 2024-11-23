import pytest
from unittest.mock import patch
from main import hash_password, load_users, save_users

# Test for password hashing utility
def test_hash_password():
    password = "securepassword"
    hashed = hash_password(password)
    assert len(hashed) == 64  # SHA-256 hash length
    assert hashed != password  # Ensure hashing occurs

# Test for loading users
def test_load_users():
    with patch("builtins.open", mock_open(read_data='{"user1": {"password": "hashed"}}')):
        users = load_users()
        assert "user1" in users

# Test for saving users
def test_save_users():
    users = {"user1": {"email": "test@example.com", "password": "hashed_password"}}
    with patch("builtins.open", mock_open()) as mock_file:
        save_users(users)
        mock_file.assert_called_once_with("users.json", "w")

# Test for empty users file
def test_load_users_empty_file():
    with patch("builtins.open", mock_open(read_data="")):
        users = load_users()
        assert users == {}

# Test for saving empty data to users file
def test_save_users_empty_data():
    with patch("builtins.open", mock_open()) as mock_file:
        save_users({})
        mock_file.assert_called_once_with("users.json", "w")

def test_file_not_found(mocker):
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    with pytest.raises(FileNotFoundError, match="File not found"):
        load_users()

def test_save_users(tmp_path):
    users = {"test_user": {"email": "test@example.com", "password": "hashed_password"}}
    users_file = tmp_path / "users.json"
    save_users(users)
    assert json.loads(users_file.read_text()) == users

def test_load_users(tmp_path):
    sample_data = {"test_user": {"email": "test@example.com", "password": "hashed_password"}}
    users_file = tmp_path / "users.json"
    users_file.write_text(json.dumps(sample_data))
    assert load_users() == sample_data

