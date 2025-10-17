"""
Base Agent class for Project Scott multi-agent system
"""

class Agent:
    """Base class for all agents in the system."""
    
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.messages = []
    
    def receive_message(self, sender, message):
        """Receive a message from another agent."""
        self.messages.append({
            'sender': sender,
            'message': message,
            'timestamp': None
        })
    
    def send_message(self, recipient, message):
        """Send a message to another agent."""
        if hasattr(recipient, 'receive_message'):
            recipient.receive_message(self.name, message)
            return True
        return False
    
    def execute(self, task):
        """Execute agent's primary function. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement execute()")
    
    def __repr__(self):
        return f"Agent(name={self.name}, role={self.role})"

