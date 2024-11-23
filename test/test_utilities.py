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