from typing import List

from pydantic import BaseModel


class ChampionDTO(BaseModel):
    """
    Représente un champion avec ses détails.
    """

    name: str
    champ_id: int
    blurb: str
    tags: List[str]
    stats: dict
    info: dict
    image: str
