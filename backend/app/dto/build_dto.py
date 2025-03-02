from typing import Optional

from app.dto.champion_dto import ChampionDTO
from app.dto.item_dto import ItemDTO
from pydantic import BaseModel


class BuildDTO(BaseModel):
    """
    Représente un builds avec ses détails.
    """

    champion: ChampionDTO
    item1: ItemDTO
    item2: ItemDTO
    item3: ItemDTO
    item4: ItemDTO
    item5: ItemDTO
    id: Optional[int] = None
