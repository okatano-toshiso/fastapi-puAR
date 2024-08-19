from sqlalchemy.orm import Session
from .models import SessionLocal, Base, engine, Reservation, Line_User


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
