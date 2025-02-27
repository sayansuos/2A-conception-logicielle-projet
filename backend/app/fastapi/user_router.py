from app.dto.user_dto import UserDTO
from app.service.build_service import BuildService
from app.service.champion_service import ChampionService
from app.service.item_service import ItemService
from app.service.user_service import UserService
from fastapi import APIRouter, Query

user_router = APIRouter(prefix="/user", tags=["User"])

# user


@user_router.get("/{pseudo}")
async def get_user_by_pseudo(pseudo: str) -> UserDTO:
    user = UserService().get_by_pseudo(pseudo=pseudo)
    return UserDTO(user_id=user.id, pseudo=user.pseudo, pref=user.pref)


@user_router.post("/addbuild")
async def add_build(
    champion_name: str,
    item1_name: str,
    item2_name: str,
    item3_name: str,
    item4_name: str,
    item5_name: str,
    pseudo: str = Query(..., description="Username"),
) -> bool:

    user = UserService().get_by_pseudo(pseudo)

    build_create = BuildService().create(
        champion=ChampionService().get_champ_by_name(champ_name=champion_name),
        item1=ItemService().get_item_by_name(item_name=item1_name),
        item2=ItemService().get_item_by_name(item_name=item2_name),
        item3=ItemService().get_item_by_name(item_name=item3_name),
        item4=ItemService().get_item_by_name(item_name=item4_name),
        item5=ItemService().get_item_by_name(item_name=item5_name),
    )

    build_user = UserService().add_build(user=user, build=build_create)

    return build_user


@user_router.delete("/delete")
async def delete(pseudo: str) -> bool:
    return UserService().delete_where_pseudo(pseudo=pseudo)
