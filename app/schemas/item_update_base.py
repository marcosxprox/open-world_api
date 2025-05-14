from pydantic import BaseModel
from typing import Optional

class ItemUpdate(BaseModel):
    name: Optional[str] = input("nome item:")
    description: Optional[str] = input("descricao item:")
    quantify: Optional[int] = int(input("quantidade item:"))