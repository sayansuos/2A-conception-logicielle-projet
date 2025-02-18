import sqlite3

from app.config.reset_db import ResetDB
from app.config.singleton import Singleton
from app.models.champion import Champion


class ChampionDao(metaclass=Singleton):
    """
    This class contains all the methods required to access the
    database's champions.
    """

    def create(self, champion: Champion) -> bool:
        """
        This method adds a user to the database.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO champs_data(id, name) VALUES (?, ?); ",
            (champion.id, champion.name),
        )
        res = cursor.rowcount
        connection.commit()

        return res > 0
