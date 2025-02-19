from app.client.champion_client import ChampionClient
from app.client.role_client import RoleClient
from app.dao.champion_dao import ChampionDao
from app.models.champion import Champion


class ChampionService:
    """
    This class contains all the service's methods for the champions.
    """

    def get_all_champs(self) -> list[Champion]:
        """
        This method gives the list with all the champions of the API.
        """
        all_champs = []

        # Calling the client
        all_champs_raw = ChampionClient().get_all_champs()

        # Building each champ
        for c in all_champs_raw:
            name = c["name"]
            champ_id = c["id"]
            blurb = c["blurb"]
            tags = c["tags"]
            stats = c["stats"]
            info = c["info"]
            image = c["image"]
            champ = Champion(
                name=name,
                champ_id=champ_id,
                blurb=blurb,
                tags=tags,
                stats=stats,
                info=info,
                image=image,
            )
            all_champs.append(champ)

        return all_champs

    def get_champ_by_id(self, champ_id: int) -> Champion:
        """
        This method gives a champ by its id.
        """
        if not isinstance(champ_id, int):
            return TypeError("The champ's id should be an int instance.")

        wanted_champ = None

        champs_list = self.get_all_champs()
        for champ in champs_list:
            if champ.id == champ_id:
                wanted_champ = champ
        if wanted_champ is None:
            raise ValueError("This champ's id doesn't exist.")
        else:
            return wanted_champ

    def get_champ_by_name(self, champ_name: str) -> Champion:
        """
        This method gives a champ by its id.
        """
        if not isinstance(champ_name, str):
            return TypeError("The champ's id should be an str instance.")

        wanted_champ = None

        champs_list = self.get_all_champs()
        for champ in champs_list:
            if champ.name.upper() == champ_name.upper():
                wanted_champ = champ
        if wanted_champ is None:
            raise ValueError("This champ's name doesn't exist.")
        else:
            return wanted_champ

    def get_playrate(self, champ: Champion) -> dict:
        """
        This methods gives the role of the champ.
        """
        return RoleClient().get_playrate_by_id(champ.id)

    def get_all_champs_by_role(self, role: str) -> list:
        """
        This method gives the list of all champions according to a given role.
        """
        if role not in ["TOP", "JGL", "MID", "BOT", "SUPP"]:
            raise ValueError("This role doesn't exist.")

        playable_champs_for_role = []

        champs_list = self.get_all_champs()
        for champ in champs_list:
            if self.get_playrate(champ)[role] != 0:
                playable_champs_for_role.append(champ)

        return playable_champs_for_role

    def available_champs_by_role(
        self, role: str, picks: list = None, bans: list = None
    ) -> list:
        """
        This method gives the list of all available champions someone can choose to
        play according to their role.
        """
        if picks is None:
            picks = []

        if bans is None:
            bans = []

        available_champs_for_role = self.get_all_champs_by_role(role)

        unplayable_champs = picks + bans

        for champ_name in unplayable_champs:
            for champ in available_champs_for_role:
                if champ_name == champ.name:
                    available_champs_for_role.remove(champ)

        return available_champs_for_role

    def create_all_champs(self) -> bool:
        """
        This method add all the champions to the database.
        """
        champs_list = self.get_all_champs()
        all_created = True
        for champ in champs_list:
            created = ChampionDao().create(champion=champ)
            if not created:
                all_created = False

        return all_created
