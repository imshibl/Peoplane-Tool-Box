from pydantic import BaseModel, EmailStr

from app.models.shared.sop_type_model import SopType

from .shared.user_type_model import UserType


class CheckPlagiarismModel(BaseModel):
    content: str
    email: EmailStr
    sop_type: SopType
    user_type: UserType
