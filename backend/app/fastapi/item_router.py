from typing import List

from app.dto.item_dto import ItemDTO
from app.service.item_service import ItemService
from fastapi import APIRouter

item_router = APIRouter(prefix="/item", tags=["Item"])


@item_router.get("/total_items")
async def get_total_items() -> dict:
    return {"total": len(ItemService().get_all_items())}


@item_router.get("/items")
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


@item_router.get("/id/{id}")
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


@item_router.get("/name/{name}")
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
