import pytest

import db
from app import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test.db")
    db.init_db()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_index_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_create_client_and_search(client):
    client.post("/clients/new", data={"name": "Alice", "phone": "0400111222"})
    response = client.get("/clients?q=Alice")
    assert b"Alice" in response.data