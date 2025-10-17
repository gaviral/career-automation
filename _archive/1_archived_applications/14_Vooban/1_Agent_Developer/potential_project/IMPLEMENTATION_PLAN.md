# Project Scott - Iterative Implementation Plan

**Goal**: Build a working demonstration of Project Scott iteratively, adding one feature at a time.

**Philosophy**: Each iteration is fully functional and builds on the previous iteration. Every iteration has its own folder with requirements, design, and code.

---

## Iteration Overview

| Iteration | Feature | Demo Capability |
|-----------|---------|-----------------|
| 1 | Hello World Console | Basic Q&A loop |
| 2 | Documentation Lookup | Read from dummy files |
| 3 | Complete Match Detection | Semantic search with embeddings |
| 4 | Partial/Zero Match Classification | Match type detection |
| 5 | SME Routing | Identify correct expert |
| 6 | Multi-Agent System | Separate agents for retrieval/routing |
| 7 | Documentation Generation | Auto-create docs from SME responses |
| 8 | Conversation Memory | Context across multiple questions |

---

## Iteration 1: Hello World Console

**Folder**: `iteration_01_hello_world/`

### Requirements
- User can type questions in console
- System responds with hardcoded "Scott" message
- Clean exit on "quit" or Ctrl+C
- Professional console output formatting

### Design
- Single Python script
- Infinite loop with input/output
- Basic error handling

### Deliverables
- `requirements.md` - Feature requirements
- `design.md` - Architecture (simple flow diagram)
- `scott.py` - Main script
- `README.md` - How to run

### Success Criteria
- User can ask questions
- System responds consistently
- Clean termination

---

## Iteration 2: Documentation Lookup

**Folder**: `iteration_02_documentation_lookup/`

### Requirements
- Read from dummy documentation files
- Keyword-based search (simple string matching)
- Display matched documentation
- Handle "not found" gracefully

### Design
- Load documentation files at startup
- Simple string search across all docs
- Return matching sections
- File structure:
  ```
  documentation/
    color_properties.md
    team_processes.md
  ```

### Deliverables
- All from Iteration 1, plus:
- `documentation/` folder with dummy files
- Enhanced `scott.py` with file reading
- Search functionality

### Success Criteria
- Finds documentation for keywords like "unicorn red", "standup"
- Shows "No documentation found" for unknown topics
- Fast response (<1 second)

---

## Iteration 3: Complete Match Detection (Semantic Search)

**Folder**: `iteration_03_semantic_search/`

### Requirements
- Semantic similarity matching (not just keywords)
- Embedding-based search using sentence-transformers
- Confidence scores for matches
- High confidence (>0.85) = "Complete Match"

### Design
- Use sentence-transformers for embeddings
- Generate embeddings for all documentation at startup
- Compare query embedding with doc embeddings
- Return top match with confidence score

### Technical Stack
- `sentence-transformers` library
- `all-MiniLM-L6-v2` model (lightweight)
- Cosine similarity for matching

### Deliverables
- `requirements.txt` with dependencies
- `embedding_manager.py` - Handle embeddings
- Enhanced `scott.py` with semantic search
- `config.yaml` - Configuration settings

### Success Criteria
- Semantic matching works (e.g., "RGB for unicorn red" matches even if exact phrase not in docs)
- Confidence scores calculated correctly
- Performance: <2 seconds per query

---

## Iteration 4: Match Type Classification

**Folder**: `iteration_04_match_types/`

### Requirements
- Classify matches as: Complete, Partial, Zero, Inferred
- Different responses for each type
- Clear indication of match type to user

### Design
- **Complete** (>0.85): Direct answer
- **Partial** (0.60-0.85): "Found related info..."
- **Zero** (<0.60): "No documentation found..."
- **Inferred** (>0.70 but indirect): "Based on related docs..."

### Match Classification Logic
```python
if confidence > 0.85:
    return "complete"
elif confidence > 0.70:
    if is_direct_match:
        return "partial"
    else:
        return "inferred"
else:
    return "zero"
```

### Deliverables
- `match_classifier.py` - Match type logic
- Enhanced response formatting
- Examples in README showing each match type

### Success Criteria
- All four match types demonstrated
- User sees clear indication of confidence
- Appropriate responses for each type

---

## Iteration 5: SME Routing

**Folder**: `iteration_05_sme_routing/`

### Requirements
- Identify topic from question
- Route to correct Subject Matter Expert
- Display SME contact information
- Handle multiple topics in one question

### Design
- Topic classification using keyword/semantic matching
- SME reference table (topics → experts)
- Multiple topic handling (ranked by relevance)

### SME Reference Table
```python
SME_TABLE = {
    "color_properties": {"name": "Alice Chen", "topics": ["colors", "RGB", "lipstick"]},
    "team_processes": {"name": "Bob Smith", "topics": ["standup", "workflow", "deployment"]},
    "architecture": {"name": "Carol Lee", "topics": ["design", "infrastructure", "systems"]},
}
```

### Deliverables
- `topic_classifier.py` - Topic detection
- `sme_router.py` - SME routing logic
- `sme_table.json` - SME reference data
- Enhanced responses showing routed SME

