""" Build """

from typing import List

from app.dto.build_dto import BuildDTO
from app.dto.champion_dto import ChampionDTO
from app.fastapi.item_router import ItemDTO
from app.service.build_service import BuildService
from fastapi import APIRouter

build_router = APIRouter(prefix="/build", tags=["Build"])


@build_router.get("/builds")
async def get_all_builds() -> List[BuildDTO]:
    """
    Returns a list of all available builds.
    """
    builds = BuildService().get_all_builds()
    all_builds = [
        BuildDTO(
            champion=ChampionDTO(
                name=build.champion.name,
                champ_id=build.champion.id,
                blurb=build.champion.blurb,
                tags=build.champion.tags,
                stats=build.champion.stats,
                info=build.champion.info,
                image=build.champion.image,
            ),
            item1=ItemDTO(
                name=build.items["item1"].name,
                item_id=build.items["item1"].id,
                description=build.items["item1"].description,
                tags=build.items["item1"].tags,
                stats=build.items["item1"].stats,
                image=build.items["item1"].image,
            ),
            item2=ItemDTO(
                name=build.items["item2"].name,
                item_id=build.items["item2"].id,
                description=build.items["item2"].description,
                tags=build.items["item2"].tags,
                stats=build.items["item2"].stats,
                image=build.items["item2"].image,
            ),
            item3=ItemDTO(
                name=build.items["item3"].name,
                item_id=build.items["item3"].id,
                description=build.items["item3"].description,
                tags=build.items["item3"].tags,
                stats=build.items["item3"].stats,
                image=build.items["item3"].image,
            ),
            item4=ItemDTO(
                name=build.items["item4"].name,
                item_id=build.items["item4"].id,
                description=build.items["item4"].description,
                tags=build.items["item4"].tags,
                stats=build.items["item4"].stats,
                image=build.items["item4"].image,
            ),
            item5=ItemDTO(
                name=build.items["item5"].name,
                item_id=build.items["item5"].id,
                description=build.items["item5"].description,
                tags=build.items["item5"].tags,
                stats=build.items["item5"].stats,
                image=build.items["item5"].image,
            ),
            id=build.id,
        )
        for build in builds
    ]
    return all_builds


@build_router.get("/build/{id}")
async def get_build_by_id(id: int) -> BuildDTO:
    """
    Returns a Build by its id.
    """
    build = BuildService().get_build_by_id(id)
    return BuildDTO(
        champion=ChampionDTO(
            name=build.champion.name,
            champ_id=build.champion.id,
            blurb=build.champion.blurb,
            tags=build.champion.tags,
            stats=build.champion.stats,
            info=build.champion.info,
            image=build.champion.image,
        ),
        item1=ItemDTO(
            name=build.items["item1"].name,
            item_id=build.items["item1"].id,
            description=build.items["item1"].description,
            tags=build.items["item1"].tags,
            stats=build.items["item1"].stats,
            image=build.items["item1"].image,
        ),
        item2=ItemDTO(
            name=build.items["item2"].name,
            item_id=build.items["item2"].id,
            description=build.items["item2"].description,
            tags=build.items["item2"].tags,
            stats=build.items["item2"].stats,
            image=build.items["item2"].image,
        ),
        item3=ItemDTO(
            name=build.items["item3"].name,
            item_id=build.items["item3"].id,
            description=build.items["item3"].description,
            tags=build.items["item3"].tags,
            stats=build.items["item3"].stats,
            image=build.items["item3"].image,
        ),
        item4=ItemDTO(
            name=build.items["item4"].name,
            item_id=build.items["item4"].id,
            description=build.items["item4"].description,
            tags=build.items["item4"].tags,
            stats=build.items["item4"].stats,
            image=build.items["item4"].image,
        ),
        item5=ItemDTO(
            name=build.items["item5"].name,
            item_id=build.items["item5"].id,
            description=build.items["item5"].description,
            tags=build.items["item5"].tags,
            stats=build.items["item5"].stats,
            image=build.items["item5"].image,
        ),
        id=build.id,
    )
