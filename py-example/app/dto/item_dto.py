from pydantic import BaseModel

class ItemCreateDTO(BaseModel):
    name: str
    description: str

class ItemUpdateDTO(BaseModel):
    name: str
    description: str

class ItemDTO(BaseModel):
    id: int
    name: str
    description: str
    
    class Config:
        from_attributes = True

