from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

CATALOG_PATH = BASE_DIR / "data" / "catalog.json"
CHROMA_DB_PATH = BASE_DIR / "chroma_db"
COLLECTION_NAME = "assessments"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = "gemini-2.5-flash"