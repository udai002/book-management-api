from pydantic import BaseModel

class post(BaseModel):
    user_id:str
    post:str
    desc:str

    