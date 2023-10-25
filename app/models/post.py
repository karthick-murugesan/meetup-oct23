from pydantic import BaseModel

class UserPost(BaseModel):
    name:str
    gender:str
    