from pydantic import BaseModel


class MgrRequest(BaseModel):
    user: str
    email: str
    branch: str
