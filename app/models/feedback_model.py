from pydantic import BaseModel, EmailStr


class FeedbackAndRatingModel(BaseModel):
    user_email: EmailStr
    feedback: str
    rating: float
