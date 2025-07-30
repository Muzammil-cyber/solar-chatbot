from sentence_transformers import SentenceTransformer
import pickle
import os

with open("data/knowledge.txt") as f:
    text = f.read()

chunks = [text[i:i+500] for i in range(0, len(text), 500)]
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks, convert_to_tensor=True)

vector_store = {"chunks": chunks, "embeddings": embeddings}
with open("vector_store.pkl", "wb") as f:
    pickle.dump(vector_store, f)
print("✅ Vector store built")