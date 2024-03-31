from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def helloworld():
    return "Hello World!dgdfgdfgdfg"

@app.get("/gettodos") # route
def getTodos():
    print("Get todos called")
    return "gettodos called" 


@app.post("/gettodos") # route
def getTodosPost():
    print("Get post method todos called")
    return "post gettodos called" 

@app.get("/getSingleTodo")
def getSingleTodo():
    print("Get todo called")
    return "getSingleTodo called"

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo Called"

def start():
   uvicorn.run ("todos.main:app", host="127.0.0.1", port=8080, reload=True) # 127.0.0.1 is Local Host IP