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
        return ItemDTO.from_orm(created_item)
    
    def get_item(self, item_id: int) -> ItemDTO:
        db_item = self.repository.get(item_id)
        return ItemDTO.from_orm(db_item)
    
    def get_items(self) -> List[ItemDTO]:
        db_items = self.repository.get_all()
        return [ItemDTO.from_orm(db_item) for db_item in db_items]

    def update_item(self, item_id: int, item_update_dto: ItemUpdateDTO) -> ItemDTO:
        updated_data = item_update_dto.dict(exclude_unset=True)
        updated_item = self.repository.update(item_id, updated_data)
        return ItemDTO.from_orm(updated_item)
    
    def delete_item(self, item_id: int):
        self.repository.delete(item_id)