import uuid


# A second user with a name that is already taken is refused.
def test_duplicate_username_is_refused(api):
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}

    first = api.post("/api/users", json=user)
    assert first.status_code == 201

    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}


# Logging in with a wrong password is refused.
def test_wrong_password_is_refused(api):
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}

    res = api.post("/api/users", json=user)
    assert res.status_code == 201

    wrong = {"username": name, "password": "Wrong-2026"}
    res = api.post("/api/users/token/login", json=wrong)

    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# A user with an empty name is refused.
def test_empty_username_is_refused(api):
    user = {"username": "", "password": "Pizza-2026"}

    res = api.post("/api/users", json=user)

    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}