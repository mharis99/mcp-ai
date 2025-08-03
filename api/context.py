from model import get_embedding
from sentence_transformers import util

class ContextMemory:
    def __init__(self):
        self.history = []
        self.embeddings = []

    def update(self, user_input: str, response: str):
        self.history.append({"user": user_input, "model": response})
        self.embeddings.append(get_embedding(user_input))

    def get_context(self, query=None, top_k=3):
        if not self.history:
            return ""
        if query:
            query_embedding = get_embedding(query)
            scores = [float(util.pytorch_cos_sim(query_embedding, emb)) for emb in self.embeddings]
            top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        else:
            top_indices = range(len(self.history))[-top_k:]

        context = ""
        for i in top_indices:
            h = self.history[i]
            context += f"User: {h['user']}\nAI: {h['model']}\n"
        return context
