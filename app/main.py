import os

from dotenv import load_dotenv

# Charger le fichier principal
load_dotenv()

# Charge un fichier local si présent
local_env_path = ".env.local"
if os.path.exists(local_env_path):
    load_dotenv(dotenv_path=local_env_path, override=True)


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


afficher_var_env()
