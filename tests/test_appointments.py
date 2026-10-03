import pytest

import db
from app import app


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test.db")
    db.init_db()
    app.config["TESTING"] = True
    return app.test_client()


def _make_animal(client):
    client.post("/clients/new", data={"name": "Amy", "phone": "0400000000"})
    client.post(
        "/animals/new",
        data={"client_id": "1", "name": "Buddy", "species": "dog"},
    )


def test_appointments_page_returns_200(client):
    resp = client.get("/appointments")
    assert resp.status_code == 200


def test_book_clinic_appointment(client):
    _make_animal(client)
    resp = client.post(
        "/appointments/new",
        data={
            "animal_id": "1",
            "appointment_time": "2026-10-06T09:00",
            "duration_minutes": "30",
            "visit_type": "clinic",
            "room": "R1",
        },
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert b"2026-10-06T09:00" in resp.data


def test_room_conflict_is_rejected(client):
    _make_animal(client)
    data = {
        "animal_id": "1",
        "appointment_time": "2026-10-06T09:00",
        "duration_minutes": "30",
        "visit_type": "clinic",
        "room": "R1",
    }
    client.post("/appointments/new", data=data)
    resp = client.post("/appointments/new", data=data)
    assert b"already booked" in resp.data


def test_farm_visit_requires_60_minutes(client):
    _make_animal(client)
    resp = client.post(
        "/appointments/new",
        data={
            "animal_id": "1",
            "appointment_time": "2026-10-06T09:00",
            "duration_minutes": "30",
            "visit_type": "farm_visit",
        },
    )
    assert b"at least 60 minutes" in resp.data

def test_cancel_appointment_keeps_history(client):
    _make_animal(client)
    client.post(
        "/appointments/new",
        data={
            "animal_id": "1",
            "appointment_time": "2026-10-06T09:00",
            "duration_minutes": "30",
            "visit_type": "clinic",
            "room": "R1",
        },
    )
    client.post("/appointments/1/cancel", follow_redirects=True)
    resp = client.get("/appointments")
    assert b"cancelled" in resp.data


def test_cancelled_room_can_be_rebooked(client):
    _make_animal(client)
    data = {
        "animal_id": "1",
        "appointment_time": "2026-10-06T09:00",
        "duration_minutes": "30",
        "visit_type": "clinic",
        "room": "R1",
    }
    client.post("/appointments/new", data=data)
    client.post("/appointments/1/cancel")
    resp = client.post("/appointments/new", data=data)
    assert b"already booked" not in resp.data