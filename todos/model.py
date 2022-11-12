from pydantic import BaseModel
from fastapi import Form
from typing import List, Optional

class Todo(BaseModel):
    id: Optional[int]
    item: str
    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)
    class config:
        Schema_extra = {
            "Example": {
                "id": 1,
                "item": "Example schema!"
            }
        }
class TodoItem(BaseModel):
    item: str
    class config:
        Schema_extra = {
            "Example": {
                "item": "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "items": "Example schema 1!"
                    }
                ]
            }
        }