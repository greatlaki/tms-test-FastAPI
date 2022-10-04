from db.users import users
from base import BaseRepository


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0):
        return

    async def get_by_id(self, id: int):
        return

    async def create(self):
        return

    async def update(self):
        return

    async def get_by_email(self, email: str):
        return
