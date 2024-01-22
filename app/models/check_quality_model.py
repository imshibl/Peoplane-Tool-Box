from pydantic import BaseModel, Field


class CheckQualityModel(BaseModel):
    sop: str
    is_premium_user: bool | None = Field(default=False)
