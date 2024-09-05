from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

# GET ALL
@app.get("/tasks/")
async def home(req: Request, db: Session = Depends(get_db)):
	todos = db.query(models.Todo).all()
	return templates.TemplateResponse("todolist.html", { "request": req, "todo_list": todos })

# POST
@app.post("/tasks")
def add(req: Request, title: str = Form(...), description: str = Form(...), db: Session = Depends(get_db)):
	new_todo = models.Todo(title=title, description=description)
	db.add(new_todo)
	db.commit()
	url = app.url_path_for("home")
	return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

# PATCH
@app.get("/tasks/{task_id}")
def patch(req: Request, task_id: int, db: Session = Depends(get_db)):
	todo = db.query(models.Todo).filter(models.Todo.id == task_id).first()
	todo.completed = not todo.completed
	db.commit()
	url = app.url_path_for("home")
	return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

# DELETE
@app.get("/tasks/{task_id}")
def delete(req: Request, task_id: int, db: Session = Depends(get_db)):
	todo = db.query(models.Todo).filter(models.Todo.id == task_id).first()
	db.delete(todo)
	db.commit()
	url = app.url_path_for("home")
	return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

# GET BY ID
@app.get("/tasks/{task_id}")
def find(req: Request, task_id: int, db: Session = Depends(get_db)):
	todo = db.query(models.Todo).filter(models.Todo.id == task_id).first()
	db.find(todo)
	db.commit()
	url = app.url_path_for("home")
	return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

# PUT
@app.put("/tasks/{task_id}")
def put(req: Request, task_id: int, title: str = Form(...), description: str = Form(...), db: Session = Depends(get_db)):
  todo = db.query(models.Todo).filter(models.Todo.id == task_id).first()
  todo = models.Todo(title=title, description=description)
  todo.completed = not todo.completed
  db.update(todo)
  db.commit()
  url = app.url_path_for("home")
  return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)