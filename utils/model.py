from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer, util
from accelerate import init_empty_weights
import torch
import types

def load_embedder(device = None):
    device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    embedder = SentenceTransformer(model_name, device=device)
    return embedder

def find_top_reviews(reviews, question, embedder, top_k=5):
    try:
        # Your embedding computation logic
        review_embeddings = embedder.encode(reviews, convert_to_tensor=True)
        question_embedding = embedder.encode(question, convert_to_tensor=True)
        cosine_scores = util.cos_sim(question_embedding, review_embeddings)[0]
        top_results = torch.topk(cosine_scores, k=top_k)
        return [reviews[idx] for idx in top_results.indices]
    except NotImplementedError as e:
        if "Cannot copy out of meta tensor" in str(e):
            # Reload model and retry once
            embedder = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')
            embeddings = embedder.encode(reviews, convert_to_tensor=True)
            question_embedding = embedder.encode(question, convert_to_tensor=True)
            cosine_scores = util.cos_sim(question_embedding, review_embeddings)[0]
            top_results = torch.topk(cosine_scores, k=top_k)
            return [reviews[idx] for idx in top_results.indices]
        else:
            raise e
    