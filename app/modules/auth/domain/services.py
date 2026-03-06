from .repositories import UserRepository
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
    
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
    
    def register_user(self, payload):
        user = self.repo.find_by_email(payload.email)

        if user:
            raise Exception("Email already registered")
        
        
        return self.repo.create_user(
            payload.email,
            self.hash_password(payload.password),
            payload.full_name
        )