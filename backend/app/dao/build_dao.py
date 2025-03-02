import sqlite3

from app.config.reset_db import ResetDB
from app.config.singleton import Singleton
from app.models.build import Build


class BuildDao(metaclass=Singleton):
    """
    This class contains all the methods required to access the
    builds' database.
    """

    def create(self, build: Build) -> bool:
        """
        This method adds a build to the database.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO builds_data(champ_id, "
            "item1_id, item2_id, item3_id, item4_id, item5_id)"
            " VALUES (?, ?, ?, ?, ?, ?); ",
            (
                build.champion.id,
                build.items["item1"].id,
                build.items["item2"].id,
                build.items["item3"].id,
                build.items["item4"].id,
                build.items["item5"].id,
            ),
        )
        build.id = cursor.lastrowid
        connection.commit()

        return build.id is not None

    def read_all_builds(self) -> list[Build]:
        """
        This methods gives all the bulds from the database.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM builds_data",
        )
        res = cursor.fetchall()

        builds_list = []
        for build_raw in res:
            builds_list.append(build_raw)

        return builds_list
