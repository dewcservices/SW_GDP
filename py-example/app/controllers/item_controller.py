from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..dependencies import get_item_service
from ..service.iitem_service import IItemService
from ..dto.item_dto import ItemCreateDTO, ItemUpdateDTO, ItemDTO

router = APIRouter(prefix="/api/items")

@router.post("/", response_model=ItemDTO)
async def create_item(item_create_dto: ItemCreateDTO, service: IItemService = Depends(get_item_service)):
        return service.create_item(item_create_dto)

@router.get("/{item_id}", response_model=ItemDTO)
async def read_item(item_id: int, service: IItemService = Depends(get_item_service)):
    return service.get_item(item_id)

@router.get("/", response_model=List[ItemDTO])
async def read_items(service: IItemService = Depends(get_item_service)):
    return service.get_items()

@router.put("/{item_id}", response_model=ItemDTO)
async def update_item(item_id: int, item_update_dto: ItemUpdateDTO, service: IItemService = Depends(get_item_service)):
    return service.update_item(item_id, item_update_dto)
