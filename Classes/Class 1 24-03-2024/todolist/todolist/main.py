from fastapi import FastAPI

app = FastAPI()

@app.get("/get_todos")
def get_todos():
    print ("get todos called")
    return ("message: Test todo list")*
# 

@app.post("/get_todos")
def get_todos():
    print("get Post todos called")
    return ("message: Test Post todo List")

get_todos()

@app.get("/getSingleTodo")
def getSingleTodo():
    print("Get todo Called")
    return "getSingleTodo called"