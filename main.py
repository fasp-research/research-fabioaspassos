from fastapi import FastAPI
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

@app.post("/persons/", response_model=Person)
async def create_person(person: PersonCreate):
    return None

@app.get("/persons/", response_model=List[Person])
async def list_persons():
    return None

@app.get("/persons/{person_id}", response_model=Person)
async def get_person(person_id: int):
    return None

@app.put("/persons/{person_id}", response_model=Person)
async def update_person(person_id: int, person: PersonCreate):
    return None

@app.delete("/persons/{person_id}")
async def delete_person(person_id: int):
    return None