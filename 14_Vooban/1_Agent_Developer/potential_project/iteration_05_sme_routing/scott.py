#!/usr/bin/env python3
"""
Project Scott - Iteration 5: SME Routing
Adds Subject Matter Expert routing based on topic classification
"""

import os, sys, json
from pathlib import Path
from sentence_transformers import SentenceTransformer, util

BANNER = """========================================
    Project Scott - Iteration 5
   SME Routing & Topic Classification
========================================"""

WELCOME_MESSAGE = """Welcome to Project Scott with SME Routing!
I can now identify topics and route to the right expert!"""

GOODBYE_MESSAGE = "\nScott: Goodbye! Thanks for using Project Scott.\n"
EXIT_COMMANDS = ['quit', 'exit', 'q']

documentation = {}
doc_embeddings = {}
sme_table = {}
model = None

def load_model():
    global model
    print("Loading model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Model loaded!\n")

def load_sme_table():
    global sme_table
    sme_file = Path(__file__).parent / "sme_table.json"
    try:
        with open(sme_file, 'r') as f:
            sme_table = json.load(f)
        print(f"Loaded SME table with {len(sme_table)} experts.\n")
    except:
        print("Warning: Could not load SME table\n")

def load_documentation():
    global documentation, doc_embeddings
    doc_dir = Path(__file__).parent / "documentation"
    if not doc_dir.exists():
        return
    print("Loading documentation...")
    for filepath in doc_dir.glob("*.md"):
        with open(filepath, 'r') as f:
            content = f.read()
            documentation[filepath.name] = content
            doc_embeddings[filepath.name] = model.encode(content, convert_to_tensor=True)
    print(f"Loaded {len(documentation)} docs.\n")

def classify_topic(question):
    """Classify question topic using keyword matching with SME expertise."""
    question_lower = question.lower()
    scores = {}
    
    for topic, sme_info in sme_table.items():
        score = sum(1 for keyword in sme_info['expertise'] if keyword in question_lower)
        if score > 0:
            scores[topic] = score
    
    if not scores:
        return None, None
    
    best_topic = max(scores, key=scores.get)
    return best_topic, sme_table[best_topic]

def search_documentation(question):
    if not doc_embeddings:
        return []
    question_embedding = model.encode(question, convert_to_tensor=True)
    matches = []
    for filename, doc_embedding in doc_embeddings.items():
        similarity = util.cos_sim(question_embedding, doc_embedding).item()
        matches.append((filename, documentation[filename], similarity))
    matches.sort(key=lambda x: x[2], reverse=True)
    return matches

def extract_relevant_section(content, question, max_chars=500):
    lines = content.split('\n')
    keywords = [w.lower() for w in question.split() if len(w) > 3]
    start_idx = 0
    for i, line in enumerate(lines):
        if any(kw in line.lower() for kw in keywords):
            start_idx = max(0, i - 2)
            break
    section = '\n'.join(lines[start_idx:start_idx + 20])
    return section[:max_chars] + "..." if len(section) > max_chars else section

def generate_response(user_input):
    if not user_input:
        return "I didn't catch that."
    
    matches = search_documentation(user_input)
    topic, sme = classify_topic(user_input)
    
    # Build response
    response_parts = []
    
    if matches and matches[0][2] > 0.7:
        # Good match found
        filename, content, confidence = matches[0]
        section = extract_relevant_section(content, user_input)
        response_parts.append(f"✅ Found documentation (Confidence: {confidence:.0%})\n")
        response_parts.append(f"📄 From {filename}:\n{section}\n")
    else:
        response_parts.append(f"⚠️ No strong documentation match found.\n")
    
    # Add SME routing info
    if topic and sme:
        response_parts.append(f"\n📮 Routed Topic: {topic.replace('_', ' ').title()}")
        response_parts.append(f"👤 Subject Matter Expert: {sme['name']} ({sme['role']})")
        response_parts.append(f"📧 Contact: {sme['slack']} or {sme['email']}")
        
        if not matches or matches[0][2] < 0.7:
            response_parts.append(f"\n💡 In production, Scott would:")
            response_parts.append(f"1. Contact {sme['name']} via Slack")
            response_parts.append(f"2. Ask specific targeted questions")
            response_parts.append(f"3. Generate documentation from responses")
            response_parts.append(f"4. Update vector database")
            response_parts.append(f"5. Respond with new information")
    else:
        response_parts.append(f"\n❓ Could not classify topic. Would escalate to general support.")
    
    return '\n'.join(response_parts)

def main():
    try:
        load_model()
        load_sme_table()
        load_documentation()
        
        if len(sys.argv) > 1:
            question = ' '.join(sys.argv[1:])
            response = generate_response(question)
            print(f"User: {question}")
            print(f"Scott: {response}")
            return
        
        print(BANNER)
        print()
        print(WELCOME_MESSAGE)
        print()
        
        while True:
            user_input = input("User: ").strip()
            if not user_input or user_input.lower() in EXIT_COMMANDS:
                print(GOODBYE_MESSAGE)
                break
            response = generate_response(user_input)
            print(f"Scott: {response}\n")
    except KeyboardInterrupt:
        print(f"\n{GOODBYE_MESSAGE}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

