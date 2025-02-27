from typing import List, Optional

from app.dto.champion_dto import ChampionDTO
from app.service.champion_service import ChampionService
from fastapi import APIRouter, Path, Query

champion_router = APIRouter(prefix="/champion", tags=["Champion"])


@champion_router.get("/total_champion")
async def get_total_champion() -> dict:
    return {"total": len(ChampionService().get_all_champs())}


@champion_router.get("/champions", response_model=List[ChampionDTO])
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


@champion_router.get("/id/{id}")
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


@champion_router.get("/name/{name}")
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


@champion_router.get("/best")
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


@champion_router.get("/image")
async def show_image_by_name(name: str):
    return ChampionService().get_champ_by_name(name).show_image()
