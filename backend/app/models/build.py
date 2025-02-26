from app.models.champion import Champion
from app.models.item import Item


class Build:
    """
    Représente un build avec ses détails.

    - **champion**: Champion associé au build.
    - **items**: Dictionnaire des Items qui constituent le build.
    """

    def __init__(
        self,
        champion: Champion,
        item1: Item = None,
        item2: Item = None,
        item3: Item = None,
        item4: Item = None,
        item5: Item = None,
        id: int = None,
    ):
        """
        Builder
        """
        self.champion = champion
        self.items = {
            "item1": item1,
            "item2": item2,
            "item3": item3,
            "item4": item4,
            "item5": item5,
        }
        self.id = id

    def __str__(self):
        champion = f"** {self.champion}'s Build **\n"
        items = ""
        for index_item, item in self.items.items():
            items += f"{index_item} : [{item.id}] {item.name}\n"
        return champion + items
