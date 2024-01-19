import asyncio

from fastapi import APIRouter, HTTPException, WebSocket

from app.utils.error_responses import APIErrorResponses

from ..firebase.firebase_helper import FirebaseHelper
from ..models.feedback_model import FeedbackAndRatingModel

router = APIRouter(
    prefix="/peoplaneai",
)


@router.post("/submit-feedback-and-rating", tags=["Feedback & Rating"])
async def submit_feedback_and_rating(
    feedback_data: FeedbackAndRatingModel,
):
    isUserAvailable = FirebaseHelper.user_exists(feedback_data.user_email)

    if not isUserAvailable:
        raise HTTPException(
            status_code=403, detail=APIErrorResponses.noPermissionErrorResponse
        )

    FirebaseHelper.feedbacks_ref.add(feedback_data.model_dump())
    return {
        "message": "Feedback and rating submitted successfully",
        "data": feedback_data.model_dump(),
    }


# @router.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     # Accept the WebSocket connection
#     await websocket.accept()

#     try:
#         # Count from 1 to 1000 and send each count to connected clients
#         for i in range(1, 1001):
#             # Check if the WebSocket connection is still open
#             if websocket.client_state != WebSocket.close:
#                 # Send the count to the clientwscat -c ws://127.0.0.1:8000/peoplaneai/ws
#                 await websocket.send_text(f"Count: {i}")

#                 # Wait for a short duration before sending the next count
#                 await asyncio.sleep(0.1)

#     except Exception as e:
#         print(f"WebSocket Error: {str(e)}")
