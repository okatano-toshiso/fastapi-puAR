from .models import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class LineReserveBase(BaseModel):
    token: str
    reservation_id: int
    reservation_date: date
    check_in: date
    check_out: date
    line_id: str
    status: str
    count_of_person: int
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

