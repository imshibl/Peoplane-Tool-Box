from fastapi import FastAPI

from app.routes import analyze_cv, check_plagiarism, check_quality, feedback, root
from app.routes.user_management import consultancy, user

app = FastAPI()


app.include_router(root.router)
app.include_router(user.router)
app.include_router(consultancy.router)
app.include_router(check_quality.router)
app.include_router(check_plagiarism.router)
app.include_router(analyze_cv.router)
app.include_router(feedback.router)
