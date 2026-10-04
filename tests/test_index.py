import app as flask_app
import db


def test_homepage_has_navigation_links(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test.db")
    db.init_db()
    client = flask_app.app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"/clients" in resp.data
    assert b"/animals" in resp.data
    assert b"/properties" in resp.data
    assert b"/appointments" in resp.data