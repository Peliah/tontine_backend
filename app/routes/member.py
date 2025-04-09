from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(
    prefix="/member",
    tags=["member"],
    dependencies=[Depends(OAuth2PasswordBearer(tokenUrl="auth/login"))]
)

@router.get("/profile")
async def get_profile():
    return {"message": "Member profile"}