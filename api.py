from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError, Field
from typing import List, Optional
import ollama
import uuid

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change to specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "API is running! Use /chat for chatbot requests."}


class Message(BaseModel):
    role: str = Field(..., description="Role of the sender (user/system)")
    content: str = Field(..., description="Message content")


class ChatRequest(BaseModel):
    conversation_id: Optional[str] = None  # Allow None for dynamic generation
    messages: List[Message]  # Ensures each message has role & content
    language: str = "en"


# Define system instruction prompt
# Define system instruction prompt
SYSTEM_PROMPT = Message(
    role="system",
    content=(
        "You are a highly efficient and customer-friendly virtual assistant for a salon, "
        "responsible for booking appointments for haircuts, facials, and other salon services "
        "between 10 AM and 8 PM. You assist customers by providing available time slots, "
        "stylist preferences, estimated waiting times, pricing details, and special promotions. "
        "Additionally, you handle rescheduling, cancellations, and payment inquiries while ensuring "
        "a seamless and interactive user experience."
        "And your response should be in the language specified by the user. If no language is specified, respond in English. "
        "Available languages: English (en), Urdu (ur), French (fr), Spanish (es)."
    )
)

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Generate a unique session ID if not provided
        if not request.conversation_id:
            request.conversation_id = str(uuid.uuid4())

        # Validate that messages are not empty
        if not request.messages:
            raise HTTPException(status_code=400, detail="Messages cannot be empty.")

        # Ensure each message has both "role" and "content"
        for msg in request.messages:
            if not msg.content.strip():
                raise HTTPException(status_code=400, detail="Message content cannot be empty.")

        # messages = [SYSTEM_PROMPT.dict()] + [msg.dict() for msg in request.messages]  # Convert Pydantic models to dict
        messages = [SYSTEM_PROMPT.model_dump()] + [msg.model_dump() for msg in request.messages]

        # Generate response using Ollama's LLaMA 3.2 model
        response = ollama.chat(model="llama3.2", messages=messages)

        # Validate Ollama response
        if not response or "message" not in response or "content" not in response["message"]:
            raise HTTPException(status_code=500, detail="Invalid response from Ollama API.")

        bot_response = response["message"]["content"]

        return {"response": bot_response, "conversation_id": request.conversation_id}

    except ValidationError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
    except HTTPException as he:
        raise he  # Pass FastAPI-specific errors
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
