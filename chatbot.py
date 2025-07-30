from sentence_transformers import SentenceTransformer, util

class SolarChatbot:
    def __init__(self, knowledge_path):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        with open(knowledge_path, "r", encoding="utf-8") as f:
            self.knowledge = [line.strip() for line in f if line.strip()]
        self.embeddings = self.model.encode(self.knowledge, convert_to_tensor=True)

    def get_response(self, query):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.pytorch_cos_sim(query_embedding, self.embeddings)[0]
        best_match_idx = scores.argmax().item()
        best_score = scores[best_match_idx].item()

        if best_score < 0.5:
            return "I'm not sure how to answer that. Can you please rephrase or ask about solar panels, estimates, or maintenance?"

        return self.knowledge[best_match_idx]
