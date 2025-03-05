from models.User import User
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/mydatabase")
db_client = AsyncIOMotorClient(MONGO_URI)
db = db_client.mydatabase
users_collection = db.users

class UserRepository:
    @staticmethod
    async def get_all_users():
        users = await users_collection.find().to_list(None)
        return [User(**user, id=str(user["_id"])) for user in users]  # แปลงเป็น Pydantic model

    @staticmethod
    async def create_user(user_data: User):
        user_dict = user_data.model_dump(exclude={"id"})  # แปลงเป็น dict (ยกเว้น id)
        result = await users_collection.insert_one(user_dict)
        return User(id=str(result.inserted_id), **user_dict)  # คืนค่าเป็น User model

    @staticmethod
    async def get_user_by_id(user_id: str):
        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        return User(**user, id=str(user["_id"])) if user else None

    @staticmethod
    async def update_user(user_id: str, user_data: User):
        user_dict = user_data.model_dump(exclude={"id"})
        updated_user = await users_collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": user_dict},
            return_document=True
        )
        return User(**updated_user, id=str(updated_user["_id"])) if updated_user else None

    @staticmethod
    async def delete_user(user_id: str):
        deleted_user = await users_collection.find_one_and_delete({"_id": ObjectId(user_id)})
        return User(**deleted_user, id=str(deleted_user["_id"])) if deleted_user else None
