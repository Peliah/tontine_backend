from fastapi import FastAPI
from app.routes import auth, admin, member
from app.database import engine, Base

Base.metadata.create_all(bind=engine)  # Create tables

app = FastAPI()

app.include_router(auth.router)
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(member.router, prefix="/member", tags=["member"])