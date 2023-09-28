from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..dependencies import get_item_service
from ..service.iitem_service import IItemService
from ..dto.item_dto import ItemCreateDTO, ItemUpdateDTO, ItemDTO

router = APIRouter()

class ItemController:
    def __init__(self, service: IItemService = Depends(get_item_service)):
        self.service = service

    @router.post("/", response_model=ItemDTO)
    async def create_item(self, item_create_dto: ItemCreateDTO):
        return self.service.create_item(item_create_dto)

    @router.get("/{item_id}", response_model=ItemDTO)
    async def read_item(self, item_id: int):
        return self.service.get_item(item_id)

    @router.get("/", response_model=List[ItemDTO])
    async def read_items(self, skip: int = 0, limit: int = 10):
        return self.service.get_items(skip=skip, limit=limit)

    @router.put("/{item_id}", response_model=ItemDTO)
    async def update_item(self, item_id: int, item_update_dto: ItemUpdateDTO):
        return self.service.update_item(item_id, item_update_dto)

controller = ItemController()
router.include_router(controller, tags=["Items"])