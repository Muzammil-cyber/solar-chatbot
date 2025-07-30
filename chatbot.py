# chatbot.py
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer, util
import pickle

# Load vector store (precomputed chunks + embeddings)
with open("vector_store.pkl", "rb") as f:
    vector_store = pickle.load(f)

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load local LLM (phi2 or your preferred GGUF model)
llm = Llama(model_path="models/phi2.gguf", n_ctx=2048)

def get_answer(query, top_k=3):
    # Embed the query
    query_vec = embedding_model.encode(query, convert_to_tensor=True)

    # Find top relevant chunks
    hits = util.semantic_search(query_vec, vector_store['embeddings'], top_k=top_k)[0]
    context = "\n\n".join([vector_store['chunks'][hit['corpus_id']] for hit in hits])

    # Prompt engineering
    prompt = f"""You are a helpful assistant for a solar energy company in Pakistan. Use the context below to answer the question clearly and briefly. Answer only the question and nothing else.

Context:
{context}

Question: {query}
Answer:"""

    # Generate answer from the LLM with stop tokens to cut off excess output
    result = llm(prompt, max_tokens=150, temperature=0.2, stop=["\n\n", "Question:", "Exercise"])

    return result["choices"][0]["text"].strip()
