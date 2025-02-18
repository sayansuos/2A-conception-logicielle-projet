import sqlite3

from app.config.reset_db import ResetDB
from app.models.user import User


class UserDao:
    """
    This class contains all the methods required to access the
    database's users.
    """

    def create(self, user: User) -> bool:
        """
        This method adds a user to the database.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO users_data(pseudo, pwd) VALUES (?, ?); ",
            (user.pseudo, user.pwd),
        )
        user.id = cursor.lastrowid
        connection.commit()
        cursor.close()
        connection.close()

        return user.id is not None

    def read_all_users(self) -> list[User]:
        """
        This methods gives all the users from the database.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users_data",
        )
        res = cursor.fetchall()

        users_list = []
        for user in res:
            users_list.append(User.from_sql_result(user))

        return users_list

    def read_where_pseudo(self, where_pseudo: str) -> User:
        """
        This method gives a user from the database by its pseudo.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users_data WHERE pseudo = ?; ",
            (where_pseudo,),
        )
        res = cursor.fetchone()

        user = None
        if res:
            user = User.from_sql_result(res)
        return user

    def delete_where_pseudo(self, where_pseudo: str) -> bool:
        """
        This methods deletes a user from the database by its pseudo.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM users_data WHERE pseudo = ?; ",
            (where_pseudo,),
        )
        res = cursor.rowcount
        connection.commit()

        return res > 0

    def login(self, pseudo: str, pwd: str) -> User:
        """
        This method allows a user to log in.
        """
        connection = sqlite3.connect(ResetDB().get_db_path())
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users_data WHERE pseudo=? AND pwd=?", (pseudo, pwd)
        )
        res = cursor.fetchone()
        connection.commit()

        user = None
        if res:
            user = User.from_sql_result(res)

        return user
