from typing import List

from pydantic import BaseModel


class ItemDTO(BaseModel):
    """
    Représente un item avec ses détails.
    """

    name: str
    item_id: int
    description: str
    tags: List[str]
    stats: dict
    image: str
