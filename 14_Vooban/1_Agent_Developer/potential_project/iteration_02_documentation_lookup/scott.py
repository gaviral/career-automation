#!/usr/bin/env python3
"""
Project Scott - Iteration 2: Documentation Lookup
Q&A system with simple keyword-based documentation search

Author: Aviral Garg
Purpose: Demonstrate documentation retrieval using keyword matching
"""

import os
import sys
from pathlib import Path

# Banner and messages
BANNER = """========================================
    Project Scott - Iteration 2
    Documentation Q&A System
========================================"""

WELCOME_MESSAGE = """Welcome to Project Scott with Documentation Lookup!
Ask me questions about documentation, or type 'quit' to exit.
I can now search through documentation files to find answers!"""

GOODBYE_MESSAGE = "\nScott: Goodbye! Thanks for using Project Scott.\n"

# Exit commands (case-insensitive)
EXIT_COMMANDS = ['quit', 'exit', 'q']

# Documentation storage
documentation = {}


def load_documentation():
    """
    Load all markdown files from the documentation directory.
    
    Returns:
        dict: Dictionary with filename as key and content as value
    """
    global documentation
    doc_dir = Path(__file__).parent / "documentation"
    
    if not doc_dir.exists():
        print(f"Warning: Documentation directory not found: {doc_dir}")
        return
    
    loaded_count = 0
    for filepath in doc_dir.glob("*.md"):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                documentation[filepath.name] = f.read()
                loaded_count += 1
        except Exception as e:
            print(f"Warning: Could not load {filepath.name}: {e}")
    
    print(f"Loaded {loaded_count} documentation file(s).\n")


def extract_keywords(text):
    """
    Extract keywords from text (simple word splitting).
    
    Args:
        text (str): Input text
        
    Returns:
        list: List of lowercase keywords (3+ characters)
    """
    # Simple keyword extraction: split on whitespace and remove short words
    words = text.lower().split()
    keywords = [w for w in words if len(w) >= 3]
    return keywords


def search_documentation(question):
    """
    Search documentation for keywords from the question.
    
    Args:
        question (str): User's question
        
    Returns:
        list: List of tuples (filename, content, match_count)
    """
    keywords = extract_keywords(question)
    matches = []
    
    for filename, content in documentation.items():
        content_lower = content.lower()
        match_count = sum(1 for keyword in keywords if keyword in content_lower)
        
        if match_count > 0:
            matches.append((filename, content, match_count))
    
    # Sort by match count (most relevant first)
    matches.sort(key=lambda x: x[2], reverse=True)
    
    return matches


def extract_relevant_section(content, question, max_chars=500):
    """
    Extract the most relevant section from documentation.
    
    Args:
        content (str): Full documentation content
        question (str): User's question
        max_chars (int): Maximum characters to return
        
    Returns:
        str: Relevant section of documentation
    """
    keywords = extract_keywords(question)
    lines = content.split('\n')
    
    # Find first line containing any keyword
    start_idx = 0
    for i, line in enumerate(lines):
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in keywords):
            # Start a few lines before the match for context
            start_idx = max(0, i - 2)
            break
    
    # Extract section starting from that line
    section_lines = lines[start_idx:start_idx + 20]  # Get ~20 lines
    section = '\n'.join(section_lines)
    
    # Truncate if too long
    if len(section) > max_chars:
        section = section[:max_chars] + "..."
    
    return section


def display_banner():
    """Display the welcome banner and instructions."""
    print(BANNER)
    print()
    print(WELCOME_MESSAGE)
    print()


def get_user_input():
    """
    Get input from the user with a prompt.
    
    Returns:
        str: The user's input, or None if there was an error
    """
    try:
        user_input = input("User: ").strip()
        return user_input
    except EOFError:
        return None


def should_exit(user_input):
    """
    Check if the user wants to exit the program.
    
    Args:
        user_input (str): The user's input
        
    Returns:
        bool: True if user wants to exit, False otherwise
    """
    if user_input is None:
        return True
    return user_input.lower() in EXIT_COMMANDS


def generate_response(user_input):
    """
    Generate a response to the user's question by searching documentation.
    
    Args:
        user_input (str): The user's question
        
    Returns:
        str: The response to display
    """
    if not user_input:
        return "I didn't catch that. Could you please ask a question?"
    
    # Search documentation
    matches = search_documentation(user_input)
    
    if not matches:
        return (
            f"I couldn't find documentation matching your question: \"{user_input}\"\n"
            f"Try asking about colors (RGB values) or team processes (standup time, workflows)."
        )
    
    # Build response from top matches (max 2)
    response_parts = [f"I found {len(matches)} relevant document(s):\n"]
    
    for filename, content, match_count in matches[:2]:  # Show top 2
        relevant_section = extract_relevant_section(content, user_input)
        response_parts.append(f"\n📄 From {filename}:")
        response_parts.append(f"{relevant_section}\n")
    
    if len(matches) > 2:
        response_parts.append(f"(+ {len(matches) - 2} more document(s) also matched)")
    
    return '\n'.join(response_parts)


def display_response(response):
    """
    Display the system's response.
    
    Args:
        response (str): The response to display
    """
    print(f"Scott: {response}")
    print()  # Blank line for spacing


def display_goodbye():
    """Display the goodbye message."""
    print(GOODBYE_MESSAGE)


def main():
    """Main execution loop."""
    try:
        # Load documentation first
        load_documentation()
        
        if not documentation:
            print("Warning: No documentation loaded. Answers will be limited.\n")
        
        # Check if question provided as command-line argument (for testing)
        if len(sys.argv) > 1:
            # Non-interactive mode for testing
            question = ' '.join(sys.argv[1:])
            response = generate_response(question)
            print(f"User: {question}")
            print(f"Scott: {response}")
            return
        
        # Display welcome
        display_banner()
        
        # Main interaction loop
        while True:
            # Get user input
            user_input = get_user_input()
            
            # Check if user wants to exit
            if should_exit(user_input):
                display_goodbye()
                break
            
            # Generate and display response
            response = generate_response(user_input)
            display_response(response)
            
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print()  # New line after ^C
        display_goodbye()
    except Exception as e:
        # Handle any unexpected errors
        print(f"\nScott: Oops! Something went wrong: {str(e)}")
        print("Please try again or type 'quit' to exit.\n")


if __name__ == "__main__":
    main()

