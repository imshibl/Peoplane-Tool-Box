from enum import Enum

from pydantic import BaseModel, EmailStr


class ContentType(str, Enum):
    university = "university"
    visa = "visa"


class CheckPlagiarismModel(BaseModel):
    content: str
    owner_email: EmailStr
    type: ContentType
