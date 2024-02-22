
from pydantic import BaseModel, EmailStr

from .shared.user_type_model import UserType


class AnalyzeCVModel(BaseModel):
    email: EmailStr
    user_type: UserType
