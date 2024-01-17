from fastapi import APIRouter, HTTPException

from app.utils.error_responses import APIErrorResponses

from ...firebase.firebase_helper import FirebaseHelper
from ...models.user_model import (
    ConsultancyChildUserModel,
    ConsultancyUserModel,
    UserModel,
)

router = APIRouter(
    prefix="/peoplaneai",
)


@router.post("/add-consultancy-user", tags=["consultancy user management"])
async def add_user(user: ConsultancyUserModel):
    if FirebaseHelper.consultancy_exists(user.email):
        raise HTTPException(
            status_code=409,
            detail={
                "message": "Consultancy with this email already exists",
                "data": user.model_dump(),
            },
        )
    FirebaseHelper.consultants_ref.add(user.model_dump())
    return {
        "message": "Consultancy added successfully",
        "data": user.model_dump(),
    }


@router.post("/add-consultancy-child-user", tags=["consultancy user management"])
async def add_consultancy_child_user(data: ConsultancyChildUserModel):
    FirebaseHelper.add_consultancy_child_user(data.email, data.model_dump())
    return {
        "message": "Consultancy added successfully",
        "data": data.model_dump(),
    }
