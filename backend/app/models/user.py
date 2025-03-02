class User:
    """
    This class describes a user with its details.

    - **pseudo**: Pseudonyme of the user.
    - **id**: Identifiant of the user.
    - **pwd**: Password of the user.
    - **pref**: A list with associated builds' id.
    """

    def __init__(self, user_id: int, pseudo: str, pwd: str, pref: list = None):
        """
        Builder
        """
        self.pseudo = pseudo
        self.id = user_id
        self.pwd = pwd
        self.pref = pref

    def __str__(self):
        return f"[{self.id}] {self.pseudo}"

    @classmethod
    def from_data(cls, data: dict):
        """
        Builds a User using its details from the data.
        """
        return User(None, data["pseudo"], data["pwd"], data["pref"])

    @classmethod
    def from_sql_result(cls, data: tuple):
        """
        Builds a User using its details from the sql result.
        """
        if data is None:
            return None
        return User(data[0], data[1], data[2])
