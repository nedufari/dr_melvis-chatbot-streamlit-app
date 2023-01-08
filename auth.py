from fastapi import APIRouter,Response,status,Depends,HTTPException,Body
from database import get_db
from sqlalchemy.orm import Session
import schemas,utils
import oauth2
from fastapi.security import OAuth2PasswordRequestForm
import database

router=APIRouter(tags=["authentication"])

@router.post("/login",response_model=schemas.AccessToken) #user
def Login1(username:str=Body(...),password:str=Body(...), db:Session=Depends(get_db)):
    owner= db.query(database.User).filter(database.User.email==username).first()

    if not owner :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")
    if utils.verify_passowrd(password, owner.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")

    access_token= oauth2.create_token(data={"user_id":owner.id})   
    return {"access_token":access_token, "token_type":"bearer"}






 #"$2b$12$03.YoohrHav.AqvSsZsiYe/P25EnVZly9xXerscDFe2TKLQtMvIRm"