def test_navigation_buttons(mocker):
    mocker.patch("streamlit.button", side_effect=["Dashboard", "Logout"])
    assert st.button.called_with("Dashboard")
    assert st.button.called_with("Logout")
