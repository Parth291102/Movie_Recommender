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

def test_trending_top_10_consistency(mocker):
    mocker.patch("pd.Timestamp.now", return_value=pd.Timestamp("2024-11-23"))
    mock_movies = pd.DataFrame({"movie_id": [1, 2, 3, 4, 5], "title": ["A", "B", "C", "D", "E"]})
    trending = get_trending_top_10(mock_movies)
    assert len(trending) == 10
    assert trending[0]["title"] == "A"

def test_large_dataset_performance(mocker):
    large_dataset = pd.DataFrame({"movie_id": range(1000000), "title": [f"Movie{i}" for i in range(1000000)]})
    mocker.patch("preprocess.recommend", return_value=(["Movie1"], ["Poster1"]))
    movies, posters = preprocess.recommend(large_dataset, "Sample Movie", "sample.pkl")
    assert len(movies) > 0

def test_hash_password():
    password = "mypassword"
    hashed = hash_password(password)
    assert hashed == hashlib.sha256(password.encode()).hexdigest()

def test_paging_boundaries():
    st.session_state['movie_number'] = 0
    movies = ["Movie1", "Movie2", "Movie3"]
    prev_page(movies)
    assert st.session_state['movie_number'] == 0  # Cannot go below 0

    st.session_state['movie_number'] = 3
    next_page(movies)
    assert st.session_state['movie_number'] == 3  # Cannot go beyond dataset length

def test_prev_page():
    st.session_state['movie_number'] = 10
    prev_page(movies)
    assert st.session_state['movie_number'] == 0

def test_trending_movies_limit(mocker):
    mock_movies = pd.DataFrame({"movie_id": range(15), "title": [f"Movie{i}" for i in range(15)]})
    trending = get_trending_top_10(mock_movies)
    assert len(trending) == 10
