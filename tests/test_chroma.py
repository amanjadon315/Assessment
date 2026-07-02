from pathlib import Path
import chromadb

BASE_DIR = Path(__file__).resolve().parent.parent

client = chromadb.PersistentClient(
    path=str(BASE_DIR / "chroma_db")
)

collections = client.list_collections()

print(collections)