from fastapi import APIRouter
from ..models.sentiment import Sentiment
from ..routers.clean import clean_text
from ..models.clean import Clean

router = APIRouter()

@router.post("/sentiment/")
async def create_sentiment(sentiment: Sentiment):
    clean_data = Clean(text=sentiment.text)
    cleaned_text = clean_text(clean_data)
    return {"text": cleaned_text["text"], "sentiment": sentiment.sentiment}
