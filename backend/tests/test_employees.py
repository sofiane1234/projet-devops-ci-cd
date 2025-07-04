import sys
import os
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

client = TestClient(app)

def test_get_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert {"id": 1, "name": "Alice", "role": "Engineer"} in data
    assert {"id": 2, "name": "Bob", "role": "Manager"} in data
