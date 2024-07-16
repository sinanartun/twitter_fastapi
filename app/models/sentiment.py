from pydantic import BaseModel

class Sentiment(BaseModel):
    text: str
    sentiment: str  # e.g., bullish, bearish, neutral
