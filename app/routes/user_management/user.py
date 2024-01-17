from fastapi import APIRouter, HTTPException
from pydantic import EmailStr

from app.utils.error_responses import APIErrorResponses

from ...firebase.firebase_helper import FirebaseHelper
from ...models.user_model import UserModel

router = APIRouter(
    prefix="/peoplaneai",
)


@router.post("/add-user", tags=["user management"])
async def add_user(user: UserModel):
    if FirebaseHelper.user_exists(user.email):
        raise HTTPException(
            status_code=409,
            detail={
                "message": "User with this email already exists",
                "data": user.model_dump(),
            },
        )
    FirebaseHelper.users_ref.add(user.model_dump())
    return {
        "message": "User added successfully",
        "data": user.model_dump(),
    }


@router.get("/get-user", tags=["user management"])
async def get_user(email: EmailStr):
    isUserAvailable = FirebaseHelper.user_exists(email)

    if not isUserAvailable:
        raise HTTPException(
            status_code=404, detail=APIErrorResponses.userNotFoundErrorResponse
        )

    user = FirebaseHelper.get_user(email)
    return {
        "message": "User found",
        "user": user[0].to_dict(),
    }


@router.patch("/update-user", tags=["user management"])
async def update_user(user: UserModel):
    isUserAvailable = FirebaseHelper.user_exists(user.email)

    if not isUserAvailable:
        raise HTTPException(
            status_code=404, detail=APIErrorResponses.userNotFoundErrorResponse
        )
    user = FirebaseHelper.update_user(user.email, user.model_dump())
    return {
        "message": "User data updated successfully",
        "user": user[0].to_dict(),
    }


@router.delete("/delete-user", tags=["user management"])
async def delete_user(email: EmailStr):
    isUserAvailable = FirebaseHelper.user_exists(email)

    if not isUserAvailable:
        raise HTTPException(
            status_code=404, detail=APIErrorResponses.userNotFoundErrorResponse
        )
    FirebaseHelper.delete_user(email)
    return {
        "message": "Account associated with {} deleted successfully".format(email),
    }
