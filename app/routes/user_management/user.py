from fastapi import APIRouter, HTTPException
from pydantic import EmailStr

from app.utils.error_responses import APIErrorResponses

from ...firebase.firebase_helper import FirebaseHelper
from ...models.user_model import UserModel

router = APIRouter(prefix="/user")


@router.post("/add-user", tags=["User Management"])
async def add_user(user: UserModel):
    if FirebaseHelper.user_exists(user.email):
        raise HTTPException(
            status_code=409,
            detail={
                "message": "User with this email already exists",
                "data": user.model_dump(),
            },
        )
    if user.username is None or user.email is None:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Username/Email cannot be empty.",
                "data": None,
            },
        )

    FirebaseHelper.users_ref.add(user.model_dump())
    return {
        "message": "User added successfully",
        "data": user.model_dump(),
    }


@router.get("/get-user", tags=["User Management"])
async def get_user(email: EmailStr):
    isUserAvailable = FirebaseHelper.user_exists(email)

    if not isUserAvailable:
        raise HTTPException(
            status_code=404, detail=APIErrorResponses.userNotFoundErrorResponse
        )

    user = FirebaseHelper.get_user(email)
    return {
        "message": "User found",
        "data": user[0].to_dict(),
    }


@router.patch("/update-user", tags=["User Management"])
async def update_user(user: UserModel, email: EmailStr):
    user_data = user.model_dump(exclude_defaults=True, exclude_none=True)
    user = FirebaseHelper.update_user(email, user_data)
    return {
        "message": "User data updated successfully",
        "data": user_data,
    }


@router.delete("/delete-user", tags=["User Management"])
async def delete_user(email: EmailStr):
    isUserAvailable = FirebaseHelper.user_exists(email)

    FirebaseHelper.delete_user(email)
    return {
        "message": "Account associated with {} deleted successfully".format(email),
        "data": None,
    }
