import os
from typing import List

import requests


class ChampionClient:
    """
    This class calls all the data from the champions' endpoint.
    """

    def __init__(self) -> None:
        """
        Builder
        """
        self.__host = os.getenv("DATA_URL")
        self.__host_image = (
            "https://ddragon.leagueoflegends.com/cdn/img/champion/loading"
        )

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
                image = (
                    self.__host_image
                    + "/"
                    + name.replace(" ", "").replace("'", "")
                    + "_0.jpg"
                )

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
