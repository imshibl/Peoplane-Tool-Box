from fastapi import APIRouter

from app.models.check_sop_quality_model import CheckSOPQualityModel

router = APIRouter(
    prefix="/tool",
)


@router.post("/check-quality-visa", tags=["Tools"])
async def check_sop_quality_visa(input: CheckSOPQualityModel):
    return {"message": "Not available"}
