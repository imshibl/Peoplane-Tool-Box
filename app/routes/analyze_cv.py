import datetime
import re

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.utils.error_responses import APIErrorResponses

from ..firebase.firebase_helper import FirebaseHelper
from ..functions.analyze_cv.check_name import clean_name, is_valid_text
from ..functions.analyze_cv.extract_languages import extract_languages
from ..functions.analyze_cv.get_embedded_links import extract_embedded_links
from ..functions.analyze_cv.patterns import RegexPatterns as patterns
from ..functions.analyze_cv.read_pdf import pdf_reader
from ..functions.analyze_cv.recommendations import generate_video_recommendations
from ..functions.analyze_cv.suggestions import ResumeSuggetions as cvSuggetions
from ..functions.analyze_cv.utils import imp_messages
from .root import nlp

router = APIRouter(prefix="/tool")


@router.post("/analyze-cv", tags=["Tools"])
async def analyze_cv(cv: UploadFile = File(...)):
    if not cv.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400, detail=APIErrorResponses.notAPdfFileErrorResponse
        )
    elif not cv:
        raise HTTPException(
            status_code=400, detail=APIErrorResponses.fileNotSelectedErrorResponse
        )
    content = await cv.read()

    text, page_count = pdf_reader(content)

    ### DATA FINDING & EXTRACTION SECTION
    # Find matches using regex patterns
    name_match = re.search(patterns.name_pattern, text)
    number_matches = re.findall(patterns.number_pattern, text)
    country_code_match = re.search(patterns.country_code_pattern, text)
    email_matches = re.findall(patterns.email_pattern, text)
    experience_match = re.search(patterns.experience_pattern, text)
    education_match = re.search(patterns.education_pattern, text)
    skills_match = re.search(patterns.skills_pattern, text)
    languages_match = re.search(patterns.languages_pattern, text)
    hobbies_and_interests_match = re.search(
        patterns.hobbies_and_interests_pattern, text
    )
    certifications_match = re.search(patterns.certifications_pattern, text)
    references_match = re.search(patterns.references_pattern, text)
    projects_match = re.search(patterns.projects_pattern, text)
    honors_and_awards_match = re.search(patterns.honors_and_awards_pattern, text)
    declaration_match = re.search(patterns.declaration_pattern, text)

    # Extract information
    name = name_match.group(1) if name_match else None
    numbers = (
        [f"{match[0]}{match[1]}" for match in number_matches]
        if number_matches
        else None
    )
    country_code = (
        country_code_match.group(1) or country_code_match.group(2)
        if country_code_match
        else None
    )
    emails = email_matches if email_matches else None
    has_experience = bool(experience_match)
    has_education = bool(education_match)
    has_skills = bool(skills_match)
    has_languages = bool(languages_match)
    has_hobbies_and_interests = bool(hobbies_and_interests_match)
    has_certifications = bool(certifications_match)
    has_references = bool(references_match)
    has_projects = bool(projects_match)
    has_honors_and_awards = bool(honors_and_awards_match)
    has_declaration = bool(declaration_match)

    embedded_links = extract_embedded_links(content)

    isNotAName = is_valid_text(name, nlp)
    name = None if isNotAName else name
    contact_number = numbers[0] if numbers else None
    email = emails[0] if emails else None

    name = clean_name(name)

    human_languages_data = extract_languages(text, nlp)
    human_languages_list = human_languages_data["languages"]

    if len(human_languages_list) == 0:
        has_languages = False

    # CATEGORIZATION SECTION

    general_info = {
        "name": name,
        "contact_number": contact_number,
        "country_code": country_code,
        "email": email,
    }

    must_have = {
        "experience": has_experience,
        "education": has_education,
        "skills": has_skills,
    }

    good_to_have = {
        "languages": has_languages,
        "hobbies_and_interests": has_hobbies_and_interests,
        "certifications": has_certifications,
        "projects": has_projects,
        "honors_and_awards": has_honors_and_awards,
        "references": has_references,
        "declaration": has_declaration,
    }

    # SCORING SECTION
    weights = {
        "name": 5,
        "contact_number": 10,
        "country_code": 5,
        "email": 15,
        "experience": 15,
        "education": 15,
        "skills": 15,
        "languages": 10,
        "hobbies_and_interests": 5,
        "certifications": 5,
        "projects": 5,
        "honors_and_awards": 5,
        "references": 5,
        "declaration": 5,
    }

    scores = {
        "name": 5 if general_info["name"] else 0,
        "contact_number": 10 if general_info["contact_number"] else 0,
        "country_code": 5 if general_info["country_code"] else 0,
        "email": 15 if general_info["email"] else 0,
        "experience": 15 if must_have["experience"] else 0,
        "education": 15 if must_have["education"] else 0,
        "skills": 15 if must_have["skills"] else 0,
        "languages": 10 if good_to_have["languages"] else 0,
        "hobbies_and_interests": 5 if good_to_have["hobbies_and_interests"] else 0,
        "certifications": 5 if good_to_have["certifications"] else 0,
        "projects": 5 if good_to_have["projects"] else 0,
        "honors_and_awards": 5 if good_to_have["honors_and_awards"] else 0,
        "references": 5 if good_to_have["references"] else 0,
        "declaration": 5 if good_to_have["declaration"] else 0,
    }

    total_possible_score = sum(weights.values())
    overall_score = (sum(scores.values()) / total_possible_score) * 100
    resume_score = round(overall_score)

    # RESUME UPLOADING SECTION
    # try:
    #     current_datetime = datetime.datetime.now()

    #     # Construct the new filename with readable date and time
    #     formatted_date = current_datetime.strftime("%d-%m-%Y")
    #     formatted_time = current_datetime.strftime("%I:%M%p")

    #     new_filename = f"resumes/{formatted_date}_{formatted_time}_{cv.filename}"

    #     # Upload the file using the separate function
    #     FirebaseHelper.upload_cv_to_storage(cv.file, new_filename, cv.content_type)
    # except Exception as e:
    #     print(e)

    resume_checks_performed_till_now = FirebaseHelper.resume_checks_performed_ref.get()
    FirebaseHelper.resume_checks_performed_ref.set(resume_checks_performed_till_now + 1)

    # RECOMMENDATIONS SECTION
    video_recommendations = generate_video_recommendations()

    improvement_suggestions = cvSuggetions.generateCustomResumeSuggestions(
        name=name,
        mobile_number=contact_number,
        email=email,
        country_code=country_code,
        score=resume_score,
        education=has_education,
        experience=has_experience,
        skills=has_skills,
        languages=has_languages,
        hobbies_and_interests=has_hobbies_and_interests,
        references=has_references,
        declaration=has_declaration,
        projects=has_projects,
        certifications=has_certifications,
    )

    platform_suggestions = cvSuggetions.suggest_platforms_to_create_cv(resume_score)

    page_count_based_message = cvSuggetions.message_based_on_page_count(
        page_count, resume_score
    )

    about_number_of_pages_message = cvSuggetions.about_page_number_message()

    general_info["pages"] = {
        "page_count": page_count,
        "message": page_count_based_message[0],
        "about_pages_message": about_number_of_pages_message,
    }

    return (
        {
            "overall_score": resume_score,
            "max_score": 100,
            "general_info": general_info,
            "must_have": must_have,
            "good_to_have": good_to_have,
            "human_languages": human_languages_data,
            "Embedded Links": embedded_links,
            "video_recommendations": video_recommendations,
            "improvement_suggestions": improvement_suggestions,
            "platform_suggestions": platform_suggestions,
            "imp_message": imp_messages.important_messages[0],
        },
    )
