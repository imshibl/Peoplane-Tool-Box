from enum import Enum

from pydantic import BaseModel, EmailStr


class Tools(str, Enum):
    plagiarism_checker = "plagiarism checker"
    resume_analyzer = "resume analyzer"
    quality_checker_for_university = "quality checker for university"
    quality_checker_for_visa = "quality checker for visa"


class UserType(str, Enum):
    user = "user"
    consultancy = "consultancy"


class FeedbackAndRatingModel(BaseModel):
    email: EmailStr
    user_type: UserType
    feedback: str
    rating: float
    tool: Tools
