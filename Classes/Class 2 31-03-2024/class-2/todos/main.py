from fastapi import FastAPI, Path
import uvicorn
from typing import Optional, Union, Annotated
from pydantic import BaseModel

app = FastAPI()

class Car(BaseModel):
   id: int | str
   color:str = "any default title value"
   details: Optional[str] = "any default"

class Todo(BaseModel):
   id:int
   titile:str = "any default title value"
   description:str 

userName: Annotated[str, 23, Path(ge=10)] = "IrzamTahir"
age:int = 30

listOfStudents:list[str] = ["First", "Second", "Third"]

car:Todo = {
   "id": 2025,
   "title": "red",
   "description": "any descprtion"
}

def getUserFullName(firstName:str | None = None, lastName:str = None):
   return firstName + " " + lastName

def start():
   uvicorn.run ("todos.main:app", host="127.0.0.1", port=8080, reload=True)