from pydantic import BaseModel,Field


class User(BaseModel):
    email:str = Field(default="barcecm@hotmail.com")
    password: str 