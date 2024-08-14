from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from typing import List
from datetime import date
from .database import SessionLocal, Reservation, Line_User as LineUserModel
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
app = FastAPI()

LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
# print(LINE_ACCESS_TOKEN)

# models.Base.metadata.create_all(bind=engine)
class Reserve(BaseModel):
    reservation_id: int
    reservation_date: date
    check_in: date
    check_out: date
    line_id: str
    status: str
    count_of_person: int
    room_type: str
    option_id: int
    created_at: date
    updated_at: date

class LineUserBase(BaseModel):
    line_id: str
    name: str
    name_kana: str
    phone_number: str
    age: int
    adult: bool
    created_at: date
    updated_at: date

class RequestData(BaseModel):
    reserves: List[Reserve]
    line_users: List[LineUserBase]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/reserve")
def create_reservation(request_data: RequestData, db: Session = Depends(get_db)):
    for reserve in request_data.reserves:

        db_reservation = Reservation(
            reservation_id=reserve.reservation_id,
            reservation_date=reserve.reservation_date,
            line_id=reserve.line_id,
            check_in=reserve.check_in,
            check_out=reserve.check_out,
            status=reserve.status,
            count_of_person=reserve.count_of_person,
            room_type=reserve.room_type,
            option_id=reserve.option_id,
            created_at=reserve.created_at,
            updated_at=reserve.updated_at
        )

        db.add(db_reservation)
        db.commit()
        db.refresh(db_reservation)

    for line_user in request_data.line_users:
        db_line_user = LineUserModel(
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

