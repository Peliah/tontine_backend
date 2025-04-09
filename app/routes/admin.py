from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User
from app.database import SessionLocal

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(OAuth2PasswordBearer(tokenUrl="auth/login"))]
)

db = SessionLocal()

@router.get("/users")
async def get_all_users():
    users = db.query(User).all()
    return users

@router.post("/create-tontine")
async def create_tontine():
    # Add your tontine creation logic here
    return {"message": "Tontine created"}