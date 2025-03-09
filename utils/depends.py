from repositories.User import UserRepository
from services.User import UserService

user_repository = UserRepository()
user_service = UserService(user_repository)

async def get_user_service():
    return user_service