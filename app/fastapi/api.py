from typing import Dict, List, Optional

from fastapi import FastAPI, Path, Query  # , Form, HTTPException
from pydantic import BaseModel

import app.config.charge_environnement as config
from app.service.champion_service import ChampionService
from app.service.item_service import ItemService
from app.service.user_service import UserService

# from typing import Annotated
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from starlette.requests import Request


# from service.user_service import UserService

config.load_dotenv()

# model pydantic


class Champion(BaseModel):
    """
    Représente un champion avec ses détails.
    """

    name: str
    champ_id: int
    blurb: str
    tags: list[str]
    stats: dict
    info: dict
    image: str


class Item(BaseModel):
    """
    Représente un item avec ses détails.
    """

    name: str
    item_id: int
    description: str
    tags: list[str]
    stats: dict
    image: str


class Build(BaseModel):
    """
    Représente un builds avec ses détails.
    """

    champion: Champion
    item1: Optional[Item] = None
    item2: Optional[Item] = None
    item3: Optional[Item] = None
    item4: Optional[Item] = None
    item5: Optional[Item] = None


class User(BaseModel):
    """
    Représente un utilisateur et ses détails.
    """

    user_id: int
    pseudo: str
    pref: Optional[Dict[Champion, Build]]


class LoginUser(BaseModel):
    """
    Authentification d'un utilisateur avec ses détails.
    """

    pseudo: str
    pwd: str


app = FastAPI()

# user


@app.get("/user/{pseudo}")
async def get_user_by_pseudo(pseudo: str) -> User:
    user = UserService().get_by_pseudo(pseudo=pseudo)
    return User(user_id=user.id, pseudo=user.pseudo, pref=user.pref)


# build

# champion


@app.get("/total_champion")
async def get_total_champion() -> dict:
    return {"total": len(ChampionService().get_all_champs())}


@app.get("/champions", response_model=List[Champion])
async def get_all_champions() -> list[Champion]:
    return [
        Champion(
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
async def get_champion_by_id(id: int = Path(ge=1)) -> Champion:
    champion = ChampionService().get_champ_by_id(id)
    return Champion(
        name=champion.name,
        champ_id=champion.id,
        blurb=champion.blurb,
        tags=champion.tags,
        stats=champion.stats,
        info=champion.info,
        image=champion.image,
    )


@app.get("/champion/name/{name}")
async def get_champion_by_name(name: str) -> Champion:
    champion = ChampionService().get_champ_by_name(name)
    return Champion(
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
            Champion(
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
async def get_all_items() -> List[Item]:
    return [
        Item(
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
async def get_item_by_id(id: int) -> Item:
    item = ItemService().get_item_by_id(id)
    return Item(
        name=item.name,
        item_id=item.id,
        description=item.description,
        tags=item.tags,
        stats=item.stats,
        image=item.image,
    )


@app.get("/item/name/{name}")
async def get_item_by_name(name: str) -> Item:
    item = ItemService().get_item_by_name(name)
    return Item(
        name=item.name,
        item_id=item.id,
        description=item.description,
        tags=item.tags,
        stats=item.stats,
        image=item.image,
    )


# templates = Jinja2Templates(directory="app/templates")
