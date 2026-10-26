from fastapi import APIRouter

users_router = APIRouter(prefix="/users")


@users_router.get("/")
def get_users():
    return
