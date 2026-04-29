
import chromadb
from rag.embedder import get_embedding

client = chromadb.Client()
collection = client.get_or_create_collection("legal")

def search_knowledge(query):
    emb = get_embedding(query)
    res = collection.query(query_embeddings=[emb], n_results=3)
    return res.get("documents", [])
