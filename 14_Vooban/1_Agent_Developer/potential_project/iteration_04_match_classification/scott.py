#!/usr/bin/env python3
"""
Project Scott - Iteration 4: Match Type Classification
Q&A system with Complete/Partial/Zero/Inferred match classification

Author: Aviral Garg
Purpose: Demonstrate match type classification as described in Amazon Project Scott
"""

import os
import sys
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Banner
BANNER = """========================================
    Project Scott - Iteration 4
 Match Type Classification System
========================================"""

WELCOME_MESSAGE = """Welcome to Project Scott with Match Classification!
I now classify matches as: Complete, Partial, Zero, or Inferred
Ask questions to see how confidence affects match types!"""

GOODBYE_MESSAGE = "\nScott: Goodbye! Thanks for using Project Scott.\n"
EXIT_COMMANDS = ['quit', 'exit', 'q']

# Global state
documentation = {}
doc_embeddings = {}
model = None

def load_model():
    """Load the sentence transformer model."""
    global model
    print("Loading semantic search model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Model loaded!\n")

def load_documentation():
    """Load all markdown files and generate embeddings."""
    global documentation, doc_embeddings
    doc_dir = Path(__file__).parent / "documentation"
    
    if not doc_dir.exists():
        print(f"Warning: Documentation directory not found")
        return
    
    print("Loading and embedding documentation...")
    for filepath in doc_dir.glob("*.md"):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                documentation[filepath.name] = content
                doc_embeddings[filepath.name] = model.encode(content, convert_to_tensor=True)
        except Exception as e:
            print(f"Warning: Could not load {filepath.name}: {e}")
    
    print(f"Loaded {len(documentation)} documentation file(s).\n")

def search_documentation(question):
    """Search documentation using semantic similarity."""
    if not doc_embeddings:
        return []
    
    question_embedding = model.encode(question, convert_to_tensor=True)
    
    matches = []
    for filename, doc_embedding in doc_embeddings.items():
        similarity = util.cos_sim(question_embedding, doc_embedding).item()
        matches.append((filename, documentation[filename], similarity))
    
    matches.sort(key=lambda x: x[2], reverse=True)
    return matches

def is_direct_match(question, content):
    """
    Check if match is direct or inferred.
    Direct: Key terms from question appear in content
    Inferred: Semantically related but not direct
    """
    keywords = [w.lower() for w in question.split() if len(w) > 3]
    content_lower = content.lower()
    
    # Count how many keywords appear directly
    direct_matches = sum(1 for kw in keywords if kw in content_lower)
    
    # If more than half keywords present, consider it direct
    return direct_matches >= len(keywords) * 0.5

def classify_match_type(confidence, is_direct):
    """
    Classify match type based on confidence and directness.
    
    Args:
        confidence (float): Similarity score (0-1)
        is_direct (bool): Whether keywords appear directly in content
        
    Returns:
        tuple: (match_type, emoji, color_code, description)
    """
    if confidence > 0.85:
        return ("COMPLETE MATCH", "✅", "green", "Very high confidence - exact documentation found")
    elif confidence > 0.70:
        if is_direct:
            return ("PARTIAL MATCH", "🔵", "blue", "High confidence - relevant documentation found")
        else:
            return ("INFERRED MATCH", "🔮", "purple", "High confidence but indirect - inferred from related docs")
    elif confidence > 0.50:
        return ("PARTIAL MATCH", "🟡", "yellow", "Moderate confidence - some relevant information")
    else:
        return ("ZERO MATCH", "❌", "red", "Low confidence - no relevant documentation found")

def handle_zero_match(question):
    """
    Handle zero match scenario - would contact SME in production.
    For now, just indicate what would happen.
    """
    return (
        f"🔍 ZERO MATCH DETECTED for: \"{question}\"\n\n"
        f"In production Project Scott, this would:\n"
        f"1. Classify the topic (e.g., 'vacation policy', 'benefits')\n"
        f"2. Route to appropriate Subject Matter Expert\n"
        f"3. Ask SME specific targeted questions\n"
        f"4. Generate documentation from responses\n"
        f"5. Update vector database\n"
        f"6. Respond to your question with new information\n\n"
        f"For now: No documentation found. Try asking about colors or team processes."
    )

def extract_relevant_section(content, question, max_chars=600):
    """Extract relevant section from documentation."""
    lines = content.split('\n')
    keywords = [w.lower() for w in question.split() if len(w) > 3]
    
    start_idx = 0
    for i, line in enumerate(lines):
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in keywords):
            start_idx = max(0, i - 2)
            break
    
    section_lines = lines[start_idx:start_idx + 25]
    section = '\n'.join(section_lines)
    
    if len(section) > max_chars:
        section = section[:max_chars] + "..."
    
    return section

def display_banner():
    """Display welcome banner."""
    print(BANNER)
    print()
    print(WELCOME_MESSAGE)
    print()

def get_user_input():
    """Get input from user."""
    try:
        return input("User: ").strip()
    except EOFError:
        return None

def should_exit(user_input):
    """Check if user wants to exit."""
    if user_input is None:
        return True
    return user_input.lower() in EXIT_COMMANDS

def generate_response(user_input):
    """Generate response with match type classification."""
    if not user_input:
        return "I didn't catch that. Could you please ask a question?"
    
    matches = search_documentation(user_input)
    
    if not matches:
        return handle_zero_match(user_input)
    
    filename, content, confidence = matches[0]
    is_direct = is_direct_match(user_input, content)
    match_type, emoji, color, description = classify_match_type(confidence, is_direct)
    
    # Handle zero match
    if match_type == "ZERO MATCH":
        return handle_zero_match(user_input)
    
    relevant_section = extract_relevant_section(content, user_input)
    
    response = (
        f"{emoji} {match_type}\n"
        f"Confidence: {confidence:.1%} | {description}\n\n"
        f"📄 From {filename}:\n"
        f"{relevant_section}\n"
    )
    
    # Show additional matches if relevant
    if len(matches) > 1 and matches[1][2] > 0.5:
        response += f"\n(Also found relevant info in {matches[1][0]} - {matches[1][2]:.0%} confidence)"
    
    return response

def display_response(response):
    """Display system response."""
    print(f"Scott: {response}")
    print()

def display_goodbye():
    """Display goodbye message."""
    print(GOODBYE_MESSAGE)

def main():
    """Main execution loop."""
    try:
        load_model()
        load_documentation()
        
        if not documentation:
            print("Warning: No documentation loaded.\n")
        
        # CLI argument support for testing
        if len(sys.argv) > 1:
            question = ' '.join(sys.argv[1:])
            response = generate_response(question)
            print(f"User: {question}")
            print(f"Scott: {response}")
            return
        
        display_banner()
        
        while True:
            user_input = get_user_input()
            
            if should_exit(user_input):
                display_goodbye()
                break
            
            response = generate_response(user_input)
            display_response(response)
            
    except KeyboardInterrupt:
        print()
        display_goodbye()
    except Exception as e:
        print(f"\nScott: Oops! Something went wrong: {str(e)}")
        print("Please try again or type 'quit' to exit.\n")

if __name__ == "__main__":
    main()

