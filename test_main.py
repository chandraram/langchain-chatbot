from fastapi.testclient import TestClient
from main import app  # Adjust the import path if necessary
import httpx

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI example!"}

def test_greet_user():
    response = client.post("/greet", json={"name": "Alice"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello user, Alice!"}


def test_predict_sales():
    new_data = {
        'Item_Fat_Content': 'Low Fat',
        'Item_Visibility': 0.016047,
        'Item_MRP': 249.8092,
        'Outlet_Establishment_Year': 1999,
        'Outlet_Size': 'Medium',
        'Outlet_Location_Type': 'Tier 1',
        'Outlet_Type': 'Supermarket Type1',
        'Item_Type': 'Fruits and Vegetables'
    }
    response = client.post("/predict_sales/", json=new_data)
    assert response.status_code == 200
    assert 'predicted_sales' in response.json()