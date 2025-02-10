import os
from typing import List

import requests
from dotenv import load_dotenv

# Charger le fichier principal
load_dotenv()

# Charge un fichier local si présent
LOCAL_ENV_PATH = ".env.local"
if os.path.exists(LOCAL_ENV_PATH):
    load_dotenv(dotenv_path=LOCAL_ENV_PATH, override=True)


class ChampionClient:
    """
    This class calls all the data from the champions' endpoint.
    """

    def __init__(self) -> None:
        """
        Builder
        """
        self.__host = os.environ["DATA_URL"]

    def get_all_champs(self) -> List[str]:
        """
        This method gives the whole champions' list.
        """
        # Calling the API
        req = requests.get(f"{self.__host}/champion.json", timeout=None)

        # Initialising the list and filling with the datanzb
        all_champions = []
        if req.status_code == 200:
            raw_types = req.json()["data"]
            for champ in raw_types:
                name = raw_types[champ]["name"]
                champ_id = int(raw_types[champ]["key"])
                blurb = raw_types[champ]["blurb"]
                tags = raw_types[champ]["tags"]
                stats = raw_types[champ]["stats"]
                info = raw_types[champ]["info"]
                image = raw_types[champ]["image"]

                c = {
                    "name": name,
                    "id": champ_id,
                    "blurb": blurb,
                    "tags": tags,
                    "stats": stats,
                    "info": info,
                    "image": image,
                }

                all_champions.append(c)

        return all_champions


if __name__ == "__main__":
    champ_list = ChampionClient().get_all_champs()
    print(champ_list[0])
