from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.item import Item
from .iitem_repository import IItemRepository
from ..database import get_db

class ItemRepository(IItemRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, item: Item) -> Item:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item
    
    def get(self, item_id: int) -> Optional[Item]:
        return self.db.query(Item).filter(Item.id == item_id).first()
    
    def get_all(self, skip: int = 0, limit: int = 10) -> List[Item]:
        return self.db.query(Item).offset(skip).limit(limit).all()
    
    def update(self, item_id: int, item: Item) -> Item:
        db_item = self.db.query(Item).filter(Item.id == item_id).first()
        if db_item:
            for key, value in item.dict().items():
                setattr(db_item, key, value)
            self.db.commit()
            self.db.refresh(db_item)
        return db_item
    
    def delete(self, item_id: int):
        db_item = self.db.query(Item).filter(Item.id == item_id).first()
        if db_item:
            self.db.delete(db_item)
            self.db.commit()