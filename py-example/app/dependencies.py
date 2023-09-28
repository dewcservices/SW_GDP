from fastapi import Depends
# from sqlalchemy.orm import Session
# from .database import SessionLocal
# from .repository.item_repository import ItemRepository
# from .repository.iitem_repository import IItemRepository
from .service.item_service_mock import ItemServiceMock
from .service.iitem_service import IItemService

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# def get_item_repository(db: Session = Depends(get_db)) -> IItemRepository:
#     return ItemRepository(db)

# def get_item_service(repository: IItemRepository = Depends(get_item_repository)) -> IItemService:
#     return ItemService(repository)

def get_item_service() -> IItemService:
    return ItemServiceMock()