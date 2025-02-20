from app.client.item_client import ItemClient
from app.dao.item_dao import ItemDao
from app.models.item import Item


class ItemService:
    """
    This class contains all the service's methods for the champions.
    """

    def get_all_items(self) -> list[Item]:
        """
        This method gives the list with all the champions of the API.
        """
        all_items = []

        # Calling the client
        all_items_raw = ItemClient().get_all_items()

        # Building each champ
        for i in all_items_raw:
            name = i["name"]
            item_id = i["id"]
            tags = i["tags"]
            stats = i["stats"]
            description = i["description"]
            image = i["image"]
            item = Item(
                name=name,
                item_id=item_id,
                description=description,
                tags=tags,
                stats=stats,
                image=image,
            )
            all_items.append(item)

        return list(set(all_items))

    def print_all_items(self):
        """
        This methods prints all the items.
        """
        items_list = self.get_all_items()
        for item in items_list:
            print(f"{item}\n")

    def get_item_by_id(self, item_id: int) -> Item:
        """
        This method gives an item by its id.
        """
        if not isinstance(item_id, int):
            return TypeError("The item's id should be an int instance.")

        wanted_item = None

        items_list = self.get_all_items()
        for item in items_list:
            if item.id == item_id:
                wanted_item = item
        if wanted_item is None:
            raise ValueError("This item's id doesn't exist.")
        else:
            return wanted_item

    def get_item_by_name(self, item_name: str) -> Item:
        """
        This method gives an item by its id.
        """
        if not isinstance(item_name, str):
            return TypeError("The item's id should be an str instance.")

        wanted_item = None

        items_list = self.get_all_items()
        for item in items_list:
            if item.name.upper() == item_name.upper():
                wanted_item = item
        if wanted_item is None:
            raise ValueError("This item's name doesn't exist.")
        else:
            return wanted_item

    def create_all_items(self) -> bool:
        """
        This method add all the items to the database.
        """
        items_list = self.get_all_items()
        all_created = True
        for item in items_list:
            created = ItemDao().create(item=item)
            if not created:
                all_created = False

        return all_created
