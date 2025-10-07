from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model once at startup
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Model loading failed: {str(e)}")
    summarizer = None

app = FastAPI(
    title="Text Summarization API",
    description="Summarize text using DistilBART CNN model"
)

class TextRequest(BaseModel):
    text: str
    max_length: int = 130
    min_length: int = 30

@app.post("/summarize")
async def summarize_text(request: TextRequest):
    if not summarizer:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    try:
        # Ensure reasonable length constraints
        max_len = min(request.max_length, 512)
        min_len = min(request.min_length, max_len - 20)
        
        summary = summarizer(
            request.text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
        logger.error(f"Summarization error: {str(e)}")
        raise HTTPException(status_code=500, detail="Summarization failed")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": summarizer is not None}