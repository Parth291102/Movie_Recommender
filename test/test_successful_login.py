def test_successful_login():
    users = {"valid_user": {"email": "valid@example.com", "password": hash_password("valid_password")}}
    st.session_state['logged_in'] = False
    validate_login("valid_user", "valid_password", users)
    assert st.session_state['logged_in'] is True
