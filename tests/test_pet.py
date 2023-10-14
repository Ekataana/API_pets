from api import Pets

pt = Pets()


def test_get_token():
    status = pt.get_token()[1]
    token = pt.get_token()[0]
    assert token
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    pet_id = pt.get_list_users()[1]
    assert status == 200
    assert pet_id


def test_create_pet():
    status = pt.create_pet()[1]
    pet_id = pt.create_pet()[0]
    assert status == 200
    assert pet_id


def test_get_pet_photo():
    status = pt.get_pet_photo()[0]
    link = pt.get_pet_photo()[1]
    assert status == 200
    assert link


def test_update_pet():
    status = pt.update_pet()
    assert status == 200


def test_like_pet():
    status = pt.like_pet()[0]
    pet_id = pt.like_pet()[1]
    assert status == 200
    assert pet_id


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200
