from app.dao.build_dao import BuildDao
from app.models.build import Build
from app.models.champion import Champion
from app.models.item import Item


class BuildService:
    """
    This class describes the methods of the Build's class.
    """

    def create(
        self,
        champion: Champion,
        item1: Item = None,
        item2: Item = None,
        item3: Item = None,
        item4: Item = None,
        item5: Item = None,
    ) -> Build:
        """
        This method adds a user to the database.
        """
        if not isinstance(champion, Champion):
            raise TypeError("The champion should be a Champion instance.")
        if not isinstance(item1, Item):
            raise TypeError("The item1 should be a Item instance.")
        if not isinstance(item2, Item):
            raise TypeError("The item2 should be a Item instance.")
        if not isinstance(item3, Item):
            raise TypeError("The item3 should be a Item instance.")
        if not isinstance(item4, Item):
            raise TypeError("The item4 should be a Item instance.")
        if not isinstance(item4, Item):
            raise TypeError("The item5 should be a Item instance.")

        build = Build(
            champion=champion,
            item1=item1,
            item2=item2,
            item3=item3,
            item4=item4,
            item5=item5,
        )
        BuildDao().create(build=build)
        return build
