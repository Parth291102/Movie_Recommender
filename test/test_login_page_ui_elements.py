def test_login_page_ui_elements():
    login_page()
    assert st.text_input.called_with("Username")
    assert st.text_input.called_with("Password")
    assert st.button.called_with("Login")
