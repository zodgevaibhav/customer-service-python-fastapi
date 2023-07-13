from fastapi import APIRouter
from api.model import User

router = APIRouter()

@router.get("/users")
async def get_users():
    user = User(id=1, name="John Doe", email="john@example.com")
    return user

@router.post("/users")
async def post_users():
    pass
