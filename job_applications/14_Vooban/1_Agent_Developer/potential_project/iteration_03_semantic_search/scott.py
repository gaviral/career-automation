#!/usr/bin/env python3
"""
Project Scott - Iteration 3: Semantic Search
Q&A system with embedding-based semantic search

Author: Aviral Garg
Purpose: Demonstrate semantic similarity matching using sentence transformers
"""

import os
import sys
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Banner and messages
BANNER = """========================================
    Project Scott - Iteration 3
    Semantic Search with Embeddings
========================================"""

WELCOME_MESSAGE = """Welcome to Project Scott with Semantic Search!
I now understand the MEANING of your questions, not just keywords!
Ask me questions about documentation, or type 'quit' to exit."""

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
        print(f"Warning: Documentation directory not found: {doc_dir}")
        return
    
    print("Loading and embedding documentation...")
    loaded_count = 0
    for filepath in doc_dir.glob("*.md"):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                documentation[filepath.name] = content
                # Generate embedding
                doc_embeddings[filepath.name] = model.encode(content, convert_to_tensor=True)
                loaded_count += 1
        except Exception as e:
            print(f"Warning: Could not load {filepath.name}: {e}")
    
    print(f"Loaded {loaded_count} documentation file(s).\n")

def search_documentation(question):
    """
    Search documentation using semantic similarity.
    
    Args:
        question (str): User's question
        
    Returns:
        list: List of tuples (filename, content, confidence_score)
    """
    if not doc_embeddings:
        return []
    
    # Generate embedding for question
    question_embedding = model.encode(question, convert_to_tensor=True)
    
    # Calculate similarity with each document
    matches = []
    for filename, doc_embedding in doc_embeddings.items():
        similarity = util.cos_sim(question_embedding, doc_embedding).item()
        matches.append((filename, documentation[filename], similarity))
    
    # Sort by similarity (highest first)
    matches.sort(key=lambda x: x[2], reverse=True)
    
    return matches

def extract_relevant_section(content, question, max_chars=500):
    """Extract relevant section from documentation."""
    lines = content.split('\n')
    keywords = question.lower().split()
    
    # Find first line containing any keyword
    start_idx = 0
    for i, line in enumerate(lines):
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in keywords):
            start_idx = max(0, i - 2)
            break
    
    section_lines = lines[start_idx:start_idx + 20]
    section = '\n'.join(section_lines)
    
    if len(section) > max_chars:
        section = section[:max_chars] + "..."
    
    return section

def classify_confidence(score):
    """
    Classify confidence level based on similarity score.
    
    Args:
        score (float): Similarity score (0-1)
        
    Returns:
        tuple: (confidence_level, emoji, description)
    """
    if score > 0.85:
        return ("COMPLETE MATCH", "✅", "Very high confidence")
    elif score > 0.70:
        return ("GOOD MATCH", "👍", "High confidence")
    elif score > 0.50:
        return ("PARTIAL MATCH", "🤔", "Moderate confidence")
    else:
        return ("WEAK MATCH", "⚠️", "Low confidence")

def display_banner():
    """Display the welcome banner."""
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
    """Generate response using semantic search."""
    if not user_input:
        return "I didn't catch that. Could you please ask a question?"
    
    matches = search_documentation(user_input)
    
    if not matches or matches[0][2] < 0.3:
        return (
            f"I couldn't find documentation matching your question: \"{user_input}\"\n"
            f"(Confidence too low: {matches[0][2]:.2%} if matches else 0)\n"
            f"Try asking about colors (RGB values) or team processes."
        )
    
    # Show top match with confidence
    filename, content, confidence = matches[0]
    conf_level, emoji, desc = classify_confidence(confidence)
    
    relevant_section = extract_relevant_section(content, user_input)
    
    response = (
        f"{emoji} {conf_level} (Confidence: {confidence:.2%})\n\n"
        f"📄 From {filename}:\n"
        f"{relevant_section}\n"
    )
    
    if len(matches) > 1 and matches[1][2] > 0.5:
        response += f"\n(Also found relevant info in {matches[1][0]} - confidence: {matches[1][2]:.2%})"
    
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
        
        # Check if question provided as command-line argument (for testing)
        if len(sys.argv) > 1:
            # Non-interactive mode for testing
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

