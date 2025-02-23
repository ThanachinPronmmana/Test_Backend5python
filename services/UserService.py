from repositories.UserRepository import UserRepository

class UserService:
    @staticmethod
    async def get_all_users():
        return await UserRepository.get_all_users()

    @staticmethod
    async def create_user(user_data):
        return await UserRepository.create_user(user_data)

    @staticmethod
    async def get_user_by_id(user_id):
        return await UserRepository.get_user_by_id(user_id)

    @staticmethod
    async def update_user(user_id, user_data):
        return await UserRepository.update_user(user_id, user_data)

    @staticmethod
    async def delete_user(user_id):
        return await UserRepository.delete_user(user_id)
