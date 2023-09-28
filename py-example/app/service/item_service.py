from typing import List
from fastapi import HTTPException
from ..repository.iitem_repository import IItemRepository
from ..dto.item_dto import ItemCreateDTO, ItemUpdateDTO, ItemDTO
from ..models.item import Item as ItemDB
from .iitem_service import IItemService


class ItemService(IItemService):
    def __init__(self, repository: IItemRepository):
        self.repository = repository
    
    def create_item(self, item_create_dto: ItemCreateDTO) -> ItemDTO:
        db_item = ItemDB(**item_create_dto.dict())
        created_item = self.repository.create(db_item)
        return ItemDTO(**created_item.dict())
    
    def get_item(self, item_id: int) -> ItemDTO:
        db_item = self.repository.get(item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return ItemDTO(**db_item.dict())
    
    def get_items(self, skip: int = 0, limit: int = 10) -> List[ItemDTO]:
        db_items = self.repository.get_all(skip, limit)
        return [ItemDTO(**db_item.dict()) for db_item in db_items]

    def update_item(self, item_id: int, item_update_dto: ItemUpdateDTO) -> ItemDTO:
        db_item = self.repository.get(item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        updated_item = self.repository.update(item_id, ItemDB(**item_update_dto.dict()))
        return ItemDTO(**updated_item.dict())
    
    def delete_item(self, item_id: int):
        db_item = self.repository.get(item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        self.repository.delete(item_id)