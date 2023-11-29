import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    video_url = os.environ.get('VIDEO_URL')
