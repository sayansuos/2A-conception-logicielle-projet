from app.dao.build_dao import BuildDao
from app.models.build import Build
from app.models.champion import Champion
from app.models.item import Item
from app.service.champion_service import ChampionService
from app.service.item_service import ItemService


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

    def get_all_builds(self) -> list[Build]:
        """
        This method gives the list with all the builds of the database.
        """
        all_builds = []

        # Calling the client
        all_builds_raw = BuildDao().read_all_builds()

        # Building each champ
        for raw_build in all_builds_raw:
            id = raw_build[0]
            champion = ChampionService().get_champ_by_id(raw_build[1])
            item1 = ItemService().get_item_by_id(raw_build[2])
            item2 = ItemService().get_item_by_id(raw_build[3])
            item3 = ItemService().get_item_by_id(raw_build[4])
            item4 = ItemService().get_item_by_id(raw_build[5])
            item5 = ItemService().get_item_by_id(raw_build[6])
            build = Build(
                champion=champion,
                item1=item1,
                item2=item2,
                item3=item3,
                item4=item4,
                item5=item5,
                id=id,
            )
            all_builds.append(build)

        return all_builds

    def get_build_by_id(self, build_id: int) -> Build:
        """
        This method gives a build by its id.
        """
        if not isinstance(build_id, int):
            return TypeError("The build's id should be an int instance.")

        wanted_build = None

        builds_list = self.get_all_builds()
        for build in builds_list:
            if build.id == build_id:
                wanted_build = build
        if wanted_build is None:
            raise ValueError("This build's id doesn't exist.")
        else:
            return wanted_build
