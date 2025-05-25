import pytest
from fastapi.testclient import TestClient
from app import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


client = TestClient(app)


def test_add_endpoint():
    response = client.get("/add", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_subtract_endpoint():
    response = client.get("/subtract", params={"a": 5, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3}


def test_multiply_endpoint():
    response = client.get("/multiply", params={"a": 4, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 12}


def test_divide_endpoint():
    response = client.get("/divide", params={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_divide_by_zero_endpoint():
    response = client.get("/divide", params={"a": 5, "b": 0})
    assert response.status_code == 400
    assert response.json()["detail"] == "Division by zero is not allowed."
