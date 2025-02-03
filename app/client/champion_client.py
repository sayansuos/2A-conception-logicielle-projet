import os
from typing import List

import requests
from dotenv import load_dotenv

# Charger le fichier principal
load_dotenv()

# Charge un fichier local si présent
local_env_path = ".env.local"
if os.path.exists(local_env_path):
    load_dotenv(dotenv_path=local_env_path, override=True)


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
        req = requests.get(f"{self.__host}/champion.json")

        # Initialising the list and filling with the data
        all_champions = []
        if req.status_code == 200:
            raw_types = req.json()["data"]
            for champ in raw_types:
                all_champions.append(
                    [raw_types[champ]["name"], int(raw_types[champ]["key"])]
                )

        return sorted(all_champions)


if __name__ == "__main__":
    champ_list = ChampionClient().get_all_champs()
    print(champ_list)
