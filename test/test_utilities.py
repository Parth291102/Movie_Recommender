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