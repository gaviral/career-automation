# Project Scott - Iteration 1: Hello World Console

Welcome to the first iteration of Project Scott! This is a basic demonstration of the core interaction pattern that will be built upon in future iterations.

## What This Iteration Does

- Provides a console-based Q&A interface
- Accepts user questions
- Acknowledges questions with friendly responses
- Demonstrates the basic loop: question → response → next question
- Handles exit commands gracefully

## What This Iteration Does NOT Do (Yet)

- Read from documentation files
- Perform semantic search
- Classify match types
- Route to subject matter experts
- Use LLMs or AI models
- Store conversation history

**These features come in future iterations!**

## Requirements

- Python 3.10 or higher
- No external dependencies (uses standard library only)

## How to Run

### Option 1: Direct execution
```bash
python3 scott.py
```

### Option 2: Make executable (Unix/Mac)
```bash
chmod +x scott.py
./scott.py
```

## How to Use

1. **Start the program**
   ```bash
   python3 scott.py
   ```

2. **Ask questions**
   ```
   User: What is the RGB value for unicorn red?
   ```

3. **Get responses**
   ```
   Scott: Thanks for your question! In this demo version, I'm acknowledging 
   your question: "What is the RGB value for unicorn red?"
   In future iterations, I'll be able to search documentation and provide real answers!
   ```

4. **Exit the program**
   - Type `quit` or `exit`
   - Or press `Ctrl+C`

## Example Interaction

```
========================================
    Project Scott - Iteration 1
    Documentation Q&A System
========================================

Welcome to Project Scott!
Ask me questions about documentation, or type 'quit' to exit.

User: What is the RGB value for unicorn red?
Scott: Thanks for your question! In this demo version, I'm acknowledging 
your question: "What is the RGB value for unicorn red?"
In future iterations, I'll be able to search documentation and provide real answers!

User: What time is our daily standup?
Scott: Thanks for your question! In this demo version, I'm acknowledging 
your question: "What time is our daily standup?"
In future iterations, I'll be able to search documentation and provide real answers!

User: quit
Scott: Goodbye! Thanks for using Project Scott.
```

## Testing the Program

### Test Case 1: Normal Interaction
1. Run the program
2. Type a question
3. Verify you get a response
4. Type another question
5. Verify continuous operation

### Test Case 2: Exit Commands
1. Run the program
2. Type `quit` → Should exit gracefully
3. Run again, type `exit` → Should exit gracefully
4. Run again, type `QUIT` (uppercase) → Should exit gracefully

### Test Case 3: Keyboard Interrupt
1. Run the program
2. Press `Ctrl+C`
3. Verify graceful exit with goodbye message

### Test Case 4: Edge Cases
1. Run the program
2. Press Enter without typing anything → Should handle gracefully
3. Type very long question → Should handle gracefully
4. Type special characters → Should handle gracefully

## File Structure

```
iteration_01_hello_world/
├── README.md           # This file
├── requirements.md     # Feature requirements
├── design.md           # Architecture and design
└── scott.py            # Main script
```

## Key Concepts Demonstrated

### 1. **Interaction Loop**
The fundamental pattern of Project Scott:
- User asks question
- System processes
- System responds
- Repeat

### 2. **Clean Console Interface**
Professional formatting:
- Clear prompts (`User:`, `Scott:`)
- Proper spacing
- Readable output

### 3. **Graceful Exit Handling**
Multiple exit paths:
- Command-based (quit/exit)
- Keyboard interrupt (Ctrl+C)
- EOF handling (Ctrl+D)

### 4. **Error Handling**
Defensive programming:
- Empty input handling
- Unexpected errors caught
- User-friendly error messages

## Next Iteration Preview

**Iteration 2** will add:
- Reading from actual documentation files (`color_properties.md`, `team_processes.md`)
- Simple keyword-based search
- Displaying matched documentation
- "Not found" handling

## Design Philosophy

Each iteration:
- ✅ Is fully functional
- ✅ Can be demonstrated independently
- ✅ Builds on previous iteration
- ✅ Adds exactly one major feature
- ✅ Maintains clean, readable code

## Questions or Issues?

This is a demonstration project showing the core concepts of the Project Scott system built at Amazon. Each iteration adds more sophisticated features leading to a fully functional AI-powered documentation assistant.

---

**Iteration**: 1 of 8  
**Status**: Complete  
**Next**: Iteration 2 - Documentation Lookup


