from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from typing import List, Optional
from datetime import date, datetime
from .models import SessionLocal, LineReserve, LineUser

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
app = FastAPI()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
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
class RequestData(BaseModel):
    line_reserves: List[LineReserveBase]
    line_users: List[LineUserBase]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_test():
    return {"Hello, Worlds"}

@app.get("/test/")
async def read_test():
    return {"success": True}

@app.post("/reserve/")
def create_reservation(request_data: RequestData, db: Session = Depends(get_db)):

    for line_reserve in request_data.line_reserves:

        if line_reserve.token != ACCESS_TOKEN:
            raise HTTPException(status_code=401, detail="Invalid Token")

        db_line_reserve = LineReserve(
            reservation_id=line_reserve.reservation_id,
            reservation_date=line_reserve.reservation_date,
            line_id=line_reserve.line_id,
            check_in=line_reserve.check_in,
            check_out=line_reserve.check_out,
            status=line_reserve.status,
            count_of_person=line_reserve.count_of_person,
            room_type=line_reserve.room_type,
            option_id=line_reserve.option_id,
            created_at=line_reserve.created_at,
            updated_at=line_reserve.updated_at
        )

        db.add(db_line_reserve)
        db.commit()
        db.refresh(db_line_reserve)

    for line_user in request_data.line_users:

        if line_user.token != ACCESS_TOKEN:
            raise HTTPException(status_code=401, detail="Invalid Token")

        db_line_user = LineUser(
            line_id=line_user.line_id,
            name=line_user.name,
            name_kana=line_user.name_kana,
            phone_number=line_user.phone_number,
            age=line_user.age,
            adult=line_user.adult,
            created_at=line_user.created_at,
            updated_at=line_user.updated_at
        )

        db.add(db_line_user)
        db.commit()
        db.refresh(db_line_user)

    return {"message": "Reservations processed successfully"}

