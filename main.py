import app.config.charge_environnement as config
from app.config.reset_db import ResetDB
from app.service.build_service import BuildService
from app.service.champion_service import ChampionService
from app.service.item_service import ItemService
from app.service.user_service import UserService

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
    UserService().create(pseudo="pseudo", pwd="mdp")
    UserService().create(pseudo="pseudobis", pwd="mdpbis")
    UserService().print_all_users()
    print(UserService().get_by_pseudo(pseudo="pseudobis"))
    UserService().login(pseudo="pseudo", pwd="mdp")
    UserService().delete_where_pseudo(pseudo="pseudobis")
    UserService().print_all_users()
    ChampionService().create_all_champs()
    ItemService().create_all_items()
    print(ChampionService().get_all_champs_by_role("MID")[0])
    print(
        ChampionService().available_champs_by_role(
            role="BOT",
            picks=[
                "Ahri",
                "Lulu",
                "Camille",
                "Udyr",
                "Aphelios",
                "Corki",
                "Leona",
            ],
            bans=[
                "Caitlyn",
                "Blitzcrank",
                "Draven",
                "Jayce",
                "Mordekaiser",
                "Sylas",
                "Kayn",
                "Lee Sin",
                "Master Yi",
                "Darius",
            ],
        )[0]
    )
    print(ChampionService().available_champs_by_role("JGL")[0])
    ChampionService().get_champ_by_name("ahri").show_image()
    ItemService().get_item_by_name("heartsteel").show_image()
    champion = champ_list[5]
    item1 = ItemService().get_all_items()[0]
    item2 = ItemService().get_all_items()[1]
    item3 = ItemService().get_all_items()[2]
    item4 = ItemService().get_all_items()[3]
    item5 = ItemService().get_all_items()[4]
    build = BuildService().create(
        champion=champion,
        item1=item1,
        item2=item2,
        item3=item3,
        item4=item4,
        item5=item5,
    )
    print(build)
