from app.dto.login_dto import LoginUserDTO
from app.dto.user_dto import UserDTO
from app.service.user_service import UserService
from fastapi import APIRouter, Depends

login_router = APIRouter(prefix="/login", tags=["Login"])


@login_router.post("/create")
async def create_user(userlogin: LoginUserDTO = Depends()):
    user_id = UserService().create(
        pseudo=userlogin.pseudo, pwd=userlogin.pwd.get_secret_value()
    )
    return user_id


@login_router.post("/user")
async def login_user(userlogin: LoginUserDTO = Depends()):
    user = UserService().login(
        pseudo=userlogin.pseudo, pwd=userlogin.pwd.get_secret_value()
    )
    user_id = UserService().get_by_pseudo(pseudo=userlogin.pseudo).id
    return UserDTO(user_id=user_id, pseudo=user.pseudo, pref=user.pref)
