from sqlalchemy import Column, DateTime, Integer, String, func
from app import db


class Application(db.Model):
    __tablename__ = 'application'
    id = Column(Integer, primary_key=True)
    state = Column(String(64), index=True)
    term_start = Column(String(120))
    term_end = Column(String(120))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
