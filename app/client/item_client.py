import os
from typing import List

import requests


class ItemClient:
    """
    This class calls all the data from the items' endpoint.
    """

    def __init__(self) -> None:
        """
        Builder
        """
        self.__host = os.getenv("DATA_URL")

    def get_all_items(self) -> List[str]:
        """
        This method gives the whole items' list.
        """
        # Calling the API
        req = requests.get(f"{self.__host}/item.json", timeout=None)

        # Initialising the list and filling with the data
        all_items = []
        if req.status_code == 200:
            raw_types = req.json()["data"]
            for item in raw_types:
                if (
                    "into" not in raw_types[item]
                    and raw_types[item]["gold"]["base"] != 0
                    and raw_types[item]["gold"]["purchasable"]
                ):
                    name = raw_types[item]["name"]
                    item_id = int(item)
                    description = raw_types[item]["plaintext"]
                    tags = raw_types[item]["tags"]
                    stats = raw_types[item]["stats"]
                    image = raw_types[item]["image"]

                    i = {
                        "name": name,
                        "id": item_id,
                        "description": description,
                        "tags": tags,
                        "stats": stats,
                        "image": image,
                    }

                    all_items.append(i)

        return all_items
