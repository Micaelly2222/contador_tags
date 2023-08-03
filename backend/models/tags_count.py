from pydantic import BaseModel
from typing import Dict

class TagsCount(BaseModel):
    tags_count: Dict[str, int]