from pydantic import BaseModel


class ItemResponseModel(BaseModel):
    title: str
    description: str
