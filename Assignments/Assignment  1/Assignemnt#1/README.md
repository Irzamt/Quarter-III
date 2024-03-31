1. poetry new Assignment#1 --name todos
2. Created main.py file in todos
3. poetry add fastapi
4. poetry add sqlmodel
5. poetry add  "uvicorn[standard]" 
6.  [tool.poetry.scripts]  # added this text in pyproject.toml file
    dev= "todos.main:start"
7. 