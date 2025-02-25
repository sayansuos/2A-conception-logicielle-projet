from typing import Dict, Optional

from app.dto.build_dto import BuildDTO
from app.dto.champion_dto import ChampionDTO
from pydantic import BaseModel


class UserDTO(BaseModel):
    """
    Représente un utilisateur et ses détails.
    """

    user_id: int
    pseudo: str
    pref: Optional[Dict[ChampionDTO, BuildDTO]]
