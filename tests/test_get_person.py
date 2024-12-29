from fastapi.testclient import TestClient
from main import app, persons

client = TestClient(app)

def setup_function():
    """Clear and populate the persons dictionary before each test"""
    persons.clear()
    # Add test data
    test_data = [
        {"name": "Alice Smith", "age": 25, "email": "alice@example.com"},
        {"name": "Bob Johnson", "age": 35, "email": "bob@example.com"}
    ]
    for person_data in test_data:
        response = client.post("/persons/", json=person_data)
        assert response.status_code == 200

def test_get_all_persons():
    """Test getting all persons"""
    response = client.get("/persons/")
    assert response.status_code == 200
    persons_list = response.json()
    
    assert len(persons_list) == 2
    assert any(p["name"] == "Alice Smith" for p in persons_list)
    assert any(p["name"] == "Bob Johnson" for p in persons_list)

def test_get_person_by_id():
    """Test getting a person by ID"""
    # Get the first person's ID
    response = client.get("/persons/")
    persons_list = response.json()
    first_person_id = persons_list[0]["id"]
    
    # Get person by ID
    response = client.get(f"/persons/{first_person_id}")
    assert response.status_code == 200
    person = response.json()
    assert person["id"] == first_person_id
    assert "name" in person
    assert "age" in person
    assert "email" in person

def test_get_person_not_found():
    """Test getting a non-existent person"""
    response = client.get("/persons/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Person not found"
