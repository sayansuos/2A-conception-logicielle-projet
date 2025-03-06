""" Item """

from typing import List, Union

from app.dto.item_dto import ItemDTO
from app.service.item_service import ItemService
from fastapi import APIRouter

item_router = APIRouter(prefix="/item", tags=["Item"])


@item_router.get("/total")
async def get_total_items() -> dict:
    """
    Returns the total number of items available in the system.
    """
    return {"total": len(ItemService().get_all_items())}


@item_router.get("/all")
async def get_all_items() -> List[ItemDTO]:
    """
    Returns a list of all items available in the system.
    """
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


@item_router.get("/names")
async def get_items_names() -> List[str]:
    """
    Returns a list of all items name available in the system.
    """
    return [item.name for item in ItemService().get_all_items()]


@item_router.get("/id_name/{item}")
async def get_item_by_id_or_name(item: Union[int, str]) -> ItemDTO:
    """
    Returns an item by its ID.
    """
    try:
        item_id = int(item)
        item_wanted = ItemService().get_item_by_id(item_id=item_id)
    except ValueError:
        item_wanted = ItemService().get_item_by_name(item_name=item)

    return ItemDTO(
        name=item_wanted.name,
        item_id=item_wanted.id,
        description=item_wanted.description,
        tags=item_wanted.tags,
        stats=item_wanted.stats,
        image=item_wanted.image,
    )


@item_router.get("/image")
async def show_image_by_name(name: str):
    """
    Displays the image of an item by its name.
    """
    return ItemService().get_item_by_name(name).show_image_plt()
