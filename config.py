from pydantic import BaseSettings



class Settings(BaseSettings):
    database_name:str
    database_port:str
    database_host:str
    database_password:str
    database_username:str
    algorithm:str
    expired_time:int
    secret_key:str


    class Config:
        env_prefix="DATABASE_"

config_dict={
    "database_name":"robot_fastapi",
    "database_port":"5432",
    "database_host":"localhost",
    "database_password":"98654449",
    "database_username":"nedu",
    "algorithm":"HS256",
    "expired_time":30,
    "secret_key":"klhabvsishjsnksninsubhsvcuosudydhbbxcbsgvsusvsyskjsiak"

}

settings = Settings.parse_obj(config_dict)

