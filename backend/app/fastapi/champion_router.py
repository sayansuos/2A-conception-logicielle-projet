""" Champion """

from typing import List, Optional

from app.dto.champion_dto import ChampionDTO
from app.service.champion_service import ChampionService
from fastapi import APIRouter, Path, Query

champion_router = APIRouter(prefix="/champion", tags=["Champion"])


@champion_router.get("/total_champion")
async def get_total_champion() -> dict:
    """
    Returns the total number of available champions.
    """
    return {"total": len(ChampionService().get_all_champs())}


@champion_router.get("/champions", response_model=List[ChampionDTO])
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


@champion_router.get("/id/{champion_id}")
async def get_champion_by_id(champion_id: int = Path(ge=1)) -> ChampionDTO:
    """
    Returns a champion by its ID.
    """
    champion = ChampionService().get_champ_by_id(champion_id)
    return ChampionDTO(
        name=champion.name,
        champ_id=champion.id,
        blurb=champion.blurb,
        tags=champion.tags,
        stats=champion.stats,
        info=champion.info,
        image=champion.image,
    )


@champion_router.get("/name/{name}")
async def get_champion_by_name(name: str) -> ChampionDTO:
    """
    Returns a champion by its name.
    """
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


@champion_router.get("/best")
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

    for champ in teammates:
        team.append(ChampionService().get_champ_by_name(champ))
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
