from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')


def embed_texts(texts):
    embeddings = model.encode(texts)
    return embeddings


def build_faiss_index(embeddings):
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index


def get_top_k_docs(query, index, texts, k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)
    return [texts[i] for i in indices[0]]

