import app.config.charge_environnement as config
from app.config.reset_db import ResetDB
from app.service.champion_service import ChampionService
from app.service.item_service import ItemService

if __name__ == "__main__":
    config.load_dotenv()
    champ_list = ChampionService().get_all_champs()
    print(champ_list[0])
    print(ChampionService().get_champ_by_name("ahri"))
    print(ChampionService().get_champ_by_id(201))
    print(ChampionService().get_playrate(champ_list[0]))
    print(ItemService().get_all_items()[0])
    ItemService().print_all_items()
    print(ItemService().get_item_by_id(1040))
    print(ItemService().get_item_by_name("heartsteel"))
    ResetDB().init_db()
