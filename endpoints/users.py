from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_users(limit: int = 100, skip: int = 100):
    """
    The function returns a list of users
    limit: maximum number of users
    skip: how many users to skip for pagination
    """
    return {}
