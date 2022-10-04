import datetime
from typing import List, Optional
from db.users import users
from models.user import User, UserIn
from core.security import hash_password
from base import BaseRepository


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        """
        The function returns a list of users
        limit: maximum number of users
        skip: how many users to skip for pagination (a way to return objects page by page)
        """
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[User]:
        """
        The function return a specific user by 'id'
        id: user's id
        """
        query = users.select().where(users.c.id == id).first()
        user = await self.database.fetch_one(query=query)
        if user in None:
            return None
        return User.parse_obj(user)

    async def create(self, u: UserIn) -> User:
        """
        The function creates a user
        """
        user = User(
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop('id', None)
        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update(self, id: int, u: UserIn) -> User:
        """
        The function updates user's data
        """
        user = User(
            id=id,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop('id', None)
        values.pop('created_at', None)
        query = users.update().where(users.c.id == id).values(**values)
        await self.database.execute(query)
        return user

    async def get_by_email(self, email: str) -> User:
        """
        The function returns a user by email
        """
        query = users.select().where(users.c.email == email).first()
        user = await self.database.fetch_one(query=query)
        if user in None:
            return None
        return User.parse_obj(user)
