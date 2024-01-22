from enum import Enum

from pydantic import BaseModel, EmailStr


class UserType(str, Enum):
    user = "user"
    consultancy = "consultancy"


class AnalyzeCVModel(BaseModel):
    email: EmailStr
    user_type: UserType
