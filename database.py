from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the database connection
engine = create_engine("postgresql://nedu:98654449@localhost:5432/robot_fastapi")
Base = declarative_base()

# Define a model for the users table
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session maker
Session= sessionmaker(autocommit=False, autoflush=False,bind=engine)
# Session = sessionmaker(bind=engine)

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close
