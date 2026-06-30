from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Literal
from datetime import date

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3)
    description: Optional[str] = None
    status: Literal["pending", "in-progress", "done"]
    priority: Optional[Literal["low", "medium", "high"]] = None
    due_date: Optional[date] = None
    tags: Optional[List[str]] = None

    @field_validator("tags")
    def validate_tags(cls, v):
        if v is None:
            return v
        
        for tag in v:
            if not isinstance(tag, str):
                raise ValueError("Each tag must be a string")
            if (len(tag) < 2):
                raise ValueError("Each tag must be at least 2 characters long")
        return v


class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=3)
    description: Optional[str] = None
    status: Literal["pending", "in-progress", "done"]
    priority: Optional[Literal["low", "medium", "high"]] = None
    due_date: Optional[date] = None
    tags: Optional[List[str]] = None

    @field_validator("tags")
    def validate_tags(cls, v):
        if v is None:
            return v
        
        for tag in v:
            if not isinstance(tag, str):
                raise ValueError("Each tag must be a string")
            if (len(tag) < 2):
                raise ValueError("Each tag must be at least 2 characters long")
        return v