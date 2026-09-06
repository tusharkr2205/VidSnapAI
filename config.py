import os
from dotenv import load_dotenv

load_dotenv("/Users/tusharkumar/Documents/VidSnapAI/.env")

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")