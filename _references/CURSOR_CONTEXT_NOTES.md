# Cursor Context Notes for Career Automation Project

## Current Working Context (Updated: October 5, 2025)

### Active Job Application: Kardium - Senior Software Build Engineer

**Status:** Application selected, moving to interview stage  
**Location:** Vancouver, BC (Hybrid)  
**Folder:** `9_Kardium/2_Senior_Software_Build_Engineer/`

#### Interview Process (6 Stages):
1. **General Interview with Talent Team** - 30-45 min Teams call
2. **Take-Home Test**
3. **Panel 1 Technical Interview** - 90-120 min with immediate team
4. **Panel 2 Technical Interview** - 90-120 min with collaborating teams
5. **Executive Interview** - 60 min
6. **Reference Check**

**Timeline:** 3-6 weeks total  
**In-person component:** At least one interview in Vancouver office (with potential company tour)

**Contact:** Sara Khoshbakht - Team Lead, Talent Acquisition

---

## Transcription Context

### Multi-Person Discussions
You may see transcriptions that include:
- Aviral (the user) discussing job applications and interview preparation
- Friends/colleagues providing feedback and advice
- Group discussions about interview strategy
- Shared screen sessions analyzing job requirements

### What to Expect in Transcriptions:
- **Multiple speakers** - not just Aviral, but also friends helping with preparation
- **Collaborative brainstorming** - people discussing approaches together
- **Instructions embedded in conversations** - tasks may be mentioned conversationally
- **Screen sharing context** - references to things being shown on screen

### How to Handle This:
- **Extract actionable tasks** from conversational transcriptions
- **Identify the speaker** when context matters
- **Distinguish between** discussion/brainstorming vs. actual instructions
- **Look for confirmation** of tasks before executing if ambiguous

---

## Project Structure Notes

### Backup Strategy
A stable backup folder exists alongside the main working folder:
- **Working folder:** `9_Kardium/` - for active experimentation and changes
- **Backup folder:** `9_Kardium_stable_backup_[date]/` - preserved state before major changes

**Why:** Allows experimentation with new approaches while maintaining a safe restore point if something goes wrong.

---

## Common Workflows

### Bob-Cursor Loop
This project uses a custom voice-to-action workflow:
1. Run `bob-cursor` command to capture speech-to-text
2. Extract instructions from transcription
3. Formulate plan
4. Execute tasks
5. Report results
6. Repeat

### Task Execution Principles
- **Never run** `npm run dev` (always already running in separate terminal)
- **Always use** `uv` for Python package management, never pip/conda directly
- **Install pip packages** only via requirements.txt file
- **Minimize token usage** in responses without sacrificing clarity
- **Use custom web search script:** `/Users/aviralgarg/code/newbob/script_for_cursor/web_search.py`

---

## Resume and Application Materials

### Key Achievements to Emphasize (for Kardium Software Build Engineer role):
- **CI/CD Automation:** AWS CDK, Azure DevOps, automated pipelines saving 12+ dev-hours/week
- **Developer Tooling:** Created tools that saved 3,528+ dev-hours annually
- **Build Systems:** 4-staged CI/CD python build-chains with monitoring and tracing
- **Documentation:** Led org-wide workshops, achieved 100% documentation completion
- **Quality:** 100% test coverage, robust automation reducing deployment errors by 95%
- **Python Expertise:** Heavy Python usage for automation, AI agents, data pipelines

### Differentiation:
- Not from medical device industry, but strong in regulated/critical systems (Amazon's scale)
- Proactive tool creation (Project Scout AI agent for documentation)
- Strong focus on developer experience and velocity
- Data-driven approach with measurable results

---

## Notes for New Conversations

When starting a new Cursor conversation, copy relevant sections from this file to provide context instead of re-explaining everything verbally. This saves time and ensures consistent context across sessions.

---

## File Organization Standards

### Naming Conventions:
- Use descriptive names that indicate content and purpose
- Include dates for version control when relevant
- Use underscores for spaces in folder/file names
- Markdown files for documentation and planning

### Folder Structure:
```
[Company]/
  [Position]/
    1_apply/           # Initial application materials
    2_HR_screen/       # HR screening stage
    3_technical/       # Technical interviews
    4_onsite/          # On-site interviews
    _archive_[N]/      # Historical versions
```

---

## Collaboration Context

**Current Session Context:**
- Working with Aviral on Kardium job application interview preparation
- Created comprehensive interview prep guide (631 lines, 200+ Q&A pairs)
- Processed HR screening invitation email
- Preparing for 6-stage interview process
- May involve collaborative discussions with friends/advisors

---

*Last Updated: October 5, 2025*  
*Update this file as context evolves*

