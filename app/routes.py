from flask import(
    Flask,
    request
)
from app.database import task


app = Flask(__name__)

@app.get("/")
@app.get("/index")
def get_all_tasks():
    out = {
        "task": task.scan(),
        "ok": True
    }
    return out

@app.get("/task/<int:pk>/")
def get_single_task(pk):
    out = {
        "task": task.select_by_id(pk),
        "ok": True
    }
    return out

@app.post("/task/<int:pk>/")
def update_task(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204

@app.delete("/task/<int:pk>/")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204

