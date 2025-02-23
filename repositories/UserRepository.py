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
        return await users_collection.find().to_list(None)

    @staticmethod
    async def create_user(user_data):
        result = await users_collection.insert_one(user_data)
        return {"id": str(result.inserted_id), **user_data}

    @staticmethod
    async def get_user_by_id(user_id):
        return await users_collection.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    async def update_user(user_id, user_data):
        return await users_collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": user_data},
            return_document=True
        )

    @staticmethod
    async def delete_user(user_id):
        return await users_collection.find_one_and_delete({"_id": ObjectId(user_id)})