import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

token = os.getenv("BOT_TOKEN")
api_url = os.getenv("API_URL")