from pydantic import BaseModel, Field


class CheckSOPQualityModel(BaseModel):
    sop: str
    home_country: str | None = Field(default="India")
    is_premium_user: bool | None = Field(default=False)
