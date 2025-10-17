"""
Retrieval Agent - Responsible for searching documentation
"""

from .base_agent import Agent
from sentence_transformers import SentenceTransformer, util

class RetrievalAgent(Agent):
    """Agent specialized in document retrieval using semantic search."""
    
    def __init__(self, documentation, doc_embeddings, model):
        super().__init__("RetrievalAgent", "Documentation Retrieval Specialist")
        self.documentation = documentation
        self.doc_embeddings = doc_embeddings
        self.model = model
    
    def execute(self, task):
        """
        Execute retrieval task.
        
        Args:
            task (dict): {
                'type': 'retrieve',
                'question': str
            }
        
        Returns:
            dict: {
                'matches': [(filename, content, confidence), ...],
                'status': 'success' | 'no_matches'
            }
        """
        question = task.get('question', '')
        
        if not question:
            return {'status': 'error', 'message': 'No question provided'}
        
        # Generate embedding for question
        question_embedding = self.model.encode(question, convert_to_tensor=True)
        
        # Search all documents
        matches = []
        for filename, doc_embedding in self.doc_embeddings.items():
            similarity = util.cos_sim(question_embedding, doc_embedding).item()
            matches.append((filename, self.documentation[filename], similarity))
        
        # Sort by similarity
        matches.sort(key=lambda x: x[2], reverse=True)
        
        return {
            'status': 'success' if matches else 'no_matches',
            'matches': matches,
            'best_match': matches[0] if matches else None
        }

