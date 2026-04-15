import csv
import uuid
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
CSV_FILE = "todos.csv"

# Ensure CSV exists and has headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "description", "priority", "state"])

class Todo(BaseModel):
    title: str
    description: str
    priority: int
    state: str

class TodoID(BaseModel):
    todo_id: str

@app.get("/webapi")
async def root():
    return {"message": "hello from the python course"}

@app.post("/add_todo")
#uvicorn fa:
# json_dal_client_http = leggi_dal_curl()
# chiamata = add_todo(json_dal_client_http)
async def add_todo(todo: Todo):
    #todo_id = str(uuid.uuid4())
    
    print(type(todo))
    print(todo.title)
    print(type(todo.title))
    print(todo.priority)
    print(type(todo.priority))
    print(todo)
    #print(todo)
    #with open(CSV_FILE, mode='a', newline='') as f:
    #    writer = csv.writer(f)
    #    writer.writerow([todo_id, todo.title, todo.description, todo.priority, todo.state])
    
    #return {"todo_id": todo_id}
    return {"todo ricevuto correttamente"}

@app.get("/read_todo")
async def read_todo(payload: TodoID):
    with open(CSV_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"] == payload.todo_id:
                return row
                
    raise HTTPException(status_code=404, detail="Todo not found")