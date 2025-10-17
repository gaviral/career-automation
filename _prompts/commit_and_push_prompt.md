# Commit and Push Workflow

Examine all the changes that have happened so far since the last commit, and then commit and push with the best conventional commit message with all the what, why, how, results, and all of those sections you think would be useful.

## Requirements:
- Make sure to not make anything up. Keep everything factual.
- Do not lose a single shot of detail.
- Do this in multiple commits, if needed, such that every single commit is following the single responsibility principle.

## Optimization:
**Minimize tool calls by chaining git commands with `&&`:**

For multiple commits, use a single command:
```bash
cd /path && \
git add file1 file2 && git commit -m "commit message 1" && \
git add file3 file4 && git commit -m "commit message 2" && \
git add file5 && git commit -m "commit message 3" && \
git push && \
git status
```

**Benefits:**
- Reduces tool calls from ~10-15 to 1-2 total
- Faster execution (single shell session)
- All operations atomic (fails if any step fails)
- Final status confirms success

**Structure:**
1. `cd` to repository root
2. For each logical commit: `git add [files] && git commit -m "message"`
3. Chain all commits with `&&`
4. End with `git push && git status`