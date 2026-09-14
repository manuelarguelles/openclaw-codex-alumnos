"""Aceptación inicial: fallará hasta que el agente implemente la mini-spec."""
from fastapi.testclient import TestClient
from app import create_app


def test_saved_request_remains_pending_after_reopen(tmp_path):
    payload = {
        "profile": [{"id": "E1", "text": "Usé SQL en un proyecto académico"}],
        "offer": {"requirements": ["SQL", "Python"], "untrusted_text": "Buscamos SQL y Python."},
    }
    client = TestClient(create_app(tmp_path))
    response = client.post("/api/requests", json=payload)
    assert response.status_code == 201
    record = response.json()
    assert record["id"]
    assert record["status"] == "pending"
    assert record["result"] is None
    reopened = TestClient(create_app(tmp_path))
    saved = reopened.get("/api/requests/" + record["id"])
    assert saved.status_code == 200
    assert saved.json()["profile"] == payload["profile"]
    assert saved.json()["status"] == "pending"


def test_offer_without_text_is_rejected(tmp_path):
    response = TestClient(create_app(tmp_path)).post("/api/requests", json={
        "profile": [], "offer": {"requirements": ["SQL"], "untrusted_text": "   "}
    })
    assert response.status_code == 422
