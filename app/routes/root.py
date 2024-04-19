import spacy
from fastapi import APIRouter, HTTPException

from app.utils.error_responses import APIErrorResponses

from ..features.analyze_cv.utils import imp_messages as cv_analyzer_important_messages
from ..features.check_plagiarism.utils import (
    imp_messages as plagiarism_checker_important_messages,
)
from ..features.check_sop_quality.utils import (
    imp_messages_uni as uni_sop_checker_important_messages,
)
from ..firebase.firebase_helper import FirebaseHelper

router = APIRouter()

# Check if the English language model is already installed
if "en_core_web_md" not in spacy.util.get_installed_models():
    # If it's not installed, download and install it
    spacy.cli.download("en_core_web_md")
    # Load the model after installation
    nlp = spacy.load("en_core_web_md")
else:
    # If it's already installed, you can simply load it
    nlp = spacy.load("en_core_web_md")


@router.get("/", tags=["Home"])
def root():
    maintenance_ongoing = FirebaseHelper.maintenance_ref.get()

    if maintenance_ongoing is True:
        raise HTTPException(
            status_code=503, detail=APIErrorResponses.underMaintenanceErrorResponse
        )
    no_of_quality_checks_performed = FirebaseHelper.quality_checks_performed_ref.get()
    no_of_plagiarism_checks_performed = (
        FirebaseHelper.plagiarism_checks_performed_ref.get()
    )
    no_of_resume_checks_performed = FirebaseHelper.resume_checks_performed_ref.get()

    response_data = {
        "title": "Peoplane Tool Box",
        "owner": "Peoplane Technologies PVT LTD",
        "contact_email": "hello@peoplane.com",
        "tools": [
             {
                "id":1,
                "name": "Resume Analyzer",
                "purpose": "For creating polished and effective resumes.",
                "description": "Our Resume Analyzer is a user-friendly tool designed to assist you in crafting polished and effective resumes. Tailored for job seekers, this tool employs intelligent algorithms to analyze your resume and provides personalized recommendations and suggestions to help you create a standout CV for job applications.",
                "version": "1.0",
                "type": "Free",
                "isFree": True,
                "isActive": True,
                "status": "Available",
                "no_of_resume_checks_performed": no_of_resume_checks_performed,
                "more_details": cv_analyzer_important_messages.important_messages,
            },
            {
                "id":2,
                "name": "SOP/LOM Plagiarism Checker",
                "purpose": "For checking the authenticity and originality of your Statement of Purpose (SOP) or Letter of Motivation (LOM) used for your University and VISA application",
                "description": "Our SOP/LOM Plagiarism Checker is an advanced tool designed to ensure the authenticity and originality of your Statement of Purpose (SOP) or Letter of Motivation (LOM). Tailored for prospective students and job seekers, this tool employs cutting-edge technology to meticulously scan and analyze your document, identifying any instances of plagiarism or unintentional content overlap",
                "version": "1.0",
                "type": "Free",
                "isFree": True,
                "isActive": False,
                "status": "Coming Soon",
                "no_of_plagiarism_checks_performed": no_of_plagiarism_checks_performed,
                "more_details": plagiarism_checker_important_messages.important_messages,
            },
           
            {
                "id":3,
                "name": "AI Powered University SOP/LOM Quality Checker",
                "purpose": "For University applications",
                "description": "Our AI Powered University SOP/LOM Quality Checker meticulously assesses your University Statement of Purpose (SOP) or Letter of Motivation (LOM). Receive a detailed report to enhance and optimize your application for a stronger university candidacy.",
                "version": "1.0",
                "type": "Paid",
                "isFree": False,
                "isActive": True,
                "status": "Available",
                "no_of_quality_checks_performed": no_of_quality_checks_performed,
                "more_details": uni_sop_checker_important_messages.important_messages,
            },
            {
                "id":4,
                "name": "AI Powered VISA SOP/LOM Quality Checker",
                "purpose": "For VISA applications",
                "description": "Our AI Powered VISA SOP/LOM quality checker evaluates your Statement of Purpose (SOP) or Letter of Motivation (LOM) for visa applications. Receive a detailed report highlighting areas for improvement, enhancing your chances of visa approval.",
                "version": "1.0",
                "type": "Paid",
                "isFree": False,
                "isActive": False,
                "status": "Coming Soon",
                "no_of_quality_checks_performed": no_of_quality_checks_performed,
                "more_details": None,
            },
            {
                "id":5,
                "name": "Boredom Buster Activity Suggestor",
                "purpose": "For providing personalized activity recommendations based on your current location, personality, mood and budget preference",
                "description": "Boredom Buster is your go-to tool for discovering exciting activities tailored to your preferences. Whether you're an introvert or extrovert, on a tight budget or ready to splurge, this tool suggests handpicked activities and experiences in your current country. Explore new places, make the most of your free time, and create unforgettable memories.",
                "version": "1.0",
                "type": "Free",
                "isFree": True,
                "isActive": False,
                "status": "Coming Soon",
                "more_details": [
                    "Discover a variety of activities from quiet nature walks to lively social events.",
                    "Discover a wide range of activities to suit your mood and personality."
                    "Choose between free and paid options based on your budget preference.",
                    "Perfect for solo adventurers, friends, and families looking for personalized recommendations.",
                    "Enhance your experience in a new city with Boredom Buster, your virtual travel companion!",
                ],
            },
        ],
        "message": "The Peoplane Tool Box is still under development. it may make mistakes or errors. Consider checking important details yourself or consult professionals for added assurance. Your understanding is appreciated.",
    }
    return response_data
