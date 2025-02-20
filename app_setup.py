import app.config.charge_environnement as config
from app.config.reset_db import ResetDB
from app.service.build_service import BuildService
from app.service.champion_service import ChampionService
from app.service.item_service import ItemService
from app.service.user_service import UserService

if __name__ == "__main__":
    config.load_dotenv()
    # Database initialisation
    ResetDB().init_db()

    # Database filling with champs and items
    ChampionService().create_all_champs()
    ItemService().create_all_items()

    # Users simulation
    user1 = UserService().create(pseudo="lilian", pwd="lilianlargitte")
    user2 = UserService().create(pseudo="raphael", pwd="raphaelmangatal")
    user3 = UserService().create(pseudo="sayan", pwd="sayansuos")

    # Builds simulation
    build1 = BuildService().create(
        champion=ChampionService().get_champ_by_name("Nasus"),
        item1=ItemService().get_item_by_name("Trinity Force"),
        item2=ItemService().get_item_by_name("Ionian Boots of Lucidity"),
        item3=ItemService().get_item_by_name("Frozen Heart"),
        item4=ItemService().get_item_by_name("Spirit Visage"),
        item5=ItemService().get_item_by_name("Sterak's Gage"),
    )
    build2 = BuildService().create(
        champion=ChampionService().get_champ_by_name("Smolder"),
        item1=ItemService().get_item_by_name("Spectral Cutlass"),
        item2=ItemService().get_item_by_name("Ionian Boots of Lucidity"),
        item3=ItemService().get_item_by_name("Spear of Shojin"),
        item4=ItemService().get_item_by_name("Lord Dominik's Regards"),
        item5=ItemService().get_item_by_name("Bloodthirster"),
    )
    build3 = BuildService().create(
        champion=ChampionService().get_champ_by_name("Ahri"),
        item1=ItemService().get_item_by_name("Malignance"),
        item2=ItemService().get_item_by_name("Sorcerer's Shoes"),
        item3=ItemService().get_item_by_name("Shadowflame"),
        item4=ItemService().get_item_by_name("Void Staff"),
        item5=ItemService().get_item_by_name("Rabadon's Deathcap"),
    )

    # Users' builds simulation
    UserService().add_build(user=user1, build=build1)
    UserService().add_build(user=user2, build=build2)
    UserService().add_build(user=user3, build=build3)
