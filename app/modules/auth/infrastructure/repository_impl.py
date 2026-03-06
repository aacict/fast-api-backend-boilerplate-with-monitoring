from ..domain.repositories import UserRepository
from .orm_models import UserORM

class SQLUserRepository(UserRepository):

    def __init__(self, db):
        self.db = db

    def find_by_email(self, email):
        return self.db.query(UserORM).filter_by(email=email).first()

    def create_user(self, email, hashed_password, full_name):
        user = UserORM(email=email, password_hash=hashed_password, full_name=full_name)
        self.db.add(user)
        self.db.commit()
        return user