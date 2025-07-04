from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_employees_route():
    response = client.get("/employees")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert "name" in data[0]
        assert "role" in data[0]
