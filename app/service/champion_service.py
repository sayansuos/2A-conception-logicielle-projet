from app.client.champion_client import ChampionClient
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
        if not isinstance(champ_name, int):
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
