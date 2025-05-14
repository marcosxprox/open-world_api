from pydantic import BaseModel
from typing import Optional

class PlayerUpdate(BaseModel):
    level:Optional[int] = 1
    health:Optional[int] = 100
    stamine:Optional[int] = 100