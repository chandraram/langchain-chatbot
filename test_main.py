from fastapi.testclient import TestClient
from main import app  # Adjust the import path if necessary

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI example!"}

def test_greet_user():
    response = client.post("/greet", json={"name": "Alice"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello user, Alice!"}
