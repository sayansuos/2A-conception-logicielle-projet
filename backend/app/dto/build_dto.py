from typing import Optional

from app.dto.champion_dto import ChampionDTO
from app.dto.item_dto import ItemDTO
from pydantic import BaseModel


class BuildDTO(BaseModel):
    """
    Représente un builds avec ses détails.
    """

    champion: ChampionDTO
    item1: Optional[ItemDTO] = None
    item2: Optional[ItemDTO] = None
    item3: Optional[ItemDTO] = None
    item4: Optional[ItemDTO] = None
    item5: Optional[ItemDTO] = None
