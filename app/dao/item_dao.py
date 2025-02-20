import sqlite3

from app.config.reset_db import ResetDB
from app.config.singleton import Singleton
from app.models.item import Item


class ItemDao(metaclass=Singleton):
    """
    This class contains all the methods required to access the
    items' database.
    """

    def create(self, item: Item) -> bool:
        """
        This method adds a item to the database.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO items_data(id, name) VALUES (?, ?); ",
            (item.id, item.name),
        )
        res = cursor.rowcount
        connection.commit()

        return res > 0
