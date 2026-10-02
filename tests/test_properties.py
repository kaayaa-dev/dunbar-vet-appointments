import pytest

import db
from app import app


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test.db")
    db.init_db()
    app.config["TESTING"] = True
    return app.test_client()


def test_properties_page_returns_200(client):
    resp = client.get("/properties")
    assert resp.status_code == 200


def test_create_property_and_list(client):
    client.post("/clients/new", data={"name": "Amy", "phone": "0400000000"})
    resp = client.post(
        "/properties/new",
        data={"client_id": "1", "address": "12 Farm Rd", "property_type": "farm"},
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert b"12 Farm Rd" in resp.data