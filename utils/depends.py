from repositories.User import UserRepository
from services.Auth import AuthService
from services.User import UserService

user_repository = UserRepository()
user_service = UserService(user_repository)

auth_service = AuthService(user_repository)

async def get_user_service():
    return user_service

async def get_auth_service():
    return auth_service