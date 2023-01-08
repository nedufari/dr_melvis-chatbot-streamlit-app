import datetime
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import database,schemas,utils,auth
from database import User,Session,engine


app = FastAPI()
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
database.Base.metadata.create_all(bind=engine)


@app.post("/signup")
def signup(instance:schemas.Signup, db:Session=Depends(database.get_db)):
    password =utils.hash_password(instance.password)
    instance.password=password
    data= database.User(**instance.dict())
    print(data)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


