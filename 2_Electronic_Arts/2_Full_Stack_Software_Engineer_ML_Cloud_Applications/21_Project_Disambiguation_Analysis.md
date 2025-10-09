# Project Disambiguation: Scott vs Virtual Try-On
**Date:** October 8, 2025  
**Purpose:** Clarify two SEPARATE Amazon Beauty Tech projects that may have been conflated

---

## THE PROBLEM

Files 16 and 17 (Interview_Prep_Comprehensive_Guide.md and Project_Story_Details.md) may have mixed details from TWO DIFFERENT projects:

1. **Project Scott** - AI documentation Q&A system
2. **Virtual Try-On (VTO) Project** - Visual property extraction for AR try-ons

---

## EVIDENCE FROM FILE 14 (ChatGPT Conversation)

**File 14 contains ENTIRE conversation about ONE project only:**

### Project Described in ChatGPT Conversation (File 14)
- **Name:** Virtual Try-On Project / Visual Property Extraction
- **Goal:** Extract visual properties from product images for AR try-ons
- **Problem:** Replace costly third-party tool, non-standard product photo submissions
- **Tech Stack:** 
  - SageMaker Ground Truth for data labeling
  - Data scientists/applied scientists creating models
  - Bounding boxes and color extraction
  - Pipeline from product catalog → visual properties → 3D assets → rendering
- **Team Structure:**
  - Interactive Experience team (your team) - data capture & visual property extraction
  - Customer Experience team - front-end UX
  - Rendering team - applied scientists, technical artists, AR face tracking
  - 3D Asset Creation team - external to Beauty Tech
- **Your Role:** Technical lead for overall pipeline
- **Collaboration:**
  - Worked with "bridge teams" interfacing with beauty brand clients
  - Guided product photo submission process improvements
  - Worked with design artists and computer vision experts
  - Collaborated with data scientists, applied scientists, technical artists
  - Resolved disconnects with downstream teams (3D asset creation)
- **Approach:**
  - Conducted double-blind experiments with people of different demographics
  - Worked backward from real problems
  - Established standards for future (naming conventions, photo standards, RGB values)
  - Balanced work between product owners and internal teams
- **Impact:** Created standardized workflows, improved data quality

**NOTABLE:** There is NO mention of:
- "Project Scott" by name
- AI documentation Q&A system
- Internal documentation agents
- Ticketing system integration
- 82% resolution time improvement
- 240 dev-hours/month saved
- 100% documentation coverage

---

## EVIDENCE FROM SCRIBD PREP FILE

**From `/Users/aviralgarg/code/career-automation/13_Scribd/1_Software_Engineer_II_Backend_Data_pipelines/3_Recruiter_Screen_Prep_Guide.md`:**

Line 77-78 mentions:
> "it essentially we built started off with this VTO project, the virtual try on project and it kind of led into creating a big beauty tech data lake"

**This confirms VTO is a SEPARATE project from what's typically called "Project Scott"**

---

## EVIDENCE FROM EA RECRUITER SCREEN (File 10)

**Lines 125-126 in File 10 mention:**
> "There was one project I would quickly mention would be Project Scott, where I developed internal AI agents on internal documentation."

**Key details about Project Scott from File 10:**
- AI agents powered by internal documentation
- Answered technical questions (CI/CD, admin questions)
- For new/onsite engineers joining BeautyTech team
- AI agent called "Project Scott" - people would "talk to Project Scott"
- Recognized topics, looked up documentation, provided immediate answers
- If didn't find everything, contacted subject matter expert, did documentation, responded back
- Attached to internal ticketing system
- "Reached 100% documentation"
- Improved resolution time 82%
- Saved 240 dev-hours/month

---

## DISAMB

IGUATION: TWO SEPARATE PROJECTS

### PROJECT 1: Project Scott (AI Documentation Q&A)
**Description:** AI agent for answering team questions from internal documentation  
**Problem:** New/onsite engineers needed instant answers to CI/CD/admin questions; docs were scattered  
**Technologies:**
- RAG pipeline
- AI agents / chatbot interface
- Vector databases / embeddings
- SageMaker for model hosting (inference)
- Internal ticketing system integration
- Lambda, API Gateway (likely)
- DynamoDB for session/state (likely)
- CloudWatch/X-Ray monitoring

**Key Features:**
- Natural language Q&A on internal docs
- Automatic subject matter expert escalation
- Automated documentation creation
- Ticketing system integration

**Your Role:** Built the AI agent system, drove adoption

**Impact:**
- 82% faster resolution time
- 240 dev-hours/month saved
- 100% documentation coverage

**Collaboration:**
- Worked with engineers, subject matter experts
- Led org-wide documentation workshop

---

