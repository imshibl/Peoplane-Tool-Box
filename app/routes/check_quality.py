import random

import spacy
from fastapi import APIRouter, HTTPException

from ..firebase.firebase_helper import FirebaseHelper
from ..functions import check_readability as cr
from ..functions import check_spelling_issues as csi
from ..functions import check_vocabulary as cv
from ..functions import check_word_count as cwc
from ..functions import extract_data as ed
from ..functions.check_keywords import check_for_experience, check_for_motivation
from ..models import check_quality_model as sim
from ..utils.custom_responses import CustomResponses
from ..utils.error_responses import APIErrorResponses
from .root import nlp

router = APIRouter(
    prefix="/tool",
)


@router.post("/check-quality", tags=["Tools"])
async def check_sop_quality(input: sim.CheckQualityModel):
    maintenance_ongoing = FirebaseHelper.maintenance_ref.get()

    if maintenance_ongoing == True:
        raise HTTPException(
            status_code=503, detail=APIErrorResponses.underMaintenanceErrorResponse
        )

    if input.isPremiumUser == False:
        raise HTTPException(
            status_code=404, detail=APIErrorResponses.notAPremiumUserErrorResponse
        )

    if input.sop == "" or len(input.sop) < 100:
        raise HTTPException(
            status_code=404, detail=APIErrorResponses.contentIsShortOrEmptyErrorResponse
        )

    # update the number of sops checked (int)
    quality_checks_performed_till_now = (
        FirebaseHelper.quality_checks_performed_ref.get()
    )
    FirebaseHelper.quality_checks_performed_ref.set(
        quality_checks_performed_till_now + 1
    )

    university_name_list = ed.extract_university_name(input.sop, nlp)

    if university_name_list:
        university_name = university_name_list[0]
        uni_name = university_name.lower().split()
    else:
        university_name = ""
        uni_name = []

    people_name_list = ed.extract_people_names(input.sop, nlp)
    place_name_list = ed.extract_place_names(input.sop, nlp)
    organization_name_list = ed.extract_organization_names(input.sop, nlp)

    destination_country_names = ed.extract_destination_country_names(input.sop, nlp)
    if destination_country_names:
        destination_country_name = destination_country_names[0]
    else:
        destination_country_name = ""

    word_count = cwc.check_word_count(input.sop)

    spelling_mistakes_count = csi.checkSpellingIssues(
        sop_text=input.sop,
        univeristy_name_list=uni_name,
        people_name_list=people_name_list,
        place_name_list=place_name_list,
        organization_name_list=organization_name_list,
    )

    readability = cr.check_readability(input.sop)
    experience = check_for_experience(input.sop)
    motivation = check_for_motivation(input.sop)
    vocabulary_richness = cv.check_vocabulary_richness(input.sop, nlp)

    if university_name == "" and destination_country_name == "":
        custom_university_message = random.choice(
            CustomResponses.no_university_name_found_responses
        )
        about_univerity_message = f"{custom_university_message}"
    else:
        custom_university_message = random.choice(
            CustomResponses.university_name_found_response_messages
        )
        about_univerity_message = f"{custom_university_message} {university_name} in {destination_country_name}."

    if destination_country_name == "":
        destination_country_name = random.choice(
            CustomResponses.destination_country_not_found_response_messages
        )

    predicted_quality = 2

    if predicted_quality == 0:
        sop_quality = "Excellent"
    elif predicted_quality == 1:
        sop_quality = "Good"
    else:
        sop_quality = "Poor"

    success_response = {
        "sop_quality": sop_quality,
        "about_university": about_univerity_message,
        "about_destination_country": destination_country_name,
        "words": word_count,
        "spelling_grammer_mistakes": spelling_mistakes_count,
        "readability": readability,
        "experience_keywords": experience,
        "motivation_keywords": motivation,
        "vocabulary_richness": vocabulary_richness,
    }

    return success_response
