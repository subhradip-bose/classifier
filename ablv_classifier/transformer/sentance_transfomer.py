from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Transformer:
    def __init__(self) -> None:
        self.n_matches = 5

    def load_model(self):
        return SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    
    def cosine_similarity(self, model, input_list: [], entity_list : []) :
        result_list = {}
        embeddings1 = model.encode(input_list)
        embeddings2 = model.encode(entity_list)
        cosine_scores = cosine_similarity(embeddings1, embeddings2)
        for i,s in zip(input_list,cosine_scores):
            indxs = np.argsort(s)[::-1][:self.n_matches]
            result = [(b,a) for a,b in zip(s[indxs],np.array(entity_list)[indxs.astype(int)])]
            list_elements = []
            for item in result:
               list_elements.append(item[0])
            result_list[i] = list_elements
        return result_list
            

        