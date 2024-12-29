from fastapi.testclient import TestClient
from main import app, persons

client = TestClient(app)

def setup_function():
    """Clear the persons dictionary before each test"""
    persons.clear()

def test_create_person_success():
    """Test successful person creation"""
    person_data = {
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com"
    }
    response = client.post("/persons/", json=person_data)
    
    assert response.status_code == 200
    created_person = response.json()
    assert created_person["name"] == person_data["name"]
    assert created_person["age"] == person_data["age"]
    assert created_person["email"] == person_data["email"]
    assert "id" in created_person
    assert len(persons) == 1

def test_create_person_invalid_data():
    """Test person creation with invalid data"""
    # Missing required fields
    person_data = {
        "name": "John Doe"
    }
    response = client.post("/persons/", json=person_data)
    assert response.status_code == 422
    
    # Invalid age type
    person_data = {
        "name": "John Doe",
        "age": "thirty",
        "email": "john@example.com"
    }
    response = client.post("/persons/", json=person_data)
    assert response.status_code == 422
