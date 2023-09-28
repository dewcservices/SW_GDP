from typing import List
from ..dto.item_dto import ItemCreateDTO, ItemUpdateDTO, ItemDTO

class IItemService:
    def create_item(self, item_create_dto: ItemCreateDTO) -> ItemDTO:
        raise NotImplementedError

    def get_item(self, item_id: int) -> ItemDTO:
        raise NotImplementedError

    def get_items(self) -> List[ItemDTO]:
        raise NotImplementedError

    def update_item(self, item_id: int, item_update_dto: ItemUpdateDTO) -> ItemDTO:
        raise NotImplementedError

    def delete_item(self, item_id: int):
        raise NotImplementedError