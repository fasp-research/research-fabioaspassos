from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict

app = FastAPI(title="Person API", version="0.1.0")

# Person request model
class PersonCreate(BaseModel):
    name: str
    age: int
    email: str

# Person response model
class Person(PersonCreate):
    id: int

# In-memory storage
persons: Dict[int, Person] = {}
current_id = 1

@app.get("/")
async def index():
    return "Hello, this is the Person API."

persons: Dict[int, Person] = {}
current_id = 1

@app.post("/persons/", response_model=Person)
async def create_person(person: PersonCreate):
    global current_id
    new_person = Person(
        id=current_id,
        name=person.name,
        age=person.age,
        email=person.email
    )
    persons[current_id] = new_person
    current_id += 1
    return new_person

@app.get("/persons/", response_model=List[Person])
async def list_persons():
    return list(persons.values())

@app.get("/persons/{person_id}", response_model=Person)
async def get_person(person_id: int):
    if person_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")
    return persons[person_id]

@app.put("/persons/{person_id}", response_model=Person)
async def update_person(person_id: int, person: PersonCreate):
    return None

@app.delete("/persons/{person_id}")
async def delete_person(person_id: int):
    if person_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")
    del persons[person_id]
    return {"message": "Person deleted successfully"}