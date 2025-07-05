from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_employees_route(monkeypatch):
    def mock_connect():
        class FakeConn:
            def cursor(self):
                class FakeCursor:
                    def execute(self, query):
                        pass
                    def fetchall(self):
                        return [(1, "Alice", "Engineer"), (2, "Bob", "Manager")]
                    def close(self):
                        pass
                return FakeCursor()
            def close(self):
                pass
        return FakeConn()

    monkeypatch.setattr("app.main.connect", mock_connect)

    response = client.get("/employees")
    assert response.status_code == 200
    data = response.json()
    assert data == [
        {"id": 1, "name": "Alice", "role": "Engineer"},
        {"id": 2, "name": "Bob", "role": "Manager"},
    ]
