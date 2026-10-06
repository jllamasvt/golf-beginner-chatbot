from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health(): assert client.get('/api/v1/health').status_code==200
def test_ready(): assert client.get('/api/v1/ready').status_code==200
