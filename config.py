from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Config:
    MONGODB_URI = os.environ.get("MONGODB_URI")
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    HOST = os.environ.get("HOST")
    PORT = os.environ.get("PORT")
    