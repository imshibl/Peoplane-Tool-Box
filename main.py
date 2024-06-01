from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import root
from app.routes.feeback_and_rating import feedback
from app.routes.tools import (
    analyze_cv,
    check_plagiarism,
    check_sop_quality_uni,
    check_sop_quality_visa,
)
from app.routes.user_management import consultancy, user

app = FastAPI()

origins = [
    "https://peoplane"
    "https://peoplane.com"
    "http://localhost",
    "http://localhost:5173",
    "https://feature.d1n2ly2gca58ri.amplifyapp.com",
    "https://peoplane-agnecy.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(user.router)
app.include_router(consultancy.router)
app.include_router(check_sop_quality_uni.router)
app.include_router(check_sop_quality_visa.router)
app.include_router(check_plagiarism.router)
app.include_router(analyze_cv.router)
app.include_router(feedback.router)


# fastapi
# uvicorn
# textstat
# pyspellchecker
# spacy
# firebase-admin
# pandas
# joblib
# scikit-learn
# pycountry
# pydantic[email]
# pdfminer
# PyPDF2
# python-multipart