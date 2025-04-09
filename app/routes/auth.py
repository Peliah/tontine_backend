from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.utils.security import create_access_token, authenticate_user
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.database import SessionLocal
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginRequest(BaseModel):
    username: str
    password: str

# Mock database (replace with real DB calls)
db = SessionLocal()

@router.post("/register")
async def register(user: UserCreate):
    # Add user to database
    db_user = User(email=user.email, hashed_password="hashed_password", is_admin=False)
    db.add(db_user)
    db.commit()
    return {"message": "User created successfully"}

@router.post("/login")
async def login(credentials: LoginRequest):
    if credentials.username != "admin" or credentials.password != "secret":
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    return {"message": "Logged in!"}