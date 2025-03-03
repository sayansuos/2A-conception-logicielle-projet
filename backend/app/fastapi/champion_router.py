""" Champion """

import string
from typing import List, Optional, Union

from app.dto.champion_dto import ChampionDTO
from app.service.champion_service import ChampionService
from fastapi import APIRouter, Query

champion_router = APIRouter(prefix="/champion", tags=["Champion"])


@champion_router.get("/total")
async def get_total_champion() -> dict:
    """
    Returns the total number of available champions.
    """
    return {"total": len(ChampionService().get_all_champs())}


@champion_router.get("/all", response_model=List[ChampionDTO])
async def get_all_champions() -> list[ChampionDTO]:
    """
    Returns a list of all available champions.
    """
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


@champion_router.get("/names")
async def get_champion_names() -> List[str]:
    """
    Returns a list of all champions name available in the system.
    """
    return [champion.name for champion in ChampionService().get_all_champs()]


@champion_router.get("/id_name/{champion}")
async def get_champion_by_id_or_name(champion: Union[int, str]) -> ChampionDTO:
    """
    Returns a champion by its ID or its name.
    """
    is_name = False
    for (
        lettre
    ) in (
        string.ascii_lowercase
    ):  # string.ascii_lowercase contient toutes les lettres minuscules
        if lettre in champion.lower():
            is_name = True
            break
    if is_name is True:
        champ = ChampionService().get_champ_by_name(champion)
    else:
        champ = ChampionService().get_champ_by_id(int(champion))

    return ChampionDTO(
        name=champ.name,
        champ_id=champ.id,
        blurb=champ.blurb,
        tags=champ.tags,
        stats=champ.stats,
        info=champ.info,
        image=champ.image,
    )


@champion_router.get("/besttoplay")
async def get_best_champs(
    role: str = Query(..., description="Role of the player"),
    teammates: Optional[List[str]] = Query([], description="Allies"),
    ennemies: Optional[List[str]] = Query([], description="Enemies"),
    bans: Optional[List[str]] = Query([], description="Bans"),
):
    """
    Returns the best champions for a specific role considering
    allies, enemies, and bans.
    """
    team = []
    enemies = []
    banned_champs = []
    best_champs = []

    for champi in teammates:
        team.append(ChampionService().get_champ_by_name(champi))

    for ennemy in ennemies:
        enemies.append(ChampionService().get_champ_by_name(ennemy))

    for banned in bans:
        banned_champs.append(ChampionService().get_champ_by_name(banned))

    best_champs_list = ChampionService().best_champs(
        role=role, teammates=team, ennemies=enemies, bans=banned_champs
    )

    for best in best_champs_list:
        best_champs.append(
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

    return best_champs


@champion_router.get("/image")
async def show_image_by_name(name: str):
    """
    Displays the image of a champion by its name.
    """
    return ChampionService().get_champ_by_name(name).show_image_plt()
