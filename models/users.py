from pydantic import BaseModel

class User(BaseModel):
    RUT: str
    name: str
    loans: list
