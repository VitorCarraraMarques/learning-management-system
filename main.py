from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel

from api import users, sections, courses 


app = FastAPI(
    title="Learning Management System", 
    description="A great place where students meet teachers and teachers orient students",
    version="0.0.1",
    contact={
        "name": "Vítor Carrara",
        "url": "https://www.github.com/VitorCarraraMarques",
    }
    
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)