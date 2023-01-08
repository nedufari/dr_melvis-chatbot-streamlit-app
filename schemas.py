from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class Signup(BaseModel):
    email:EmailStr
    password:str


class Login(BaseModel):
    email:EmailStr
    password:str 


##################################################################################### schema for the token authentication, the acess tokena nd the token type
class AccessToken(BaseModel):
    access_token:str
    token_type:str
    class Config:
        orm_mode=True

        

class TokenData(BaseModel):
    id: str=Optional[int]