
# A different user cannot read another user's rating.
def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.get(path, headers=other_auth)
    assert 400 <= res.status_code <= 499

    owner_res = api.get(path, headers=auth)
    assert owner_res.status_code == 200
    assert owner_res.json() == rating
    print("READ status:", res.status_code)



# A different user cannot change another user's rating.
def test_other_user_cannot_update_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.put(path, json={"stars": 4}, headers=other_auth)
    assert 400 <= res.status_code <= 499

    owner_res = api.get(path, headers=auth)
    assert owner_res.status_code == 200
    assert owner_res.json() == rating
    print("UPDATE status:", res.status_code)


# A different user cannot delete another user's rating.
def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.delete(path, headers=other_auth)
    assert 400 <= res.status_code <= 499

    owner_res = api.get(path, headers=auth)
    assert owner_res.status_code == 200
    assert owner_res.json() == rating
    print("DELETE status:", res.status_code)