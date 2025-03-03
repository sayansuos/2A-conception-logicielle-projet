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
        This method gives a champ by its name.
        """
        if not isinstance(champ_name, str):
            return TypeError("The champ's name should be an str instance.")

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

    def create_role(self, champ: Champion) -> list:
        """
        This method gives the role of a champ.
        """
        playrate = self.get_playrate(champ)
        playrate = list(playrate.items())
        playrate.remove(playrate[0])
        playrate = sorted(playrate, key=lambda x: x[1], reverse=True)

        role_champ = []

        for element in playrate:
            role, percentage = element[0], element[1]
            if percentage != 0:
                role_champ.append(role)

        return role_champ

    def get_role(self, champion: Champion) -> list:
        """
        This methods gives the roles saved in the db for a champion.
        """
        if not isinstance(champion, Champion):
            return TypeError("The champion should be a Champion instance.")

        return ChampionDao().read_role(champion=champion)

    def get_type_damages(self, champ: Champion) -> str:
        """
        This method gives the type of damages a certain champ mostly deals.
        """
        if champ.info["attack"] > champ.info["magic"]:
            return "Physical"
        elif champ.info["attack"] < champ.info["magic"]:
            return "Magical"
        return "Mixed"

    def get_type_damages_team(self, team: list) -> str:
        """
        This method gives the type of damages an entire team mostly deals.
        """
        physical = 0
        magical = 0
        for champ in team:
            if self.get_type_damages(champ) == "Physical":
                physical += 1
            elif self.get_type_damages(champ) == "Magical":
                magical += 1
        if physical > magical:
            return "Physical"
        elif physical < magical:
            return "Magical"
        return "Mixed"

    def get_all_champs_by_role(self, role: str) -> list:
        """
        This method gives the list of all champions according to a given role.
        """
        if role not in ["TOP", "JGL", "MID", "BOT", "SUPP"]:
            raise ValueError("This role doesn't exist.")

        playable_champs_for_role = []

        champs_list = self.get_all_champs()
        for champ in champs_list:
            if role in self.get_role(champion=champ):
                playable_champs_for_role.append(champ)

        return playable_champs_for_role

    def available_champs_by_role(
        self, role: str, picks: list = None, bans: list = None
    ) -> list:
        """
        This method gives the list of all available champions someone
        can choose to play according to their role.
        """
        if picks is None:
            picks = []

        if bans is None:
            bans = []

        available_champs_for_role = self.get_all_champs_by_role(role)

        unplayable_champs = picks + bans

        for unplayable in unplayable_champs:
            for champ in available_champs_for_role:
                if unplayable.name == champ.name:
                    available_champs_for_role.remove(champ)

        return available_champs_for_role

    def get_matchup(self, role: str, ennemies: list) -> Champion:
        """
        This method allows to identify the direct opponent of a player
        according to their role.
        """
        possible_opponent = []

        for champ in ennemies:
            list_role = self.get_role(champ)
            for role_champ in list_role:
                if role_champ == role:
                    possible_opponent.append(champ)

        if len(possible_opponent) == 0:
            return "Your opponent didn't pick already."

        return possible_opponent

    def is_good_against(self, classe: str) -> list:
        """
        This method gives the list of classes that counters another one.
        """
        if classe not in [
            "Tank",
            "Assassin",
            "Marksman",
            "Mage",
            "Support",
            "Fighter",
        ]:
            raise ValueError("Incorrect class given.")

        if classe == "Tank":
            return ["Marksman", "Fighter"]

        elif classe == "Assassin":
            return ["Tank", "Support", "Fighter"]

        elif classe == "Marksman":
            return ["Assassin", "Mage", "Marksman"]

        elif classe == "Mage":
            return ["Tank", "Assassin"]

        elif classe == "Fighter":
            return ["Fighter", "Marksman"]

        elif classe == "Support":
            return ["Fighter"]

    def best_classes_against(self, champ: Champion) -> list:
        """
        This method gives the classes that counter a given champ.
        """
        best_class = []
        class_champ = champ.tags

        for classe in class_champ:

            counter_classes = self.is_good_against(classe)

            for counter_class in counter_classes:
                if counter_class not in best_class:

                    best_class.append(counter_class)

        return best_class

    def best_champs(
        self,
        role: str,
        teammates: list = None,
        ennemies: list = None,
        bans: list = None,
    ) -> list:
        """
        This method gives a list of the 'best' champs to play according to a
        given situation (the role you play, your team and the ennemy team).
        """
        if teammates is None:
            teammates = []

        if ennemies is None:
            ennemies = []

        picks = teammates + ennemies

        available_champs = self.available_champs_by_role(role, picks, bans)

        type_damage_allies = self.get_type_damages_team(teammates)

        for champ in available_champs:
            if self.get_type_damages(champ) == type_damage_allies:
                available_champs.remove(champ)

        direct_opponent = self.get_matchup(role, ennemies)

        if isinstance(direct_opponent, str):
            # The opponent did not pick yet.
            return available_champs

        else:
            # You know who is your opponent.
            best_classes_against = self.best_classes_against(
                champ=direct_opponent[0]
            )

            for champ in available_champs:
                est_dans = False
                for classe in champ.tags:
                    if classe in best_classes_against:
                        est_dans = True
                if est_dans is False:
                    available_champs.remove(champ)

            return available_champs

    def create_all_champs(self) -> bool:
        """
        This method add all the champions to the database.
        """
        champs_list = self.get_all_champs()
        all_created = True
        for champ in champs_list:
            role = self.create_role(champ=champ)
            role = ", ".join(role)
            created = ChampionDao().create(champion=champ, role=role)
            if not created:
                all_created = False

        return all_created
