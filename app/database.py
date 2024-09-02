from .models import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class LineReserveBase(BaseModel):
    token: str
    version_number: Optional[int] = None
    reservation_id: int
    reservation_date: date
    check_in: date
    check_out: date
    line_id: str
    name: str
    phone_number: str
    status: str
    seq: Optional[int] = None
    count_of_person: int
    hotel_code: Optional[int] = None
    room_number: Optional[int] = None
    room_type: str
    option_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime


class LineUserBase(BaseModel):
    token: str
    line_id: str
    name: str
    name_kana: Optional[str] = None
    phone_number: str
    age: Optional[int] = None
    adult: bool = True
    created_at: datetime
    updated_at: datetime
