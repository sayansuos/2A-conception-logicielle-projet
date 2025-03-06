""" Test champion_router """

import unittest
from unittest.mock import patch

from app.dto.champion_dto import ChampionDTO
from app.fastapi.champion_router import get_champion_by_id_or_name
from app.models.champion import Champion


class TestItemRouter(unittest.IsolatedAsyncioTestCase):

    @patch("app.fastapi.champion_router.get_champion_by_id_or_name")
    @patch("app.service.champion_service.ChampionService.get_champ_by_id")
    @patch("app.service.champion_service.ChampionService.get_champ_by_name")
    async def test_get_champion_by_id_or_name(
        self,
        mock_get_champ_by_name,
        mock_get_champ_by_id,
        mock_get_champion_by_id_or_name,
    ):
        """Tests retrieving an Champion by either ID or name."""

        mock_get_champion_by_id_or_name.return_value = ChampionDTO(
            name="Champion 1",
            champ_id=1,
            blurb="This is champion 1",
            tags=["tag1", "tag2"],
            stats={"stat1": 10},
            info={"info 1 key": "info 1 value"},
            image="image_path_1",
        )

        mock_get_champ_by_id.return_value = Champion(
            name="Champion 1",
            champ_id=1,
            blurb="This is champion 1",
            tags=["tag1", "tag2"],
            stats={"stat1": 10},
            info={"info 1 key": "info 1 value"},
            image="image_path_1",
        )

        mock_get_champ_by_name.return_value = Champion(
            name="Champion 1",
            champ_id=1,
            blurb="This is champion 1",
            tags=["tag1", "tag2"],
            stats={"stat1": 10},
            info={"info 1 key": "info 1 value"},
            image="image_path_1",
        )

        result1 = await get_champion_by_id_or_name("1")
        result2 = await get_champion_by_id_or_name("Item 2")

        self.assertEqual(result1.name, "Champion 1")
        self.assertEqual(result1.champ_id, 1)
        self.assertEqual(result1.blurb, "This is champion 1")
        self.assertEqual(result1.tags, ["tag1", "tag2"])
        self.assertEqual(result1.stats, {"stat1": 10})
        self.assertEqual(result1.info, {"info 1 key": "info 1 value"})
        self.assertEqual(result1.image, "image_path_1")

        self.assertEqual(result2.name, "Champion 1")
        self.assertEqual(result2.champ_id, 1)
        self.assertEqual(result2.blurb, "This is champion 1")
        self.assertEqual(result2.tags, ["tag1", "tag2"])
        self.assertEqual(result2.stats, {"stat1": 10})
        self.assertEqual(result2.info, {"info 1 key": "info 1 value"})
        self.assertEqual(result2.image, "image_path_1")
