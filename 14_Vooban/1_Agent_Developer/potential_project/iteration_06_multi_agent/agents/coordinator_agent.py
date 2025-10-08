"""
Coordinator Agent - Orchestrates other agents
"""

from .base_agent import Agent

class CoordinatorAgent(Agent):
    """Agent responsible for coordinating other agents and assembling responses."""
    
    def __init__(self, retrieval_agent, routing_agent):
        super().__init__("CoordinatorAgent", "System Coordinator")
        self.retrieval_agent = retrieval_agent
        self.routing_agent = routing_agent
    
    def execute(self, task):
        """
        Execute coordination task - orchestrate retrieval and routing.
        
        Args:
            task (dict): {
                'type': 'coordinate',
                'question': str
            }
        
        Returns:
            dict: {
                'retrieval_result': dict,
                'routing_result': dict,
                'response': str
            }
        """
        question = task.get('question', '')
        
        # Step 1: Request retrieval
        retrieval_result = self.retrieval_agent.execute({
            'type': 'retrieve',
            'question': question
        })
        
        # Step 2: Request routing
        routing_result = self.routing_agent.execute({
            'type': 'route',
            'question': question
        })
        
        # Step 3: Assemble response
        response = self._assemble_response(question, retrieval_result, routing_result)
        
        return {
            'retrieval_result': retrieval_result,
            'routing_result': routing_result,
            'response': response
        }
    
    def _assemble_response(self, question, retrieval_result, routing_result):
        """Assemble final response from agent results."""
        response_parts = []
        
        # Add retrieval results
        if retrieval_result['status'] == 'success' and retrieval_result['matches']:
            best_match = retrieval_result['best_match']
            filename, content, confidence = best_match
            
            if confidence > 0.7:
                section = self._extract_section(content, question)
                response_parts.append(f"✅ Found documentation (Confidence: {confidence:.0%})")
                response_parts.append(f"📄 From {filename}:\n{section}\n")
            else:
                response_parts.append(f"⚠️ Low confidence match ({confidence:.0%})")
        else:
            response_parts.append(f"⚠️ No documentation found")
        
        # Add routing results
        if routing_result['status'] == 'routed':
            sme = routing_result['sme']
            topic = routing_result['topic']
            response_parts.append(f"\n📮 Topic: {topic.replace('_', ' ').title()}")
            response_parts.append(f"👤 SME: {sme['name']} ({sme['role']})")
            response_parts.append(f"📧 Contact: {sme['slack']}")
        
        return '\n'.join(response_parts)
    
    def _extract_section(self, content, question, max_chars=500):
        """Extract relevant section from content."""
        lines = content.split('\n')
        keywords = [w.lower() for w in question.split() if len(w) > 3]
        
        start_idx = 0
        for i, line in enumerate(lines):
            if any(kw in line.lower() for kw in keywords):
                start_idx = max(0, i - 2)
                break
        
        section = '\n'.join(lines[start_idx:start_idx + 20])
        return section[:max_chars] + "..." if len(section) > max_chars else section

