import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests


class Item:
    """
    Représente un item avec ses détails.

    - **name**: Le nom du champion.
    - **title**: Le titre du champion.
    - **blurb**: Une description du champion.
    - **tags**: Une liste de tags associés au champion.
    - **stats** : Un dictionnaire des statistiques du champion
    -- **info** : Un dictionnaire des informations sur les champions.
    - **image** : Une image du champion.
    """

    def __init__(
        self,
        name: str,
        item_id: int,
        description: str,
        tags: list[str],
        stats: dict,
        image: str,
    ):
        """
        Builder
        """
        self.name = name
        self.id = item_id
        self.tags = tags
        self.stats = stats
        self.description = description
        self.image = image

    def __str__(self):
        return f"[{self.id}] {self.name} \n{self.stats}"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def show_image(self):
        """
        This methods shows the item's image.
        """
        response = requests.get(self.image, timeout=None)  # Télécharge l'image
        img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        cv2.imshow("Image", img)  # Affiche l'image
        cv2.waitKey(0)  # Attend une touche pour fermer
        cv2.destroyAllWindows()  # Ferme la fenêtre

    def show_image_plt(self):
        """
        This methods shows the item's image using matplotlib.
        """
        response = requests.get(self.image, timeout=None)  # Télécharge l'image
        img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(img)
        plt.axis("off")
        plt.show()
