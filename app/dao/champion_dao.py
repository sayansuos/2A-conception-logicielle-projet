import sqlite3

from app.config.reset_db import ResetDB
from app.config.singleton import Singleton
from app.models.champion import Champion


class ChampionDao(metaclass=Singleton):
    """
    This class contains all the methods required to access the
    database's champions.
    """

    def create(self, champion: Champion, role: str) -> bool:
        """
        This method adds a user to the database.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO champs_data(id, name, role) VALUES (?, ?, ?); ",
            (champion.id, champion.name, role),
        )
        res = cursor.rowcount
        connection.commit()

        return res > 0

    def read_role(self, champion: Champion) -> list:
        """
        This methods gives the roles saved in the db for a champion.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "SELECT role FROM champs_data WHERE id = ?; ",
            (champion.id,),
        )
        res = cursor.fetchone()
        connection.commit()

        role = None
        if res:
            role = list(res)
        return role
