from fastapi import APIRouter, HTTPException

from app.utils.error_responses import APIErrorResponses

from ..firebase.firebase_helper import FirebaseHelper
from ..functions.check_plagiarism.check_plagiarism import check_plagiarism
from ..models.check_plagiarism_model import CheckPlagiarismModel
from .check_quality import nlp

router = APIRouter(prefix="/peoplaneai")


@router.post("/check-plagiarism", tags=["tools"])
def check_for_plagiarism(input: CheckPlagiarismModel):
    maintenance_ongoing = FirebaseHelper.maintenance_ref.get()

    if maintenance_ongoing == True:
        raise HTTPException(
            status_code=503, detail=APIErrorResponses.underMaintenanceErrorResponse
        )

    if input.content == "" or len(input.content) < 100:
        raise HTTPException(
            status_code=404, detail=APIErrorResponses.contentIsShortOrEmptyErrorResponse
        )

    plagiarism_checks_performed_till_now = (
        FirebaseHelper.plagiarism_checks_performed_ref.get()
    )
    FirebaseHelper.plagiarism_checks_performed_ref.set(
        plagiarism_checks_performed_till_now + 1
    )

    check = check_plagiarism(
        sop=input.content,
        owner=input.owner_email,
        type=input.type,
        nlp=nlp,
    )

    return check