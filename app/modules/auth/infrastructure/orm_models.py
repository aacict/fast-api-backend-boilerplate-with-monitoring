from sqlalchemy import Column, Integer, String
from app.shared.database.base import Base

class UserORM(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    full_name = Column(String)