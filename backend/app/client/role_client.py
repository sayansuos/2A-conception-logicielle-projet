import os
from typing import List

import requests


class RoleClient:
    """
    This class calls all the data from the playrates' endpoint.
    """

    def __init__(self) -> None:
        """
        Builder
        """
        self.__host = os.getenv("DATA_PLAYRATES")

    def get_all_playrates(self) -> List[str]:
        """
        This method gives the whole champions' list.
        """
        # Calling the API
        req = requests.get(f"{self.__host}/championrates.json", timeout=None)

        # Initialising the list and filling with the datan
        all_playrates = []
        if req.status_code == 200:
            raw_types = req.json()["data"]
            for champ in raw_types:
                top = float(raw_types[champ]["TOP"]["playRate"])
                jungle = float(raw_types[champ]["JUNGLE"]["playRate"])
                middle = float(raw_types[champ]["MIDDLE"]["playRate"])
                bottom = float(raw_types[champ]["BOTTOM"]["playRate"])
                utility = float(raw_types[champ]["UTILITY"]["playRate"])
                champ_id = int(champ)

                playrate = {
                    "id": champ_id,
                    "TOP": top,
                    "JGL": jungle,
                    "MID": middle,
                    "BOT": bottom,
                    "SUPP": utility,
                }

                all_playrates.append(playrate)

        return all_playrates

    def get_playrate_by_id(self, champ_id: int):
        """
        This methods gives the playrate of a champ.
        """
        if not isinstance(champ_id, int):
            return TypeError("The champ's id should be an int instance.")

        wanted_playrate = None

        all_playrates = self.get_all_playrates()
        for pr in all_playrates:
            if pr["id"] == champ_id:
                wanted_playrate = pr
        if wanted_playrate is None:
            raise ValueError("This champ's id doesn't exist.")
        else:
            return wanted_playrate
