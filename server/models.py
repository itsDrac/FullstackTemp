from sqlmodel import SQLModel, Field
from typing import Optional


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    realName: str | None = None
    description: str

