import random
import re

from fastapi import APIRouter, HTTPException

from ...features.check_sop_quality import check_readability as cr
from ...features.check_sop_quality import check_spelling_issues as csi
from ...features.check_sop_quality import check_vocabulary as cv
from ...features.check_sop_quality import check_word_count as cwc
from ...features.check_sop_quality import extract_data as ed
from ...features.common import get_emotion as ge
from ...features.check_sop_quality.check_keywords import (
    check_for_experience,
    check_for_motivation,
)
from ...features.check_sop_quality.extract_program import (
    extract_education_level_applying_for,
)
from ...features.common import get_read_time as read_time
from ...features.check_sop_quality.utils.custom_responses import CustomResponses
from ...firebase.firebase_helper import FirebaseHelper
from ...models import check_sop_quality_model as sim
from ...utils.const import messages
from ...utils.error_responses import APIErrorResponses
from ..root import nlp

router = APIRouter(
    prefix="/tool",
)


@router.post("/check-quality-uni", tags=["Tools"])
async def check_sop_quality_university(input: sim.CheckSOPQualityModel):
    maintenance_ongoing = FirebaseHelper.maintenance_ref.get()

    if maintenance_ongoing is True:
        raise HTTPException(
            status_code=503, detail=APIErrorResponses.underMaintenanceErrorResponse
        )

    if input.is_premium_user is False:
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

    sop_emotions = ge.get_emotions(input.sop)

    university_name_list = ed.extract_university_name(input.sop, nlp)

    if university_name_list:
        university_name = university_name_list[0]
        uni_name = university_name.lower().split()

    else:
        university_name = None
        uni_name = []

    if university_name is not None:
        if university_name.lower() == "university":
            sop_doc = nlp(input.sop)
            # Check if "TU" is present in the text
            tu_present = any(token.text.upper() == "TU" for token in sop_doc)
            if tu_present:
                university_pattern = re.compile(
                    r"\b(?:[A-Z][A-Z0-9]*\s)+[A-Z][A-Za-z0-9]*\b"
                )
                matches = university_pattern.findall(input.sop)
                tu_uni_name = matches[0].strip()
                uni_name.append(tu_uni_name)
                university_name = tu_uni_name

    people_name_list = ed.extract_people_names(input.sop, nlp)
    place_name_list = ed.extract_place_names(input.sop, nlp)
    organization_name_list = ed.extract_organization_names(input.sop, nlp)

    destination_countries_list = ed.extract_destination_country_names(input.sop, nlp)
    destination_country_names = [
        country
        for country in destination_countries_list
        if country != input.home_country
    ]

    if destination_country_names:
        destination_country_name = destination_country_names[0]
    else:
        destination_country_name = None

    education_level_applying_for = extract_education_level_applying_for(input.sop)

    word_count = cwc.check_word_count(input.sop)

    spelling_mistakes_count = csi.check_spelling_issues(
        input.sop, uni_name, people_name_list, place_name_list, organization_name_list
    )

    readability = cr.check_readability(input.sop)
    experience = check_for_experience(input.sop)
    motivation = check_for_motivation(input.sop)
    vocabulary_richness = cv.check_vocabulary_richness(input.sop, nlp)

    custom_about_uni_message = random.choice(
        CustomResponses.university_name_found_response_messages
        if university_name
        else CustomResponses.no_university_name_found_response_messages
    )

    about_univerity_message = (
        f"{custom_about_uni_message} {university_name}."
        if university_name
        else f"{custom_about_uni_message}."
    )

    custom_about_destination_country_message = random.choice(
        CustomResponses.destination_country_found_response_messages
        if destination_country_name
        else CustomResponses.destination_country_not_found_response_messages
    )

    destination_country_message = (
        f"{destination_country_name},{custom_about_destination_country_message}."
        if destination_country_name
        else f"{custom_about_destination_country_message}"
    )

    time_take_to_read_sop = read_time.calculate_reading_time(
        input.sop
    )
    
    # def classify_quality(word_count, readability, spelling_errors, experience_keywords, motivation_keywords, vocab_richness):
    # if word_count > 700 and word_count < 1400 and readability > 12 and spelling_errors < 10 and experience_keywords >= 1 and motivation_keywords >=2 and vocab_richness >= 0.40:
    #     return 'Excellent'
    # elif word_count > 500 and word_count < 1500 and readability >= 10 and spelling_errors <= 15 and motivation_keywords >=2 and vocab_richness >= 0.35:
    #     return 'Good'
    # else:
    #     return 'Poor'
    
    # wordcount = word_count[0]

    predicted_quality = 2

    if predicted_quality == 0:
        sop_quality = "Excellent"
    elif predicted_quality == 1:
        sop_quality = "Good"
    else:
        sop_quality = "Poor"

    success_response = {
        "average_time_to_read_sop": time_take_to_read_sop,
        "sop_quality": sop_quality,
        "university": about_univerity_message,
        "applying_for": education_level_applying_for,
        "destination_country": destination_country_message,
        "sop_sentiments": sop_emotions,
        "words": word_count,
        "spelling_grammer_mistakes": spelling_mistakes_count,
        "readability": readability,
        "experience_keywords": experience,
        "motivation_keywords": motivation,
        "vocabulary_richness": vocabulary_richness,
        "feedback_message": messages.ask_feedback_message,
    }

    return success_response
