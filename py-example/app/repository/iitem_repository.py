from abc import ABC, abstractmethod
from typing import List, Optional
from ..models.item import Item

class IItemRepository(ABC):
    
    @abstractmethod
    def create(self, item: Item) -> Item:
        pass
    
    @abstractmethod
    def get(self, item_id: int) -> Item:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Item]:
        pass
    
    @abstractmethod
    def update(self, item_id: int, updated_data: dict) -> Item:
        pass
