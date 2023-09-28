from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.item import Item
from .iitem_repository import IItemRepository

class ItemRepository(IItemRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, item: Item) -> Item:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def find(self, item_id: int) -> Optional[Item]:
        return self.db.query(Item).filter(Item.id == item_id).first()
    
    def get(self, item_id: int) -> Item:
        item_db = self.find(item_id)
        if item_db:
            return item_db    
        raise HTTPException(status_code=404, detail="Item not found")

    
    def get_all(self) -> List[Item]:
        return self.db.query(Item).all()
    
    def update(self, item_id: int, updated_data: dict) -> Item:
        db_item = self.get(item_id)

        # Update the SQLAlchemy model instance with data from the Pydantic model
        for key, value in updated_data.items():
            setattr(db_item, key, value)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
    
    def delete(self, item_id: int):
        db_item = self.get(item_id)
        if db_item:
            self.db.delete(db_item)
            self.db.commit()