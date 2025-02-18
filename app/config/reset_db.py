import os
import sqlite3

from app.config.singleton import Singleton


class ResetDB(metaclass=Singleton):
    """
    This class resets the database.
    """

    def __init__(self) -> None:
        """
        Builder
        """
        self.__db_path = os.getenv("DB_PATH", "data/database.db")

    def init_db(self):
        """
        This method creates the data's tables if its doesnt exist.
        """
        connection = sqlite3.connect(self.__db_path)
        cursor = connection.cursor()

        init_db = open("data/init_db.sql", encoding="utf-8")
        init_db_as_string = init_db.read()
        init_db.close()

        cursor.executescript(init_db_as_string)
        connection.commit()
