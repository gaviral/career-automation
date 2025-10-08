# Project Scott - Iteration 2: Documentation Lookup

This iteration adds the ability to search actual documentation files using keyword matching!

## What's New in This Iteration

✅ **Documentation Loading**: Reads all markdown files from `documentation/` folder  
✅ **Keyword Search**: Finds relevant documentation based on question keywords  
✅ **Smart Results**: Shows most relevant sections from matching documents  
✅ **Multiple Documents**: Can search across multiple documentation files  
✅ **Not Found Handling**: Friendly messages when documentation doesn't exist  

## What This Iteration Does

- Loads documentation files at startup
- Extracts keywords from user questions
- Searches documentation for matching keywords
- Returns relevant sections from documents
- Handles multiple matches intelligently
- Shows document names with results

## Documentation Files Included

### 1. `color_properties.md`
Contains information about:
- RGB values for lipstick colors (Unicorn Red, Classic Red, Hot Pink)
- Color processing pipelines
- Quality assurance protocols
- Technical specifications

### 2. `team_processes.md`
Contains information about:
- Daily standup time (9:30 AM PST)
- Code review standards  
- Development workflows
- Communication protocols
- Incident response procedures

## Requirements

- Python 3.10 or higher
- No external dependencies (uses standard library only)

## How to Run

```bash
python3 scott.py
```

## Example Interactions

### Example 1: Finding RGB Values
```
User: What is the RGB for unicorn red?

Scott: I found 1 relevant document(s):

📄 From color_properties.md:
#### Unicorn Red Collection
**Primary RGB**: (255, 20, 147)
- **HEX**: #FF1493
- **HSL**: 330°, 100%, 54%
- **Color Family**: Pink-Red
- **Undertone**: Cool magenta
- **Opacity**: 95%
...
```

### Example 2: Team Process Questions
```
User: What time is our standup?

Scott: I found 1 relevant document(s):

📄 From team_processes.md:
### Morning Standup (9:30 AM PST)
**Duration**: 15 minutes
**Format**: Round-robin updates
**Required Attendees**: All team members
**Topics Covered**:
- Yesterday's accomplishments
- Today's priorities
...
```

### Example 3: No Documentation Found
```
User: What is our vacation policy?

Scott: I couldn't find documentation matching your question: "What is our vacation policy?"
Try asking about colors (RGB values) or team processes (standup time, workflows).
```

## Testing the Program

### Test Case 1: Color Questions
```
User: unicorn red rgb
Expected: Should find color_properties.md with RGB (255, 20, 147)

User: hot pink color
Expected: Should find color_properties.md with Hot Pink info
```

### Test Case 2: Process Questions
```
User: standup time
Expected: Should find team_processes.md with 9:30 AM PST

User: code review
Expected: Should find team_processes.md with review standards
```

### Test Case 3: Unknown Topics
```
User: vacation policy
Expected: "No documentation found" message

User: random nonsense
Expected: "No documentation found" message
```

### Test Case 4: Multiple Matches
```
User: color system architecture
Expected: Multiple documents might match, shows top 2
```

## Key Improvements Over Iteration 1

| Feature | Iteration 1 | Iteration 2 |
|---------|-------------|-------------|
| Documentation | Hardcoded responses | Real file-based docs |
| Search | None | Keyword matching |
| Results | Generic | Specific sections |
| Multiple docs | N/A | Handles multiple sources |
| Not found | Generic | Helpful suggestions |

## File Structure

```
iteration_02_documentation_lookup/
├── README.md                      # This file
├── requirements.md                # Feature requirements
├── scott.py                       # Main script
└── documentation/                 # Documentation files
    ├── color_properties.md
    └── team_processes.md
```

## How It Works (Technical Overview)

### 1. Startup
```python
load_documentation()  # Reads all .md files from documentation/
```

### 2. Question Processing
```python
keywords = extract_keywords(question)  # ["rgb", "unicorn", "red"]
```

### 3. Search
```python
matches = search_documentation(question)
# Returns: [(filename, content, match_count), ...]
```

### 4. Result Extraction
```python
relevant_section = extract_relevant_section(content, question)
# Returns: First ~500 chars around keyword matches
```

### 5. Display
```python
display_response(formatted_response)
# Shows filename + relevant section
```

## Limitations of This Iteration

- **Simple keyword matching** (not semantic understanding)
- **No ranking by relevance** (just keyword count)
- **No match quality classification** (coming in Iteration 4)
- **No context awareness** (coming in Iteration 8)
- **No LLM integration** (coming in Iteration 7)

## Next Iteration Preview

**Iteration 3** will add:
- **Semantic search** using embeddings (sentence-transformers)
- **Confidence scores** for matches
- **Better relevance ranking** (beyond simple keyword count)
- **High-confidence detection** (>0.85 = "Complete Match")

---

**Iteration**: 2 of 8  
**Status**: Complete  
**Next**: Iteration 3 - Semantic Search


