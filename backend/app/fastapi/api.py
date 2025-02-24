from typing import List  # , Dict, Optional

import app.config.charge_environnement as config
from app.service.champion_service import ChampionService
from app.service.item_service import ItemService
from fastapi import FastAPI, Path  # , Form, HTTPException
from pydantic import BaseModel

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


"""
class User(BaseModel):
    pseudo: str
    password: str
"""


app = FastAPI()

# user
"""
@app.post("/login/")
async def login(data: Annotated[User, Form()]):
    return data
"""
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