### Success Criteria
- Correct SME identified for known topics
- Multiple topic handling works
- Fallback for unknown topics

---

## Iteration 6: Multi-Agent System

**Folder**: `iteration_06_multi_agent/`

### Requirements
- Separate specialized agents:
  - **Retrieval Agent**: Document lookup
  - **Routing Agent**: SME routing
  - **Coordinator Agent**: Orchestration
- Agents communicate via message passing
- Clean agent interfaces

### Design
- Base `Agent` class with common interface
- Each agent has: `name`, `role`, `execute()`
- Message queue for inter-agent communication
- Coordinator orchestrates workflow

### Agent Architecture
```
User Question
     ↓
Coordinator Agent
     ├→ Retrieval Agent (get docs)
     ├→ Routing Agent (identify SME)
     └→ Response Assembly
```

### Deliverables
- `agents/` folder structure:
  ```
  agents/
    base_agent.py
    retrieval_agent.py
    routing_agent.py
    coordinator_agent.py
  ```
- Message passing system
- Enhanced `scott.py` using agents

### Success Criteria
- Agents work independently
- Message passing functional
- Same functionality as Iteration 5 but with agent architecture

---

## Iteration 7: Documentation Generation

**Folder**: `iteration_07_doc_generation/`

### Requirements
- Generate new documentation when gaps found
- Simulate SME response (hardcoded or LLM)
- Add new docs to knowledge base
- Re-query shows new documentation

### Design
- When Zero/Partial match detected:
  1. Generate SME question (using LLM)
  2. Simulate SME response (dummy or LLM)
  3. Generate markdown documentation
  4. Save to documentation folder
  5. Regenerate embeddings
  6. Respond with new info

### Deliverables
- `doc_generator_agent.py` - Documentation creation
- LLM integration (OpenAI API or local)
- Persistent documentation updates
- Regeneration of embeddings

### Success Criteria
- New documentation created for gaps
- Documentation persists across runs
- Quality: Readable markdown format

---

## Iteration 8: Conversation Memory

**Folder**: `iteration_08_conversation_memory/`

### Requirements
- Remember previous questions in session
- Context-aware responses
- Follow-up questions work naturally
- Session management (clear context command)

### Design
- Conversation history stored in memory
- Pass history to LLM for context
- Smart context window management
- Commands:
  - `clear` - Clear conversation history
  - `history` - Show conversation history
  - `quit` - Exit

### Deliverables
- `conversation_manager.py` - Session management
- Context-aware LLM calls
- Enhanced UX with context hints

### Success Criteria
- Follow-up questions work correctly
- Context maintained across multiple queries
- Memory doesn't grow unbounded (smart truncation)

---

## Technical Stack (All Iterations)

### Core Dependencies
- **Python**: 3.10+
- **sentence-transformers**: Embeddings
- **numpy**: Vector operations
- **openai** or **anthropic**: LLM API (Iteration 7+)
- **pyyaml**: Configuration
- **rich**: Console formatting

### File Structure Template (Each Iteration)
```
iteration_XX_name/
├── README.md              # How to run
├── requirements.txt       # Python dependencies
├── requirements.md        # Feature requirements
├── design.md              # Architecture & design decisions
├── scott.py               # Main entry point
├── config.yaml            # Configuration
├── documentation/         # Dummy docs
│   ├── color_properties.md
│   └── team_processes.md
└── [other modules]        # Additional Python modules
```

---

## Development Workflow

### For Each Iteration:
1. **Create folder**: `iteration_XX_name/`
2. **Copy from previous**: Start with working code from last iteration
3. **Write requirements.md**: What are we building?
4. **Write design.md**: How will it work?
5. **Implement**: Build the feature
6. **Test**: Verify success criteria
7. **Document**: Update README with examples
8. **Commit**: Git commit with clear message

### Testing Approach
- Manual testing via console
- Test cases documented in README
- Example interactions showing feature works

### Success Definition
- Each iteration is fully functional
- Can demo to recruiter at any iteration
- Clear progression of features

---

## Demo Script (What to Show Recruiter)

### Iteration 1-2
"Here's the basic console interface. It reads questions and searches documentation files."

### Iteration 3-4
"Now it uses semantic search with embeddings, and classifies match types - complete, partial, zero, inferred."

### Iteration 5-6
"It routes to subject matter experts and uses a multi-agent architecture for orchestration."

### Iteration 7-8
"It generates new documentation when gaps are found and maintains conversation context."

**Key Message**: "This demonstrates the core concepts of Project Scott that I built at Amazon, using the same architecture patterns - RAG, multi-agents, SME routing, and documentation generation."

---

## Implementation Timeline

- **Iteration 1**: 1 hour
- **Iteration 2**: 2 hours
- **Iteration 3**: 3 hours (embedding setup)
- **Iteration 4**: 2 hours
- **Iteration 5**: 2 hours
- **Iteration 6**: 4 hours (refactoring to agents)
- **Iteration 7**: 4 hours (LLM integration)
- **Iteration 8**: 3 hours

**Total**: ~21 hours over 3-4 days

---

## Next Steps

1. Start with Iteration 1
2. Get it working perfectly before moving to Iteration 2
3. Repeat for each iteration
4. By the end, have a complete working demo of Project Scott


