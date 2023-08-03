from pydantic import BaseModel
from typing import Dict

class PageInfo(BaseModel):
    page_info: Dict[str, str]