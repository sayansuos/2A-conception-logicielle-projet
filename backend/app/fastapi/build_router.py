""" Build """

from typing import List

from app.dto.build_dto import BuildDTO
from app.dto.champion_dto import ChampionDTO
from app.fastapi.item_router import ItemDTO
from app.service.build_service import BuildService
from app.service.champion_service import ChampionService
from app.service.item_service import ItemService
from app.service.user_service import UserService
from fastapi import APIRouter, Query

build_router = APIRouter(prefix="/build", tags=["Build"])


@build_router.get("/all")
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


@build_router.get("/user")
async def get_build_by_user(user_pseudo: str) -> List[BuildDTO]:
    user = UserService().get_by_pseudo(pseudo=user_pseudo)
    builds = UserService().get_user_build(user=user)
    return [
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


@build_router.get("/{id}")
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


@build_router.post("/create")
async def add_build(
    champion_name: str,
    item1_name: str,
    item2_name: str,
    item3_name: str,
    item4_name: str,
    item5_name: str,
    pseudo: str = Query(..., description="Username"),
) -> bool:
    """
    Add a build for a user.
    """
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
