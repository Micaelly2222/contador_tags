from pydantic import BaseModel

class HTMLRequest(BaseModel):
    html_name: str
    html_code: str