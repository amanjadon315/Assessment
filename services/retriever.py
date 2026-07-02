from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent.parent

db_path = BASE_DIR / "chroma_db"

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=str(db_path))

collection = client.get_collection("assessments")


def search_assessments(query: str, top_k: int = 5):

    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    assessments = []

    for metadata, document, distance in zip(
    results["metadatas"][0],
    results["documents"][0],
    results["distances"][0]
):

        keys = [
            key.strip()
            for key in metadata.get("keys", "").split(",")
            if key.strip()
        ]

    assessments.append(
        {
            "entity_id": metadata["entity_id"],
            "name": metadata["name"],
            "url": metadata["url"],
            "duration": metadata["duration"],
            "remote": metadata["remote"],
            "adaptive": metadata["adaptive"],
            "distance": distance,
            "document": document,
            "keys": keys
        }
    )

    return assessments

    