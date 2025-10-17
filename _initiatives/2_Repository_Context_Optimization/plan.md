# Initiative #2: Repository Context Optimization
**Goal:** Reduce token count in company folders while preserving critical information  
**Created:** October 17, 2025  
**Status:** Planning

---

## Problem Statement

The `_companies/` folder contains extensive interview prep materials, transcripts, analyses, and documentation across 17+ companies. When AI assistants (like this one) need context about a specific company, they must read many large files, consuming significant tokens. This:

1. **Slows down AI responses** (more files to read)
2. **Increases costs** (token usage)
3. **Dilutes focus** (important info buried in verbose files)
4. **Makes context management harder** (exceeds context windows)

---

## Objectives

1. **Reduce total token count by 40-60%** in company folders while preserving all critical information
2. **Improve AI context efficiency** - Key info accessible in fewer tokens
3. **Maintain discoverability** - Don't lose important details
4. **Create reusable patterns** - Apply learnings to future applications

---

## Strategy Overview

### Phase 1: Audit & Analyze
- Identify highest-token files across all companies
- Categorize content types (transcripts, prep guides, analyses, assets)
- Determine what's essential vs. archivable

### Phase 2: Optimize Structure
- **Transcripts:** Create executive summaries, move full transcripts to `_ASSETS/`
- **Prep Guides:** Extract reusable templates to `_reference/`, leave company-specific content
- **Analysis Documents:** Consolidate learnings into master files
- **Redundant Content:** Identify and deduplicate

### Phase 3: Implement & Validate
- Execute optimizations systematically
- Test AI context retrieval (verify no critical info lost)
- Document patterns for future applications

---

## Detailed Action Plan

### Task 1: Token Audit
**Goal:** Understand current state

**Actions:**
1. Create Python script to count tokens per file (using tiktoken or similar)
2. Generate report:
   - Total tokens per company folder
   - Top 10 highest-token files
   - Content type breakdown (transcript vs. prep vs. analysis)
3. Identify optimization opportunities

**Output:** `token_audit_report.md` with data-driven insights

---

### Task 2: Create Company Context Summaries
**Goal:** Compress essential info into concise summaries

**Actions:**
1. For each company, create `_COMPANY_SUMMARY.md`:
   - Company overview (1-2 paragraphs)
   - Role applied for (1 paragraph)
   - Current status (1-2 sentences)
   - Key interview insights (bullet points)
   - Next steps (bullet points)
   - Important files reference (if need details)
2. Target: 200-500 tokens per summary (vs. 5K+ tokens reading all files)

**Output:** `_COMPANY_SUMMARY.md` in each company's role folder

---

### Task 3: Optimize Transcripts
**Goal:** Preserve insights, reduce verbosity

**Actions:**
1. For each interview transcript:
   - Extract key Q&A, important topics discussed, interviewer feedback
   - Create `[N]_interview_key_points.md` (condensed version)
   - Move full transcript to `_ASSETS/` as `[N]_interview_full_transcript.md`
2. Link condensed version to full transcript for reference
3. Target: 80% token reduction while keeping all insights

**Output:** Condensed interview summaries, full transcripts archived

---

### Task 4: Template Extraction
**Goal:** Reduce duplication across companies

**Actions:**
1. Identify common patterns across prep guides:
   - Recruiter screen prep structure (similar across all companies)
   - Interview analysis frameworks (reusable)
   - Question banks (consolidate)
2. Move templates to `_reference/templates/`
3. Company-specific files reference templates + add unique content only

**Output:** `_reference/templates/` with reusable prep structures

---

### Task 5: Consolidate Learnings
**Goal:** Avoid reading same insights multiple times

**Actions:**
1. Already have `INTERVIEW_LEARNINGS_MASTER.md` in `_reference/`
2. Audit individual company "learning points" files
3. Extract unique insights to master file
4. Remove redundant learning files (or reduce to 1-2 sentences + link to master)

**Output:** Enhanced master learnings file, reduced duplication

---

### Task 6: Archive Low-Priority Content
**Goal:** Move non-essential content out of main context

**Actions:**
1. Identify companies with low priority (rejected, no response, old applications)
2. Create `_archive/companies_inactive/` folder
3. Move low-priority companies there (still accessible but not in main `_companies/`)
4. Criteria: No interview in 2+ months, rejected, or deprioritized

**Output:** Reduced active company count, cleaner focus

---

## Success Metrics

### Quantitative:
- **Token reduction:** 40-60% decrease in total tokens across `_companies/`
- **File count:** 30-50% fewer files in active company folders
- **Summary coverage:** 100% of active applications have company summary

### Qualitative:
- **AI efficiency:** Can understand company status in 1 file read vs. 10+
- **No information loss:** All critical details preserved (in summaries or linked)
- **Maintainability:** Future applications follow optimized pattern

---

## Risks & Mitigations

### Risk 1: Losing Important Details
**Mitigation:** Never delete, only archive. Full transcripts always accessible in `_ASSETS/`

### Risk 2: Over-Summarization
**Mitigation:** Test summaries with AI queries ("What's my Scribd status?") - if can't answer from summary, expand it

### Risk 3: Time Investment
**Mitigation:** Automate where possible (token counting, file moving). Prioritize high-token companies first (80/20 rule)

---

## Implementation Timeline

**Week 1:**
- Task 1: Token audit (2 hours)
- Task 6: Archive inactive companies (1 hour)

**Week 2:**
- Task 2: Create summaries for top 5 active companies (3 hours)
- Task 3: Optimize transcripts for top 5 (2 hours)

**Week 3:**
- Task 4: Extract templates (2 hours)
- Task 5: Consolidate learnings (1 hour)

**Week 4:**
- Complete remaining companies (3 hours)
- Validation & documentation (1 hour)

**Total Estimated Effort:** 15-20 hours

---

## Next Steps

1. **Immediate:** Run token audit script
2. **Quick win:** Archive inactive companies (immediate token reduction)
3. **High impact:** Create summaries for top 5 active (Scribd, Kardium, Vooban, Cresta, EA)

---

## Notes

- This initiative pairs well with Initiative #1 (Learning About Aviral Garg) - both optimize AI context
- Can apply learnings from this to future job applications (start with optimized structure)
- Consider creating a "context budget" - each company gets max 2K tokens in main folder, rest archived

---

**Status:** Ready to execute. Awaiting approval to start with Task 1 (Token Audit).

