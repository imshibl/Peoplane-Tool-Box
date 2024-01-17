from pydantic import BaseModel, Field


class CheckQualityModel(BaseModel):
    sop: str
    isPremiumUser: bool = Field(default=False)
