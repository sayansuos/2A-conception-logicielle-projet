from app.config.security import hash_password
from app.dao.user_dao import UserDao
from app.models.build import Build
from app.models.user import User
from app.service.build_service import BuildService


class UserService:
    """
    This class describes the methods of the User's class.
    """

    def create(self, pseudo: str, pwd: str) -> User:
        """
        This method adds a user to the database.
        """
        if not isinstance(pseudo, str):
            raise TypeError("The pseudo should be an str instance.")
        if not isinstance(pwd, str):
            raise TypeError("The password should be an str instance.")

        pwd = hash_password(password=pwd, sel=pseudo)
        user = User(None, pseudo=pseudo, pwd=pwd)

        UserDao().create(user=user)
        return user

    def get_all_users(self, pwd_included=False) -> list[User]:
        """
        This method gives all the users from the database.
        """
        users_list = UserDao().read_all_users()
        if not pwd_included:
            for user in users_list:
                user.pwd = None
        return users_list

    def user_in_db(self, pseudo: str) -> bool:
        """
        This methods gives True if the pseudo is one of the users
        in the database. False otherwise.
        """
        users_list = UserDao().read_all_users()
        is_in_db = False
        for user in users_list:
            if user.pseudo == pseudo:
                is_in_db = True

        return is_in_db

    def print_all_users(self):
        """
        This method prints all the users.
        """
        users_list = UserDao().read_all_users()
        for user in users_list:
            print(user)

    def get_by_pseudo(self, pseudo: str, pwd_included=False) -> User:
        """
        This methods gives a user by its pseudo.
        """
        if not isinstance(pseudo, str):
            raise TypeError("The pseudo should be an str instance.")
        if not self.user_in_db(pseudo=pseudo):
            raise ValueError("This pseudo doesn't exist in the database.")

        user = UserDao().read_where_pseudo(where_pseudo=pseudo)
        if not pwd_included:
            user.pwd = None
        return user

    def delete_where_pseudo(self, pseudo: str) -> bool:
        """
        This methods deletes a user from the database by its pseudo.
        """
        if not isinstance(pseudo, str):
            raise TypeError("The pseudo should be an str instance.")
        if not self.user_in_db(pseudo=pseudo):
            raise ValueError("This pseudo doesn't exist in the database.")

        return UserDao().delete_where_pseudo(where_pseudo=pseudo)

    def login(self, pseudo: str, pwd: str) -> User:
        """
        This method allows a user to log in.
        """
        if not isinstance(pseudo, str):
            raise TypeError("The pseudo should be an str instance.")
        if not self.user_in_db(pseudo=pseudo):
            raise ValueError("This pseudo doesn't exist in the database.")
        if not isinstance(pwd, str):
            raise TypeError("The password should be an str instance.")

        return UserDao().login(
            pseudo=pseudo, pwd=hash_password(password=pwd, sel=pseudo)
        )

    def add_build(self, user: User, build: Build) -> bool:
        """
        This methods add a build's preference for an user to the db.
        """
        if not isinstance(user, User):
            raise TypeError("The user should be an User instance.")
        if not isinstance(build, Build):
            raise TypeError("The build should be a Build instance.")

        return UserDao().add_build(user=user, build=build)

    def get_user_build(self, user: User) -> list[Build]:
        """
        This method gives all the builds associated to an user from
        the database.
        """
        builds_list_raw = UserDao().read_user_builds(user=user)

        builds_list = []
        for raw_build in builds_list_raw:
            build = BuildService().get_build_by_id(raw_build[1])
            builds_list.append(build)

        return builds_list
