from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel


app = FastAPI(
    title="Learning Management System", 
    description="A great place where students meet teachers and teachers orient students",
    version="0.0.1",
    contact={
        "name": "Vítor Carrara",
        "url": "https://www.github.com/VitorCarraraMarques",
    }
    
)

users = [] 

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model=List[User])
async def get_user():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return users

@app.post("/users/{user_id}")
async def get_user_by_id(user_id: int = Path(..., description="The ID of the desired user")):
    return users[user_id]