import unittest
from unittest.mock import patch

from app.dto.item_dto import ItemDTO
from app.fastapi.item_router import get_item_by_id_or_name
from app.models.item import Item


class TestItemRouter(unittest.IsolatedAsyncioTestCase):

    @patch("app.fastapi.item_router.get_item_by_id_or_name")
    @patch("app.service.item_service.ItemService.get_item_by_id")
    @patch("app.service.item_service.ItemService.get_item_by_name")
    async def test_get_item_by_id_or_name(
        self,
        mock_get_item_by_name,
        mock_get_item_by_id,
        mock_get_item_by_id_or_name,
    ):

        mock_get_item_by_id_or_name.return_value = ItemDTO(
            name="Item 1",
            item_id=1,
            description="This is item 1",
            tags=["tag1", "tag2"],
            stats={"stat1": 10},
            image="image_path_1",
        )

        mock_get_item_by_id.return_value = Item(
            name="Item 1",
            item_id=1,
            description="This is item 1",
            tags=["tag1", "tag2"],
            stats={"stat1": 10},
            image="image_path_1",
        )

        mock_get_item_by_name.return_value = Item(
            name="Item 1",
            item_id=1,
            description="This is item 1",
            tags=["tag1", "tag2"],
            stats={"stat1": 10},
            image="image_path_1",
        )

        result1 = await get_item_by_id_or_name("1")
        result2 = await get_item_by_id_or_name("Item 1")

        self.assertEqual(result1.name, "Item 1")
        self.assertEqual(result1.item_id, 1)
        self.assertEqual(result1.description, "This is item 1")
        self.assertEqual(result1.tags, ["tag1", "tag2"])
        self.assertEqual(result1.stats, {"stat1": 10})
        self.assertEqual(result1.image, "image_path_1")

        self.assertEqual(result2.name, "Item 1")
        self.assertEqual(result2.item_id, 1)
        self.assertEqual(result2.description, "This is item 1")
        self.assertEqual(result2.tags, ["tag1", "tag2"])
        self.assertEqual(result2.stats, {"stat1": 10})
        self.assertEqual(result2.image, "image_path_1")
