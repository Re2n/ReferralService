from repositories.Referral import ReferralRepository
from repositories.ReferralCode import ReferralCodeRepository
from repositories.User import UserRepository
from services.Auth import AuthService
from services.ReferralCode import ReferralCodeService
from services.User import UserService

user_repository = UserRepository()
referral_code_repository = ReferralCodeRepository()
referral_repository = ReferralRepository()
user_service = UserService(
    user_repository,
    referral_code_repository,
    referral_repository,
)
referral_code_service = ReferralCodeService(referral_code_repository)

auth_service = AuthService(user_repository)


async def get_user_service():
    return user_service


async def get_auth_service():
    return auth_service


async def get_referral_code_service():
    return referral_code_service
