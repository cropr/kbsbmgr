from pydantic import BaseModel


class Person(BaseModel):
    user: str
    email: str
