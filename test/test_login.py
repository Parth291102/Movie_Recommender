import pytest
from unittest.mock import patch
import streamlit as st
from main import login_page, load_users, save_users

@pytest.fixture
def mock_users():
    users = {
        "test_user": {
            "email": "test@example.com",
            "password": "hashed_password",
            "email": "test1@example.com",
            "password": "test_1",
        }
    }
    return users

def test_login_with_valid_user(mock_users):
    with patch("main.load_users", return_value=mock_users), patch("main.st.text_input", return_value="test_user"), patch("main.st.button", return_value=True):
        with patch("main.st.session_state", {}):
            login_page()
            assert st.session_state["username"] == "test_user"
            assert st.success.called

def test_login_with_invalid_user(mock_users):
    with patch("main.load_users", return_value=mock_users), patch("main.st.text_input", return_value="invalid_user"), patch("main.st.button", return_value=True):
        with patch("main.st.session_state", {}):
            login_page()
            assert not hasattr(st.session_state, "username")
            assert st.error.called

def test_signup_with_new_user(mock_users):
    new_users = mock_users.copy()
    with patch("main.load_users", return_value=mock_users), patch("main.st.text_input", side_effect=["new_user", "new_email@example.com", "password", "password"]), patch("main.st.button", return_value=True):
        with patch("main.st.session_state", {}), patch("main.save_users") as save_mock:
            login_page()
            save_mock.assert_called_once_with({**mock_users, "new_user": {"email": "new_email@example.com", "password": "hashed_password"}})

def test_signup_with_new_user1(mock_users):
    new_users = mock_users.copy()
    with patch("main.load_users", return_value=mock_users), patch("main.st.text_input", side_effect=["new_user", "new_email1@example.com", "password1", "password1"]), patch("main.st.button", return_value=True):
        with patch("main.st.session_state", {}), patch("main.save_users") as save_mock:
            login_page()
            save_mock.assert_called_once_with({**mock_users, "new_user": {"email": "new_email@example.com", "password": "hashed_password"}})

def test_signup_with_existing_user(mock_users):
    with patch("main.load_users", return_value=mock_users), patch("main.st.text_input", side_effect=["test_user", "new_email@example.com", "password", "password"]), patch("main.st.button", return_value=True):
        with patch("main.st.session_state", {}):
            login_page()
            assert st.error.called

def test_signup_with_existing_user1(mock_users):
    with patch("main.load_users", return_value=mock_users), patch("main.st.text_input", side_effect=["test_user1", "new_email1@example.com", "password1", "password1"]), patch("main.st.button", return_value=True):
        with patch("main.st.session_state", {}):
            login_page()
            assert st.error.called

def test_signup_password_mismatch(mock_users):
    with patch("main.load_users", return_value=mock_users), patch("main.st.text_input", side_effect=["new_user", "new_email@example.com", "password", "wrong_password"]), patch("main.st.button", return_value=True):
        with patch("main.st.session_state", {}):
            login_page()
            assert st.error.called

def test_signup_empty_fields(mock_users):
    with patch("main.load_users", return_value=mock_users), patch("main.st.text_input", side_effect=["", "new_email@example.com", "", ""]), patch("main.st.button", return_value=True):
        with patch("main.st.session_state", {}):
            login_page()

def test_duplicate_signup():
    users = {"existing_user": {"email": "test@example.com", "password": "hashed_password"}}
    with pytest.raises(Exception, match="Username or email already exists."):
        validate_signup("existing_user", "new_password", users)

def test_empty_login_input():
    username = ""
    password = ""
    with pytest.raises(Exception, match="All fields are required."):
        validate_login(username, password)

def test_login_page_ui_elements():
    login_page()
    assert st.text_input.called_with("Username")
    assert st.text_input.called_with("Password")
    assert st.button.called_with("Login")
            assert st.error.called  # Expect an error message for empty fields

def test_successful_login():
    users = {"valid_user": {"email": "valid@example.com", "password": hash_password("valid_password")}}
    st.session_state['logged_in'] = False
    validate_login("valid_user", "valid_password", users)
    assert st.session_state['logged_in'] is True

def test_password_strength():
    with pytest.raises(Exception, match="Password must be at least 8 characters."):
        validate_password("12345")
