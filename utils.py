from passlib.context import CryptContext
import uuid

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_passowrd(provided_passowrd, db_password):
    pwd_context.verify(provided_passowrd,db_password)

def generate_login_token():
    return str(uuid.uuid4())