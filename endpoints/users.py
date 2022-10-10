from fastapi import APIRouter, Depends
from repositories.users import UserRepository
from endpoints.depends import get_user_repository

router = APIRouter()


@router.get("/")
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 100):
    """
    The function returns a list of users
    the object 'depends' takes a function that do some work and returns dependence(our repository)
    limit: maximum number of users
    skip: how many users to skip for pagination
    """
    return {}
