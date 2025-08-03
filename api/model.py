from sentence_transformers import SentenceTransformer, util

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def mock_llm(prompt: str) -> str:
    return f"[Mock LLM Response] Based on context: {prompt}"

def get_embedding(text: str):
    return embedding_model.encode(text, convert_to_tensor=True)
