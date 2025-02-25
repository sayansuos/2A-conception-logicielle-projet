import os

from dotenv import load_dotenv

# Charger le fichier principal
load_dotenv()

# Charge un fichier local si présent
LOCAL_ENV_PATH = ".env.local"
if os.path.exists(LOCAL_ENV_PATH):
    load_dotenv(dotenv_path=LOCAL_ENV_PATH, override=True)


def afficher_var_env():
    """
    Cette fonction charge toutes les variables d'environnements.
    """
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
