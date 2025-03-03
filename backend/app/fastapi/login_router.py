"""
Login and user creation routes for authentication.

"""

from app.config.security import hash_password
from app.dto.login_dto import LoginUserDTO
from app.dto.user_dto import UserDTO
from app.service.user_service import UserService
from fastapi import APIRouter, Depends

login_router = APIRouter(prefix="/login", tags=["Login"])


@login_router.post("/create")
async def create_user(userlogin: LoginUserDTO = Depends()):
    """
    Create a new user by providing a username and password.
    """
    user_id = UserService().create(
        pseudo=userlogin.pseudo,
        pwd=hash_password(
            password=userlogin.pwd.get_secret_value(), sel=userlogin.pseudo
        ),
    )
    return user_id


@login_router.post("/user")
async def login_user(userlogin: LoginUserDTO = Depends()):
    """
    Log in a user by verifying the username and password.
    """
    user = UserService().login(
        pseudo=userlogin.pseudo,
        pwd=hash_password(
            password=userlogin.pwd.get_secret_value(), sel=userlogin.pseudo
        ),
    )
    user_id = UserService().get_by_pseudo(pseudo=userlogin.pseudo).id
    return UserDTO(user_id=user_id, pseudo=user.pseudo, pref=user.pref)
