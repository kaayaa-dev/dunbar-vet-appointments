import pytest

import db
from app import app


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test.db")
    db.init_db()
    app.config["TESTING"] = True
    return app.test_client()


def test_animals_page_returns_200(client):
    resp = client.get("/animals")
    assert resp.status_code == 200


def test_create_animal_and_list(client):
    client.post("/clients/new", data={"name": "Amy", "phone": "0400000000"})
    resp = client.post(
        "/animals/new",
        data={"client_id": "1", "name": "Buddy", "species": "dog", "breed": "labrador"},
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert b"Buddy" in resp.data