""" User """

from app.dto.user_dto import UserDTO
from app.service.user_service import UserService
from fastapi import APIRouter

user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get("/{user}", response_model=UserDTO)
async def get_user_by_pseudo(user: str) -> UserDTO:
    """
    Retrieve a user by their pseudo.
    """
    user_wanted = UserService().get_by_pseudo(pseudo=user)
    return UserDTO(
        user_id=user_wanted.id,
        pseudo=user_wanted.pseudo,
        pref=user_wanted.pref,
    )


@user_router.delete("/delete")
async def delete(pseudo: str) -> bool:
    """
    Delete a user by their pseudo.
    """
    return UserService().delete_where_pseudo(pseudo=pseudo)
