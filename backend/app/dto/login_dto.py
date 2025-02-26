from pydantic import BaseModel, SecretStr


class LoginUserDTO(BaseModel):
    """
    Authentification d'un utilisateur avec ses détails.
    """

    pseudo: str
    pwd: SecretStr
