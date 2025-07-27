from preprocess import load_and_convert_to_text
from embedding_utils import embed_texts, build_faiss_index, get_top_k_docs

texts, df = load_and_convert_to_text("data/Training Dataset.csv")
embeddings = embed_texts(texts)
index = build_faiss_index(embeddings)

def retrieve_top_docs(query, k=3):
    return get_top_k_docs(query, index, texts, k)
