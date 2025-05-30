from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_ml():
    response = client.post("/analyze/ml", json={"numbers": [1, 2, 3, 4, 5], "top_k": 2})
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "prediction" in response.json()["data"]
