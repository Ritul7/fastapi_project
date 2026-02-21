from pydantic import BaseModel, Field
from typing import Optional

class CreateTodo(BaseModel):
    content: str = Field(..., max_length=500, min_length=5)         # ye req puri nhi hui agr, to uske liye error acche se generate ho, for that apn ne main.py me exception handling ki h
    is_completed: bool = False
