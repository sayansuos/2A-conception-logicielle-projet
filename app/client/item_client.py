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


class ItemClient:
    """
    This class calls all the data from the items' endpoint.
    """

    def __init__(self) -> None:
        """
        Builder
        """
        self.__host = os.environ["DATA_URL"]

    def get_all_items(self) -> List[str]:
        """
        This method gives the whole items' list.
        """
        # Calling the API
        req = requests.get(f"{self.__host}/item.json")

        # Initialising the list and filling with the data
        all_items = []
        if req.status_code == 200:
            raw_types = req.json()["data"]
            for item_id in raw_types:
                if (
                    not "into" in raw_types[item_id]
                    and raw_types[item_id]["gold"]["base"] != 0
                    and raw_types[item_id]["gold"]["purchasable"]
                ):
                    all_items.append([int(item_id), raw_types[item_id]["name"]])

        return sorted(all_items)


if __name__ == "__main__":
    item_list = ItemClient().get_all_items()
    print(item_list)
