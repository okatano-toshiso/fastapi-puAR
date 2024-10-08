from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import and_
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from typing import List
from .models import LineReserve, LineUser
from .database import get_db, LineReserveBase, LineUserBase


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
app = FastAPI()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

class CheckReserveData(BaseModel):
    token: str
    line_id: str
    # reserve_id: int
    name: str
    phone_number: str


class LatestReserveData(BaseModel):
    token: str


class RequestData(BaseModel):
    line_reserves: List[LineReserveBase]
    line_users: List[LineUserBase]


@app.get("/")
async def read_index_test():
    return {"Hello, Worlds"}


@app.get("/test/")
async def read_test():
    return {"success": True}


@app.post("/reserve/latest/id/")
def create_reservation(request_data: LatestReserveData, db: Session = Depends(get_db)):

    if request_data.token != ACCESS_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid Token")

    latest_reserve = db.query(LineReserve).order_by(LineReserve.reservation_id.desc()).first()

    if latest_reserve:
        return {"latest_reserve_id": latest_reserve.reservation_id}
    else:
        return {"latest_reserve_id": 0}


@app.post("/reserve/check/")
def create_reservation(request_data: CheckReserveData, db: Session = Depends(get_db)):

    if request_data.token != ACCESS_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid Token")

    reserve_datas = db.query(LineReserve, LineUser)\
        .join(LineUser, LineReserve.line_id == LineUser.line_id)\
        .filter(and_(
            # LineReserve.reservation_id == request_data.reserve_id,
            LineReserve.line_id == request_data.line_id,
            LineReserve.name == request_data.name,
            LineReserve.phone_number == request_data.phone_number,
            LineUser.line_id == request_data.line_id,
            LineUser.name == request_data.name,
            LineUser.phone_number == request_data.phone_number
        )).order_by(LineReserve.reservation_date.desc()).limit(10).all()

    if reserve_datas:
        reserves_list = []
        for line_reserve, line_user in reserve_datas:
            reserve_data = {
                "reservation_id": line_reserve.reservation_id,
                "reservation_date": line_reserve.reservation_date,
                "check_in": line_reserve.check_in,
                "check_out": line_reserve.check_out,
                "status": line_reserve.status,
                "count_of_person": line_reserve.count_of_person,
                "hotel_code": line_reserve.hotel_code,
                "room_number": line_reserve.room_number,
                "room_type": line_reserve.room_type,
                "name": line_user.name,
                "name_kana": line_user.name_kana,
                "phone_number": line_user.phone_number,
                "age": line_user.age,
                "adult": line_user.adult
            }
            reserves_list.append(reserve_data)
        return {"reservations": reserves_list}
    else:
        raise HTTPException(status_code=404, detail="Reservation not found")


@app.post("/reserve/")
def create_reservation(request_data: RequestData, db: Session = Depends(get_db)):

    print(request_data)

    for line_reserve in request_data.line_reserves:

        if line_reserve.token != ACCESS_TOKEN:
            raise HTTPException(status_code=401, detail="Invalid Token")

        db_line_reserve = LineReserve(
            version_number=line_reserve.version_number,
            reservation_id=line_reserve.reservation_id,
            reservation_date=line_reserve.reservation_date,
            line_id=line_reserve.line_id,
            name=line_reserve.name,
            phone_number=line_reserve.phone_number,
            check_in=line_reserve.check_in,
            check_out=line_reserve.check_out,
            status=line_reserve.status,
            seq=line_reserve.seq,
            count_of_person=line_reserve.count_of_person,
            hotel_code=line_reserve.hotel_code,
            room_number=line_reserve.room_number,
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

        existing_user = db.query(LineUser).filter_by(
            line_id=line_user.line_id,
            name=line_user.name,
            phone_number=line_user.phone_number
        ).first()

        if not existing_user:
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
