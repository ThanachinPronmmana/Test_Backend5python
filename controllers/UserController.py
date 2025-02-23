from fastapi import HTTPException
from services.UserService import UserService

class UserController:
    @staticmethod
    async def get_all_users():
        return await UserService.get_all_users()

    @staticmethod
    async def create_user(user_data: dict):
        return await UserService.create_user(user_data)

    @staticmethod
    async def get_user_by_id(id: str):
        user = await UserService.get_user_by_id(id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    async def update_user(id: str, user_data: dict):
        updated_user = await UserService.update_user(id, user_data)
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return updated_user

    @staticmethod
    async def delete_user(id: str):
        deleted_user = await UserService.delete_user(id)
        if not deleted_user:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}