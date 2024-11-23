def test_hash_password():
    password = "mypassword"
    hashed = hash_password(password)
    assert hashed == hashlib.sha256(password.encode()).hexdigest()
