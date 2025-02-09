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


if __name__ == "__main__":
    champ_list = ChampionService().get_all_champs()
    print(champ_list[0])
