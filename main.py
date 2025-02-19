import app.config.charge_environnement as config
from app.config.reset_db import ResetDB
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
    # UserService().login(pseudo="pseudo", pwd="mdp")
    # UserService().delete_where_pseudo(pseudo="pseudobis")
    # UserService().print_all_users()
    # ChampionService().create_all_champs()
    # ItemService().create_all_items()
    # print(ChampionService().get_all_champs_by_role("MID")[0])
    # print(
    #     ChampionService().available_champs_by_role(
    #         role="BOT",
    #         picks=[
    #             "Ahri",
    #             "Lulu",
    #             "Camille",
    #             "Udyr",
    #             "Aphelios",
    #             "Corki",
    #             "Leona"
    #         ],
    #         bans=[
    #             "Caitlyn",
    #             "Blitzcrank",
    #             "Draven",
    #             "Jayce",
    #             "Mordekaiser",
    #             "Sylas",
    #             "Kayn",
    #             "Lee Sin",
    #             "Master Yi",
    #             "Darius",
    #         ],
    #     )[0]
    # )
    # print(ChampionService().available_champs_by_role("JGL")[0])
    print(ChampionService().get_role(ChampionService().get_champ_by_name("Warwick")))
    print(
        ChampionService().get_playrate(ChampionService().get_champ_by_name("warwick"))
    )

    print(
        ChampionService()
        .get_matchup(
            role="BOT",
            ennemies=[
                ChampionService().get_champ_by_name("Darius"),
                ChampionService().get_champ_by_name("Lee Sin"),
                ChampionService().get_champ_by_name("Zed"),
                ChampionService().get_champ_by_name("Aphelios"),
                ChampionService().get_champ_by_name("Janna"),
            ],
        )[0]
        .name
    )
