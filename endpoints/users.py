from typing import List
from fastapi import APIRouter, Depends
from models.user import User, UserIn
from repositories.users import UserRepository
from endpoints.depends import get_user_repository

router = APIRouter()


@router.get("/", response_model=List[User])
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
    return await users.get_all(limit=limit, skip=0)


@router.post("/", response_model=User)
async def create(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository)):
    """ It creates a user"""
    return await users.create(u=user)
