from typing import List, Optional
from ..dto.item_dto import ItemCreateDTO, ItemUpdateDTO, ItemDTO
from .iitem_service import IItemService

class ItemServiceMock(IItemService):
    def __init__(self):
        # Creating some hardcoded items
        self.items = [
            ItemDTO(id=1, name="Item One", description="This is item one."),
            ItemDTO(id=2, name="Item Two", description="This is item two."),
        ]
    
    def create_item(self, item_create: ItemCreateDTO) -> ItemDTO:
        # Creating a new item with id=3
        new_item = ItemDTO(id=3, name=item_create.name, description=item_create.description)
        return new_item
    
    def get_item(self, item_id: int) -> ItemDTO:
        # Returning a hardcoded item if it exists in the list, else None
        item = next((item for item in self.items if item.id == item_id), None)
        return item
    
    def get_items(self) -> List[ItemDTO]:
        # Returning the list of hardcoded items
        return self.items
    
    def update_item(self, item_id: int, item_update: ItemUpdateDTO) -> ItemDTO:
        # Updating the item if it exists and returning it, else returning a default item
        item = next((item for item in self.items if item.id == item_id), None)
        if item:
            item.name = item_update.name or item.name
            item.description = item_update.description or item.description
            return item
        else:
            return ItemDTO(id=0, name="Default", description="Default item")
    
    def delete_item(self, item_id: int):
        # Deleting the item if it exists in the hardcoded list
        self.items = [item for item in self.items if item.id != item_id]