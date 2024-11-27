from pydantic import BaseModel

class Books(BaseModel):
    id:str
    title:str 
    name:str
    author:str 
