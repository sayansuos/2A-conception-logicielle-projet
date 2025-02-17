class Item:
    """
    Représente un item avec ses détails.

    - **name**: Le nom du champion.
    - **title**: Le titre du champion.
    - **blurb**: Une description du champion.
    - **tags**: Une liste de tags associés au champion.
    - **stats** : Un dictionnaire des statistiques du champion
    -- **info** : Un dictionnaire des informations sur les champions.
    - **image** : Une image du champion.
    """

    def __init__(
        self,
        name: str,
        item_id: int,
        description: str,
        tags: list[str],
        stats: dict,
        image: str,
    ):
        """
        Builder
        """
        self.name = name
        self.id = item_id
        self.tags = tags
        self.stats = stats
        self.description = description
        self.image = image

    def __str__(self):
        return f"[{self.id}] {self.name} \n{self.stats}"
