"""
Routing Agent - Responsible for SME routing and topic classification
"""

from .base_agent import Agent

class RoutingAgent(Agent):
    """Agent specialized in routing questions to Subject Matter Experts."""
    
    def __init__(self, sme_table):
        super().__init__("RoutingAgent", "SME Routing Specialist")
        self.sme_table = sme_table
    
    def execute(self, task):
        """
        Execute routing task.
        
        Args:
            task (dict): {
                'type': 'route',
                'question': str
            }
        
        Returns:
            dict: {
                'topic': str,
                'sme': dict,
                'status': 'routed' | 'no_route'
            }
        """
        question = task.get('question', '')
        question_lower = question.lower()
        
        # Score each topic based on keyword matches
        scores = {}
        for topic, sme_info in self.sme_table.items():
            score = sum(1 for keyword in sme_info['expertise'] if keyword in question_lower)
            if score > 0:
                scores[topic] = score
        
        if not scores:
            return {'status': 'no_route', 'topic': None, 'sme': None}
        
        # Get best match
        best_topic = max(scores, key=scores.get)
        
        return {
            'status': 'routed',
            'topic': best_topic,
            'sme': self.sme_table[best_topic],
            'confidence': scores[best_topic] / len(question_lower.split())
        }

