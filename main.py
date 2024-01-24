from fastapi import FastAPI

from app.routes import (
    analyze_cv,
    check_plagiarism,
    check_sop_quality_uni,
    check_sop_quality_visa,
    feedback,
    root,
)
from app.routes.user_management import consultancy, user

app = FastAPI()


app.include_router(root.router)
app.include_router(user.router)
app.include_router(consultancy.router)
app.include_router(check_sop_quality_uni.router)
app.include_router(check_sop_quality_visa.router)
app.include_router(check_plagiarism.router)
app.include_router(analyze_cv.router)
app.include_router(feedback.router)
