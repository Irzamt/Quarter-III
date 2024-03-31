from fastapi import FastAPI
import uvicorn

app = FastAPI()

students = [{
    "userName": "Ali",
    "rollNo": 302
},
{
    "userName": "Naveed",
    "rollNo": 456
},
]



@app.get("/students")
def getStudents():
    return students

@app.get("/addStudent")
def addStudent(userName:str, rollNo: int):
    global students
    students.append({"userName":userName, "rollNo":rollNo})
    return students


@app.get("/")
def helloworld():
    return {"hello": "world"}

@app.get("/gettodos/{userName}/{rollNo}") # Path variable Method
def getTodos(userName:str, rollNo:int):
    print("Get todos called", userName, rollNo)
    return userName + rollNo


@app.post("/gettodos") # route 
def getTodosPost():
    print("Get post method todos called")
    return "post gettodos called" 

@app.get("/getSingleTodo") # Query param Method
def getSingleTodo(userName:str, rollNo:int):
    print("Get todo called", userName, rollNo)
    return "getSingleTodo called"

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo Called"

def start():
   uvicorn.run ("todos.main:app", host="127.0.0.1", port=8080, reload=True) # 127.0.0.1 is Local Host IP

