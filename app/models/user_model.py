from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    username: str | None = Field(default=None)
    email: EmailStr | None = Field(default=None)
    total_quality_checks_performed: int | None = Field(default=0)
    total_plagiarism_checks_performed: int | None = Field(default=0)
    total_resume_checks_performed: int | None = Field(default=0)
