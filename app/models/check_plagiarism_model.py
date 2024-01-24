from enum import Enum

from pydantic import BaseModel, EmailStr

from .shared.user_type_model import UserType


class ContentType(str, Enum):
    university = "university"
    visa = "visa"


class CheckPlagiarismModel(BaseModel):
    content: str
    email: EmailStr
    type: ContentType
    user_type: UserType
