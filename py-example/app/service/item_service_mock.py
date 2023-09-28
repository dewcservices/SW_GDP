from typing import List, Optional
from ..models.item import Item, ItemCreate, ItemUpdate
from ..service.iitem_service import IItemService

class ItemServiceMock(IItemService):
    def __init__(self):
        # Creating some hardcoded items
        self.items = [
            Item(id=1, name="Item One", description="This is item one."),
            Item(id=2, name="Item Two", description="This is item two."),
        ]
    
    def create_item(self, item_create: ItemCreate) -> Item:
        # Creating a new item with id=3
        new_item = Item(id=3, name=item_create.name, description=item_create.description)
        return new_item
    
    def get_item(self, item_id: int) -> Optional[Item]:
        # Returning a hardcoded item if it exists in the list, else None
        item = next((item for item in self.items if item.id == item_id), None)
        return item
    
    def get_items(self, skip: int = 0, limit: int = 10) -> List[Item]:
        # Returning the list of hardcoded items
        return self.items[skip : skip + limit]
    
    def update_item(self, item_id: int, item_update: ItemUpdate) -> Item:
        # Updating the item if it exists and returning it, else returning a default item
        item = next((item for item in self.items if item.id == item_id), None)
        if item:
            item.name = item_update.name or item.name
            item.description = item_update.description or item.description
            return item
        else:
            return Item(id=0, name="Default", description="Default item")
    
    def delete_item(self, item_id: int):
        # Deleting the item if it exists in the hardcoded list
        self.items = [item for item in self.items if item.id != item_id]