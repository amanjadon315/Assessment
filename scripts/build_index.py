from pathlib import Path
import json

import chromadb
from sentence_transformers import SentenceTransformer

from services.document_builder import build_document

BASE_DIR = Path(__file__).resolve().parent.parent

catalog_path = BASE_DIR / "data" / "catalog.json"

db_path = BASE_DIR / "chroma_db"

with open(catalog_path, encoding="utf-8") as f:
    catalog = json.load(f)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=str(db_path))

collection = client.get_or_create_collection(
    name="assessments"
)

documents = []
metadatas = []
ids = []

for assessment in catalog:

    document, metadata = build_document(assessment)

    documents.append(document)
    metadatas.append(metadata)
    ids.append(str(assessment["entity_id"]))

embeddings = embedding_model.encode(documents).tolist()

collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings
)

print(f"Indexed {len(documents)} assessments.")