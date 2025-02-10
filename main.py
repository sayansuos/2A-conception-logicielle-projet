import os

from dotenv import load_dotenv

from app.service.champion_service import ChampionService

# Charger le fichier principal
load_dotenv()

# Charge un fichier local si présent
local_env_path = ".env.local"
if os.path.exists(local_env_path):
    load_dotenv(dotenv_path=local_env_path, override=True)


# test23'4
def afficher_var_env():
    for key in os.environ:
        value = os.getenv(key)
        mots_interdits = [
            "password",
            "pwd",
            "jeton",
            "token",
            "secret",
            "key",
            "cle",
            "mdp",
            "motdepasse",
        ]
        for mot in mots_interdits:
            if mot.upper() in key:
                value = "****"
        print(f"{key} : {value}")


# afficher_var_env()

if __name__ == "__main__":
    champ_list = ChampionService().get_all_champs()
    print(champ_list[0])
