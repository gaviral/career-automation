# Cursor Chat Context - Project Scott

## 1. What This Project Is

AI documentation agent that:
• Answers team questions via Slack
• Auto-creates missing docs by querying SMEs
• Integrates w/ ticketing & PR systems
• Uses RAG + vector DB + multi-agent architecture

Based on Amazon Beauty Tech implementation (see PROJECT_SCOTT_CONTEXT.md for full story).

## 2. Current Implementation State

### Active Files
• `PRD.md` - Working document w/ Mermaid diagram
• `PROJECT_SCOTT_CONTEXT.md` - Full background from Vooban interview
• `documentation/` - Empty, ready for dummy docs

### Archived (Ignore)
• `archive/requirements/` - Overcomplicated React attempt

## 3. Current PRD Flow

```
User asks question 
  ↓
Documentation Match
  ↓
4 outcomes:
  • Complete → Respond ✓
  • Partial → TODO
  • Zero → TODO  
  • Inferred → TODO
```

## 4. Key Constraints

• No parentheses in Mermaid diagrams
• Non-blocking, independent, parallel, event-driven
• Token minimization (lists, abbrev, symbols)
• Apple-inspired simplicity

## 5. Next Steps

1. Create dummy Beauty Tech docs in `documentation/`
2. Implement TODO flows (Partial/Zero/Inferred)
3. Keep Mermaid diagram updated as features added
4. Iterate slowly, stay simple

## 6. Quick Start for New Chat

Read these 3 files in order:
1. `CURSOR_CHAT_CONTEXT.md` (this file)
2. `PROJECT_SCOTT_CONTEXT.md` (background)
3. `PRD.md` (current diagram)

Then ask: "What should we build next?"
