import app.config.charge_environnement as config
from app.service.champion_service import ChampionService

if __name__ == "__main__":
    config.load_dotenv()
    champ_list = ChampionService().get_all_champs()
    print(champ_list[0])
    print(ChampionService().get_champ_by_name("ahri"))
    print(ChampionService().get_champ_by_id(201))
    print(ChampionService().get_role(champ_list[0]))
