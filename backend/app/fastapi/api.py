from typing import List, Optional

import app.config.charge_environnement as config
from app.dto.champion_dto import ChampionDTO
from app.dto.item_dto import ItemDTO
from app.dto.user_dto import UserDTO
from app.service.champion_service import ChampionService
from app.service.item_service import ItemService
from app.service.user_service import UserService
from fastapi import FastAPI, Path, Query

# from app.dto.build_dto import BuildDTO
# from app.models.build import Build
# from app.dto.login_dto import LoginUserDTO


config.load_dotenv()


app = FastAPI()

# user


@app.get("/user/{pseudo}")
async def get_user_by_pseudo(pseudo: str) -> UserDTO:
    user = UserService().get_by_pseudo(pseudo=pseudo)
    return UserDTO(pseudo=user.pseudo, pref=user.pref)


"""
@app.post("/user/addbuild")
async def add_build(user:UserDTO, build:BuildDTO) -> UserDTO:
    build_added = UserService().add_build(
        user=UserService().get_by_pseudo(user.pseudo),
        build= Build(**build)
    )
    return BuildDTO(**build_added.__dict__)


# login

@app.post("/user/create")
async def create_user(
    pseudo: str = Query(...,description="Your username"),
    pwd: str = Query(...,description="Your password")
):
    user_id = UserService().create(pseudo=pseudo,pwd=pwd)
    return user_id

@app.post("/user/login")
async def login_user(request: LoginUserDTO):
    user = UserService().login(pseudo=request.pseudo, pwd=request.pwd)
    user_id = UserService().get_by_pseudo(pseudo=request.pseudo).id
    return UserDTO(user_id=user_id, pseudo=user.pseudo, pref=user.pref)
"""

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
