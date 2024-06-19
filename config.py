from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
OPENAI_SECRET_KEY = os.getenv('OPENAI_SECRET_KEY')
OPENAI_CHAT_URL = os.getenv('OPENAI_CHAT_URL')