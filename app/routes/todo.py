from fastapi import APIRouter
from app.models.todo import CreateTodo

router = APIRouter(
    prefix="/todo"
)

@router.get('/')
def index():
    return "todo router"

@router.post('/')
def post_todo(item: CreateTodo):
    return {"My item is": item}