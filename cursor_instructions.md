Ultra-deep thinking mode. Greater rigor, attention to detail, and multi-angle verification. Start by outlining the task and breaking down the problem into subtasks. For each subtask, explore multiple perspectives, even those that seem initially irrelevant or improbable. Purposefully attempt to disprove or challenge your own assumptions at every step. Triple-verify everything. Critically review each step, scrutinize your logic, assumptions, and conclusions, explicitly calling out uncertainties and alternative viewpoints.  Independently verify your reasoning using alternative methodologies or tools, cross-checking every fact, inference, and conclusion against external data, calculation, or authoritative sources. Deliberately seek out and employ at least twice as many verification tools or methods as you typically would. Use mathematical validations, web searches, logic evaluation frameworks, and additional resources explicitly and liberally to cross-verify your claims. Even if you feel entirely confident in your solution, explicitly dedicate additional time and effort to systematically search for weaknesses, logical gaps, hidden assumptions, or oversights. Clearly document these potential pitfalls and how you've addressed them. Once you're fully convinced your analysis is robust and complete, deliberately pause and force yourself to reconsider the entire reasoning chain one final time from scratch. Explicitly detail this last reflective step.

<task>
# Cursor Rules: Bob-Cursor Interaction Loop

**Trigger:** When the user explicitly says "here we go".

**Core Loop (Execute sequentially and repeat indefinitely):** [this loop MUST BE followed no matter what - HIGHEST PRIORITY]

STEP 1.  **Run Bob-Cursor and Get Instructions:**
    *   Execute the command `bob-cursor` in the command line **exactly once**.
    *   **Wait** for the `bob-cursor` process to fully complete and output the user's speech-to-text transcript.
    *   Capture this transcript. This is the **only** source of user instructions for the current cycle.
    *   **Crucially: Do not proceed until `bob-cursor` has finished running and you have the transcript.** Do not run `bob-cursor` again at any other point in this cycle.

STEP 2.  **Formulate Plan:**
    *   Based *only* on the transcript obtained in Step 1, determine the necessary actions.
    *   List the planned steps concisely, using the minimum number of tokens required for clarity.

STEP 3.  **Execute Tasks:**
    *   Execute the planned steps from Step 2 sequentially.
    *   If any step involves an internet lookup, first retrieve and note today’s date (e.g., via `date`) before performing the lookup.
    *   Adhere strictly to all **Mandatory Command-Line Execution Rules** listed below.
    *   Ensure each command or task completes before starting the next.

STEP 4.  **Report Results:** (THIS MUST BE DONE BEFORE STEP 5)
    *   Summarize the outcome(s) of the tasks executed in Step 3.
    *   Present the results concisely, using the minimum number of tokens required but not at the cost of exhaustiveness.

STEP 5.  **Repeat Cycle:**
    *   Immediately and **only after completing Step 4**, return to Step 1 to run `bob-cursor` again for the next set of instructions. This loop continues indefinitely.

**Mandatory Command-Line Execution Rules:**

*   **Prevent Freezing:** Append ` | cat` to commands that might hang or wait for interactive input (e.g., `git log | cat`, `git diff | cat`). **NEVER use `| cat` when running the `bob-cursor` command.**
*   **Single-Line Commands:** Ensure all commands executed in the terminal are formatted as a single line. Avoid embedding newline characters within a command string.
*   **`uv` is Mandatory for Python:**
    *   **Exclusive Use:** Use `uv` for **all** Python-related tasks: package installation/syncing (`uv pip install`, `uv pip sync`), dependency management, and virtual environment creation (`uv venv`).
    *   **Strict Avoidance:** **Do not** suggest, use, or default to `pip` (except via `uv pip`), `conda`, `anaconda`, `miniconda`, `pyenv`, `pipenv`, `poetry`, `python -m venv`, or `virtualenv`. Only discuss these if explicitly asked for a comparison.
    *   **Environment Isolation:** Assume **every** distinct Python project or sub-project requires its own dedicated `uv` virtual environment (typically named `.venv`).
    *   **Activation Required:** Always include steps for creating (`uv venv`) and activating (e.g., `source .venv/bin/activate` or `.venv\Scripts\activate`) the virtual environment in your plan (Step 2) and execution (Step 3) unless explicitly confirmed that a suitable environment is already active.
*   **Information Gathering:** If you are unsure how to use `uv` for a specific task or need other information to complete the user's request, perform a web search *before* finalizing the plan in Step 2 or executing in Step 3.

**Self-Correction/Debugging:**

*   If you find yourself running `bob-cursor` outside of Step 1, stop, discard any premature results, and restart the current cycle from the last successfully completed step (or Step 1 if unsure).
*   If a command in Step 3 fails, report the failure in Step 4 and proceed to Step 5 (running `bob-cursor` again) unless the failure prevents further progress.

---

Side note: if you have a question for me, ask your question as part of the cycle in step 4 and then repeat cycle so I can respond to you using the console log of the step 5/step1.

---

Side note:

- Never run `npm run dev` Because I'm always already running it in a different terminal window.
- always only install pip packages via requirements.txt file
- use minimum number of token in your response (but not at the cost of understandability)

</task>