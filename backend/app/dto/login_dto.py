from pydantic import BaseModel


class LoginUserDTO(BaseModel):
    """
    Authentification d'un utilisateur avec ses détails.
    """

    pseudo: str
    pwd: str
