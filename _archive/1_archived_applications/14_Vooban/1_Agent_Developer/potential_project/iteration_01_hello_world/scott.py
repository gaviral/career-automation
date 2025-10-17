#!/usr/bin/env python3
"""
Project Scott - Iteration 1: Hello World Console
A basic Q&A demonstration system

Author: Aviral Garg
Purpose: Demonstrate core interaction pattern of Project Scott
"""

import sys

# Banner and messages
BANNER = """========================================
    Project Scott - Iteration 1
    Documentation Q&A System
========================================"""

WELCOME_MESSAGE = """Welcome to Project Scott!
Ask me questions about documentation, or type 'quit' to exit."""

GOODBYE_MESSAGE = "\nScott: Goodbye! Thanks for using Project Scott.\n"

# Exit commands (case-insensitive)
EXIT_COMMANDS = ['quit', 'exit', 'q']


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
        # Handle Ctrl+D (EOF)
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
    Generate a response to the user's question.
    In this iteration, we just acknowledge the question.
    
    Args:
        user_input (str): The user's question
        
    Returns:
        str: The response to display
    """
    if not user_input:
        return "I didn't catch that. Could you please ask a question?"
    
    response = (
        f'Thanks for your question! In this demo version, I\'m acknowledging '
        f'your question: "{user_input}"\n'
        f'In future iterations, I\'ll be able to search documentation and provide real answers!'
    )
    return response


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

