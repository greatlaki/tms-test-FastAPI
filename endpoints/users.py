from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User, UserIn
from repositories.users import UserRepository
from endpoints.depends import get_user_repository, get_current_user

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


@router.put("/", response_model=User)
async def update_user(
        id: int,
        user: UserIn,
        users: UserRepository = Depends(get_user_repository),
        current_user: User = Depends(get_current_user)):
    """ It updates a user"""
    old_user = await users.get_by_id(id=id)
    if old_user is None or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await users.update(id=id, u=user)
