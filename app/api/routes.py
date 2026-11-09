from fastAPI import APIRouter, HTTPExtensions

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm_service import generate_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response_text = await generate_response(request.message)
        return ChatResponse(response=response_text)
    except Exception as e:
        raise HTTPExtensions(
            status_code=500,
            detail='Failed to generate AI response'
        ) from e
