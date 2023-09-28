from abc import ABC, abstractmethod
from typing import List
from ..models.item import Item

class IItemRepository(ABC):
    
    @abstractmethod
    def create(self, item: Item) -> Item:
        pass
    
    @abstractmethod
    def get(self, item_id: int) -> Item:
        pass
    
    @abstractmethod
    def get_all(self, skip: int, limit: int) -> List[Item]:
        pass
    
    @abstractmethod
    def update(self, item_id: int, item: Item) -> Item:
        pass
