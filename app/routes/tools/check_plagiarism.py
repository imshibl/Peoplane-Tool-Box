from fastapi import APIRouter, HTTPException

from app.utils.error_responses import APIErrorResponses

from ...features.check_plagiarism.check_plagiarism import check_plagiarism
from ...firebase.firebase_helper import FirebaseHelper
from ...models.check_plagiarism_model import CheckPlagiarismModel
from ..root import nlp

router = APIRouter(prefix="/tool")


@router.post("/check-plagiarism", tags=["Tools"])
def check_for_plagiarism(input: CheckPlagiarismModel):
    maintenance_ongoing = FirebaseHelper.maintenance_ref.get()

    if maintenance_ongoing == True:
        raise HTTPException(
            status_code=503, detail=APIErrorResponses.underMaintenanceErrorResponse
        )

    if input.user_type == "user":
        user = FirebaseHelper.get_user(input.email)
    elif input.user_type == "consultancy":
        user = FirebaseHelper.get_consultancy(input.email)

    if len(user) == 0:
        raise HTTPException(
            status_code=404, detail=APIErrorResponses.userNotFoundErrorResponse
        )

    if input.content == "" or len(input.content) < 100:
        raise HTTPException(
            status_code=404, detail=APIErrorResponses.contentIsShortOrEmptyErrorResponse
        )

    # update the number of plagiarism checks performed (int) on admin side
    plagiarism_checks_performed_till_now = (
        FirebaseHelper.plagiarism_checks_performed_ref.get()
    )
    FirebaseHelper.plagiarism_checks_performed_ref.set(
        plagiarism_checks_performed_till_now + 1
    )

    # update the number of plagiarism checks performed (int) on user/consultancy side
    user_data = user[0].to_dict()
    total_plagiarism_checks = user_data["total_plagiarism_checks_performed"]

    if input.user_type == "user":
        FirebaseHelper.update_user(
            input.email,
            {"overall_plagiarism_checks_performed": total_plagiarism_checks + 1},
        )
    elif input.user_type == "consultancy":
        FirebaseHelper.update_consultancy(
            input.email,
            {"total_plagiarism_checks_performed": total_plagiarism_checks + 1},
        )

    check = check_plagiarism(
        input=input,
        nlp=nlp,
    )

    return check
