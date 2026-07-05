from sqlalchemy import Column,Table,Integer,String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base=declarative_base()
class Note(Base):
    __tablename__="notes"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(100))
    content=Column(String)

DATABASE_URL="sqlite:///./notes.db"
engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

def init_db():
    Base.metadata.create_all(bind=engine)