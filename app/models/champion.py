class Champion:
    """Représente un champion avec ses détails.

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
        champ_id: int,
        blurb: str,
        tags: list[str],
        stats: dict,
        info: dict,
        image: str,
    ):
        """
        Builder
        """
        self.name: str = name
        self.id = champ_id
        self.blurb = blurb
        self.tags = tags
        self.stats = stats
        self.info = info
        self.image = image

    def __str__(self):
        return f"[{self.id}] {self.name}"
