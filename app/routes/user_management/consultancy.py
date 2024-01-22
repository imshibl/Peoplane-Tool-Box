from fastapi import APIRouter, HTTPException
from pydantic import EmailStr

from app.utils.error_responses import APIErrorResponses

from ...firebase.firebase_helper import FirebaseHelper
from ...models.consultancy_model import ConsultancyUserModel

router = APIRouter(prefix="/consultancy")


@router.post("/add-consultancy", tags=["Consultancy User Management"])
async def add_consultancy(consultancy: ConsultancyUserModel):
    if FirebaseHelper.consultancy_exists(consultancy.email):
        raise HTTPException(
            status_code=409,
            detail={
                "message": "Consultancy with this email already exists",
                "data": consultancy.model_dump(exclude_defaults=True),
            },
        )

    if consultancy.username is None or consultancy.email is None:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Consultancy Username/Email cannot be empty.",
                "data": None,
            },
        )
    FirebaseHelper.consultants_ref.add(consultancy.model_dump())
    return {
        "message": "Consultancy added successfully",
        "data": consultancy.model_dump(),
    }


@router.get("/get-consultancy", tags=["Consultancy User Management"])
async def get_consultancy(consultancy_email: EmailStr):
    isConsultancyAvailable = FirebaseHelper.consultancy_exists(consultancy_email)

    if not isConsultancyAvailable:
        raise HTTPException(
            status_code=404,
            detail={
                "message": "Consultancy not found",
                "data": None,
            },
        )

    consultancy = FirebaseHelper.get_consultancy(consultancy_email)
    return {
        "message": "Consultancy found",
        "data": consultancy[0].to_dict(),
    }


@router.patch("/update-consultancy", tags=["Consultancy User Management"])
async def update_consultancy(
    consultancy: ConsultancyUserModel, consultancy_email: EmailStr
):
    consultancy_data = consultancy.model_dump(exclude_defaults=True, exclude_none=True)

    FirebaseHelper.update_consultancy(consultancy_email, consultancy_data)
    return {
        "message": "Consultancy data updated successfully",
        "data": consultancy_data,
    }


@router.delete("/delete-consultancy", tags=["Consultancy User Management"])
async def delete_consultancy(consultancy_email: EmailStr):
    FirebaseHelper.delete_consultancy(consultancy_email)
    return {
        "message": "Consultancy associated with {} deleted successfully".format(
            consultancy_email
        ),
        "data": None,
    }
