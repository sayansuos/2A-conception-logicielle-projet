import app.config.charge_environnement as config
from app.service.champion_service import ChampionService
from app.service.user_service import UserService

if __name__ == "__main__":
    config.load_dotenv()
    UserService().create("pseudo_test", "pwd_test")
    champ_list = ChampionService().get_all_champs()
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

    print(
        ChampionService().get_role(
            ChampionService().get_champ_by_name("Warwick")
        )
    )
    print(
        ChampionService().get_playrate(
            ChampionService().get_champ_by_name("warwick")
        )
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
    print(ChampionService().get_champ_by_name("garen").tags)
    print(ChampionService().get_champ_by_name("Lissandra").info)
    print(ChampionService().get_champ_by_name("MAokai").tags)
    print(ChampionService().get_champ_by_name("Yuumi").tags)
    print(
        ChampionService().get_type_damages(
            ChampionService().get_champ_by_name("smolder")
        )
    )

    best_champ = ChampionService().best_champs(
        role="TOP",
        teammates=[
            ChampionService().get_champ_by_name("Syndra"),
            ChampionService().get_champ_by_name("Evelynn"),
            ChampionService().get_champ_by_name("Caitlyn"),
            ChampionService().get_champ_by_name("Janna"),
        ],
        ennemies=[ChampionService().get_champ_by_name("Darius")],
    )

    for element in best_champ:
        print(element)

    print(
        ChampionService().best_classes_against(
            ChampionService().get_champ_by_name("Zed")
        )
    )
