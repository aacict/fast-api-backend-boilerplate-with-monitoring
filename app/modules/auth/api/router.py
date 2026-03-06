from fastapi import APIRouter
from .schemas import RegisterRequest
from ..domain.services import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register_user(payload: RegisterRequest):
    service = AuthService()
    return service.register_user(payload)