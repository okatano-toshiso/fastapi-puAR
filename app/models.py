from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
import os

DATABASE_URL = "mysql+pymysql://root:rJlmEKzHAcnoHEFnJGsBudDkTfOSWSRF@roundhouse.proxy.rlwy.net:10446/railway"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
class Reservation(Base):
    __tablename__ = "line_reserves"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    reservation_id = Column(Integer, unique=True, index=True)
    reservation_date = Column(Date)
    check_in = Column(Date)
    check_out = Column(Date)
    line_id = Column(String(255)) 
    status = Column(String)
    count_of_person = Column(Integer)
    room_type = Column(String)
    option_id = Column(Integer, nullable=True)
    created_at = Column(Date)
    updated_at = Column(Date)

class Line_User(Base):
    __tablename__ = "line_users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    line_id = Column(String(255), unique=True, index=True)
    name = Column(String(20))
    name_kana = Column(String(20), nullable=True)
    phone_number = Column(String(11))
    age = Column(Integer, nullable=True)
    adult = Column(Boolean, server_default=sa.text('TRUE'))
    created_at = Column(Date)
    updated_at = Column(Date)