### PROJECT 2: Virtual Try-On / Visual Property Extraction
**Description:** Data pipeline extracting visual properties from product images for AR try-ons  
**Problem:** Replace costly third-party tool, non-standard product photo submissions  
**Technologies:**
- SageMaker Ground Truth (data labeling)
- Custom ML models (bounding boxes, color extraction)
- Event-driven pipeline (product catalog changes)
- Step Functions + Lambda orchestration (likely)
- DynamoDB / S3 for data storage
- AWS CDK + CloudFormation
- Integration with 3D asset generation and AR rendering

**Key Features:**
- Automated visual property extraction (colors, attributes)
- Standardized product photo submission workflow
- End-to-end pipeline: catalog → properties → 3D assets → rendering
- Double-blind validation experiments

**Your Role:** Technical lead for overall pipeline (data capture through visual property extraction)

**Impact:**
- Replaced third-party tool
- Established organization-wide standards (naming, photo standards, RGB values)
- High data quality
- Processed 40TB/day serving 40M+ customers (this metric may be from larger Beauty Tech data lake)

**Collaboration:**
- Bridge teams (interface with beauty brand clients)
- Data scientists, applied scientists
- Technical artists (rendering team)
- Design artists, computer vision experts
- 3D asset creation team
- Customer Experience team (front-end)

---

## THE CONFUSION IN CURRENT FILES

**Files 16 and 17 may have mixed these projects because:**

1. **Both used SageMaker** - but for different purposes
   - Project Scott: Model hosting for AI Q&A
   - VTO: Model training AND inference for visual property extraction

2. **Both had "pipeline" components**
   - Project Scott: RAG pipeline for documentation Q&A
   - VTO: Data pipeline for visual property extraction

3. **Both involved collaboration**
   - Project Scott: Engineers, subject matter experts
   - VTO: Technical artists, data scientists, designers, external teams

4. **Both had significant impact**
   - Project Scott: 82% improvement, 240 dev-hrs saved, 100% docs
   - VTO: Replaced third-party tool, established standards, processed 40TB/day

---

## WHICH PROJECT TO USE FOR EA INTERVIEW?

### For "End-to-End ML Cloud Application" Question
**Use: Project Scott (Documentation AI Agent)**

**Why:**
- Cleaner "end-to-end" narrative (problem → solution → impact)
- More straightforward architecture to explain in 30-45 seconds
- Clear ML/AI focus (RAG pipeline, LLM integration)
- Specific, impressive metrics (82%, 240 dev-hrs, 100%)
- Less complex team structure (easier to explain quickly)
- Tyler already heard this one and was impressed

**30-45 second version:**
- Problem: Engineers needed instant answers, scattered docs
- Architecture: RAG pipeline, API Gateway + Lambda, SageMaker, DynamoDB, CloudWatch
- Role: Built AI agent, drove adoption, ticketing integration
- Impact: 82% faster, 240 dev-hrs saved, 100% docs

### For "Cross-Functional Collaboration" Question
**Use: Virtual Try-On Project**

**Why:**
- More collaboration examples (5+ different teams/disciplines)
- Technical artists explicitly mentioned (BIG PLUS for EA)
- Shows working backward from customer needs
- Demonstrates standards creation and long-term thinking
- External team coordination (3D asset creation)
- Bridge between technical and creative

**Can also mention:** Briefly reference Project Scott as secondary example if needed

---

## FILES NEEDING UPDATES

### File 16: Interview_Prep_Comprehensive_Guide.md
**Current status:** May have conflated projects  
**Needs:**
- Q1 answer (End-to-End ML Cloud App) → Use Project Scott details ONLY
- Q2 answer (Cross-Functional Collaboration) → Use VTO project details ONLY
- Clearly label which project in each answer
- Keep them as TWO separate stories

### File 17: Project_Story_Details.md
**Current status:** May be mixing project details  
**Needs:**
- Separate into TWO sections:
  - **Section A: Project Scott (AI Documentation Q&A)**
  - **Section B: Virtual Try-On (Visual Property Extraction)**
- Each with own 30-45 second version
- Each with own expansion details
- Clear guidance on when to use which

### File 10: Recruiter Screen Transcription
**Status:** ✅ CORRECT - Already has both projects separated
- Lines 125-126 mention Project Scott
- This is SOURCE OF TRUTH

---

## NEXT ACTIONS

1. ✅ Created this disambiguation analysis
2. ⏳ Update File 16 (Interview Prep Guide) - separate the two projects
3. ⏳ Update File 17 (Project Story Details) - create two sections
4. ⏳ Verify no other files have conflated these projects

---

## RECOMMENDED STRATEGY FOR EA INTERVIEW

**Primary Story: Project Scott**
- Use for "End-to-End ML Cloud Application" question
- Clean, clear, impressive metrics
- Tyler already heard it and liked it

**Secondary Story: Virtual Try-On**
- Use for "Cross-Functional Collaboration" question
- Emphasize technical artists, multiple teams
- Shows standards creation and long-term thinking

**Both are legitimate, impressive projects. Keep them separate and use strategically.**

