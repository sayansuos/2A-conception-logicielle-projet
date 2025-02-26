from typing import List, Optional

import app.config.charge_environnement as config
from app.dto.champion_dto import ChampionDTO
from app.dto.item_dto import ItemDTO
from app.dto.login_dto import LoginUserDTO
from app.dto.user_dto import UserDTO
from app.service.build_service import BuildService
from app.service.champion_service import ChampionService
from app.service.item_service import ItemService
from app.service.user_service import UserService
from fastapi import Depends, FastAPI, Path, Query

config.load_dotenv()


app = FastAPI()

# user


@app.get("/user/{pseudo}")
async def get_user_by_pseudo(pseudo: str) -> UserDTO:
    user = UserService().get_by_pseudo(pseudo=pseudo)
    return UserDTO(user_id=user.id, pseudo=user.pseudo, pref=user.pref)


@app.post("/user/addbuild")
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


@app.delete("/user/delete")
async def delete(pseudo: str) -> bool:
    return UserService().delete_where_pseudo(pseudo=pseudo)


# login


@app.post("/user/create")
async def create_user(userlogin: LoginUserDTO = Depends()):
    user_id = UserService().create(
        pseudo=userlogin.pseudo, pwd=userlogin.pwd.get_secret_value()
    )
    return user_id


@app.post("/user/login")
async def login_user(userlogin: LoginUserDTO = Depends()):
    user = UserService().login(
        pseudo=userlogin.pseudo, pwd=userlogin.pwd.get_secret_value()
    )
    user_id = UserService().get_by_pseudo(pseudo=userlogin.pseudo).id
    return UserDTO(user_id=user_id, pseudo=user.pseudo, pref=user.pref)


# build

# champion


@app.get("/total_champion")
async def get_total_champion() -> dict:
    return {"total": len(ChampionService().get_all_champs())}


@app.get("/champions", response_model=List[ChampionDTO])
async def get_all_champions() -> list[ChampionDTO]:
    return [
        ChampionDTO(
            name=champion.name,
            champ_id=champion.id,
            blurb=champion.blurb,
            tags=champion.tags,
            stats=champion.stats,
            info=champion.info,
            image=champion.image,
        )
        for champion in ChampionService().get_all_champs()
    ]


@app.get("/champion/id/{id}")
async def get_champion_by_id(id: int = Path(ge=1)) -> ChampionDTO:
    champion = ChampionService().get_champ_by_id(id)
    return ChampionDTO(
        name=champion.name,
        champ_id=champion.id,
        blurb=champion.blurb,
        tags=champion.tags,
        stats=champion.stats,
        info=champion.info,
        image=champion.image,
    )


@app.get("/champion/name/{name}")
async def get_champion_by_name(name: str) -> ChampionDTO:
    champion = ChampionService().get_champ_by_name(name)
    return ChampionDTO(
        name=champion.name,
        champ_id=champion.id,
        blurb=champion.blurb,
        tags=champion.tags,
        stats=champion.stats,
        info=champion.info,
        image=champion.image,
    )


@app.get("/champion/best")
async def get_best_champs(
    role: str = Query(..., description="role of the player"),
    teammates: Optional[List[str]] = Query([], description="Allies"),
    ennemies: Optional[List[str]] = Query([], description="Enemies"),
    bans: Optional[List[str]] = Query([], description="Bans"),
):

    Team = []
    Ennemies = []
    Bans = []
    Best_Champs = []

    for champs in teammates:
        Team.append(ChampionService().get_champ_by_name(champs))
    for ennems in ennemies:
        Ennemies.append(ChampionService().get_champ_by_name(ennems))
    for champ_bans in bans:
        Bans.append(ChampionService().get_champ_by_name(champ_bans))

    best_champs = ChampionService().best_champs(
        role=role, teammates=Team, ennemies=Ennemies, bans=Bans
    )

    for best in best_champs:
        Best_Champs.append(
            ChampionDTO(
                name=best.name,
                champ_id=best.id,
                blurb=best.blurb,
                tags=best.tags,
                stats=best.stats,
                info=best.info,
                image=best.image,
            )
        )

    return Best_Champs


# item


@app.get("/total_items")
async def get_total_items() -> dict:
    return {"total": len(ItemService().get_all_items())}


@app.get("/items")
async def get_all_items() -> List[ItemDTO]:
    return [
        ItemDTO(
            name=item.name,
            item_id=item.id,
            description=item.description,
            tags=item.tags,
            stats=item.stats,
            image=item.image,
        )
        for item in ItemService().get_all_items()
    ]


@app.get("/item/id/{id}")
async def get_item_by_id(id: int) -> ItemDTO:
    item = ItemService().get_item_by_id(id)
    return ItemDTO(
        name=item.name,
        item_id=item.id,
        description=item.description,
        tags=item.tags,
        stats=item.stats,
        image=item.image,
    )


@app.get("/item/name/{name}")
async def get_item_by_name(name: str) -> ItemDTO:
    item = ItemService().get_item_by_name(name)
    return ItemDTO(
        name=item.name,
        item_id=item.id,
        description=item.description,
        tags=item.tags,
        stats=item.stats,
        image=item.image,
    )
