from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    username: str
    email: EmailStr


class ConsultancyUserModel(BaseModel):
    username: str
    email: EmailStr


class ConsultancyChildUserModel(ConsultancyUserModel):
    sub_user_email: EmailStr
    quality_checks_perfomed: int
