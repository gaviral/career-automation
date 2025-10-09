# Project Story Details - TWO SEPARATE PROJECTS
**Amazon Beauty Tech Projects**

---

## ⚠️ CRITICAL: THESE ARE TWO DIFFERENT PROJECTS

Based on File 21 (Project Disambiguation Analysis), we have confirmed these are TWO SEPARATE projects that should NOT be conflated:

1. **Project Scott** - AI Documentation Q&A System
2. **Virtual Try-On (VTO)** - Visual Property Extraction for AR Try-Ons

---

# PROJECT 1: PROJECT SCOTT (AI Documentation Q&A)

## CORE STORY (30-45 seconds version)

**Situation:** Built AI agent system to answer team questions from internal documentation within Amazon Beauty Tech.

**Problem:** New/onsite engineers needed instant answers to CI/CD/admin questions; documentation was scattered across multiple sources.

**Architecture:**
- **RAG Pipeline:** Vector embeddings, document retrieval, LLM-powered Q&A
- **API Layer:** API Gateway + Lambda for orchestration
- **ML/AI:** SageMaker for model hosting (inference endpoints)
- **Storage:** DynamoDB for session state, S3 for document storage
- **Integration:** Internal ticketing system integration
- **Infrastructure:** AWS CDK + CloudFormation, 4-staged CI/CD
- **Monitoring:** CloudWatch + X-Ray for observability

**Role:** Built the AI agent system, drove org-wide adoption, integrated with ticketing.

**Key Features:**
- Natural language Q&A interface ("Talk to Project Scott")
- Automatic subject matter expert escalation if answer not found
- Automated documentation creation and updates
- Ticketing system integration

**Impact:**
- **82% improvement** in resolution time
- **240+ dev-hours/month saved**
- **100% documentation coverage** (led org-wide documentation workshop)

*[Stop here - offer to elaborate if they want details]*

---

## EXPANSION DETAILS (If Asked to Elaborate)

### Problem Context
- Engineers joining Beauty Tech team had many technical questions
- Documentation scattered across wikis, Slack, individual knowledge
- Manual Q&A process was time-consuming
- Subject matter experts repeatedly answering same questions

### Technical Implementation
- **RAG (Retrieval Augmented Generation) pipeline**
- **Vector database** for document embeddings
- **LLM integration** for natural language understanding and response generation
- **Automated escalation:** If AI couldn't find answer, contacted subject matter expert
- **Documentation loop:** SME responses fed back into documentation, improving coverage over time

### Cross-Team Collaboration
- Worked with **engineers** across Beauty Tech
- Collaborated with **subject matter experts** in various domains (CI/CD, infrastructure, admin)
- Led **org-wide documentation workshop** to improve coverage
- **Integrated with ticketing system** for seamless workflow

### Key Decisions
1. **Named it "Project Scott"** - anthropomorphized AI to encourage adoption
2. **Ticketing integration** - made it part of existing workflow
3. **Documentation feedback loop** - continuously improved knowledge base
4. **SME escalation** - balanced automation with human expertise

### Metrics & Impact
- **82% faster** resolution time for technical questions
- **240+ dev-hours/month saved** across organization
- **100% documentation completion** for Beauty Tech team
- **High adoption rate** - became go-to resource for new/existing engineers

---

## WHICH VERSION TO USE WHEN

### For "End-to-End ML Cloud Application" Question
→ Use **PROJECT SCOTT** - cleaner narrative, clear ML/AI focus, impressive metrics

### For "AI/ML in Production" Question
→ Use **PROJECT SCOTT** - demonstrates RAG, LLM integration, production deployment

### For "Documentation/Team Knowledge" Question
→ Use **PROJECT SCOTT** - led org-wide workshop, 100% documentation coverage

---

# PROJECT 2: VIRTUAL TRY-ON (VTO) - VISUAL PROPERTY EXTRACTION

## CORE STORY (30-45 seconds version)

**Situation:** Led visual property extraction pipeline within Amazon Beauty Tech for AR virtual try-on experiences.

**Problem:** Needed to replace costly third-party tool; non-standard product photo submissions from beauty brands caused inconsistent data quality.

**Architecture:**
- **Data Ingestion:** Event-driven pipeline with AWS Step Functions + Lambda for product catalog changes
- **ML Pipeline:** SageMaker Ground Truth for data labeling, custom models for bounding boxes and color extraction
- **API Layer:** API Gateway + Lambda for orchestration
- **Storage:** DynamoDB for session state, S3 for data artifacts
- **Infrastructure:** AWS CDK + CloudFormation, 4-staged CI/CD
- **Monitoring:** CloudWatch + X-Ray for observability

**Role:** Technical lead for overall pipeline - owned architecture, planning, execution. Consulted senior engineer for design review.

**Collaboration:** Worked with technical artists (rendering team), designers, data scientists, 3D asset creation team, PMs, beauty brand bridge teams.

**Impact:**
- Replaced third-party tool successfully
- Established standardized data workflows organization-wide
- Created naming conventions and photo standards for future beauty brand partners
- High data quality for AR try-on experiences
- Part of larger Beauty Tech data lake processing **40TB/day serving 40M+ monthly customers**

*[Stop here - offer to elaborate if they want details]*

---

## EXPANSION DETAILS (If Asked to Elaborate)

### Team Structure & Ownership
- **Beauty Tech Organization** split into:
  - **Interactive Experience** (Your team) - Data capture and visual property extraction
  - **Customer Experience** (Sister team) - Front-end UX, before/after UI features
  - **Rendering Team** (Applied scientists, technical artists) - Real-time AR rendering, face tracking
- **3D Asset Creation Team** - External to Beauty Tech, created 3D models
- **Your Role:** Technical lead for pipeline from product catalog → visual properties → (handed off to) 3D assets → rendering

### Problem Context
- **Initial Problem:** Non-standard product photo submissions from beauty brands (different lighting, angles, backgrounds)
- **Cost Issue:** Third-party tool was expensive
- **Quality Issue:** Inconsistent data quality affecting AR try-on realism

### Solution Approach - Working Backward
1. **Collaborated with "bridge teams"** who interfaced with beauty brand clients (L'Oréal, Maybelline, etc.)
2. **Improved product photo submission platform** - guided standardization of submission forms
3. **Created internal standards** for color value extraction (RGB values) and naming conventions
4. **Worked with design artists and computer vision experts** to optimize extraction algorithms
5. **Not just fixing present issues, but establishing standards for future partners**

### Technical Implementation Details
- **SageMaker Ground Truth:** Used data labelers to create bounding boxes inside product images (e.g., lipstick within packaging)
- **Experiments:** Conducted double-blind experiments with people of different gender and race wearing virtual lipsticks in demo app locally
- **Decision tree approach:** Early-stage data used for immediate averages, validated through real user experiments
- **Model Development:** Data consumed by data scientists and applied scientists to create in-house models for bounding boxes and color extraction
- **Event-driven:** Product catalog changes triggered pipeline automatically

### Cross-Team Collaboration Examples
1. **Technical Artists (Rendering Team):**
   - Regular syncs on visual calibration
   - Data-driven discussions on color accuracy (what RGB values look realistic in AR?)
   - Visual realism optimization for different skin tones

2. **Designers:**
   - UX collaboration for before/after slider feature
   - Visual property standards
   - Balance design goals with technical constraints

3. **Data Scientists / Applied Scientists:**
   - Model training collaboration (bounding box detection, color extraction)
   - Validation experiments
   - Face tracking and AR integration

4. **Product Managers:**
   - Requirements gathering (what properties do we need to extract?)
   - Worked backward from product vision (realistic AR try-on)
   - Multiple iterations to clarify disconnects

5. **3D Asset Creation Team (External):**
   - Guided overall direction (what data format do you need?)
   - Respected their expertise (they know 3D modeling)
   - Resolved disconnects with scheduled meetings (example: one instance where context was misunderstood about coordinate systems)

6. **Beauty Brand Bridge Teams:**
   - Improved product photo submission forms
   - Guided standardization of photo quality (lighting, angles)
   - Established best practices for RGB color values

### Leadership & Decision Making
- **Consulted senior engineer** for architecture design review, but **owned the overall project**
- **Decided to leverage partner teams' expertise** for later stages (3D asset generation by specialized team, rendering by applied scientists) - "didn't want to reinvent the wheel"
- **Still guided them at high level** to keep technical direction consistent (data formats, APIs, handoff points)
- **They didn't need day-to-day support** as they were domain experts

### Key Technical Decisions
1. **Not binding to current state:** Designed for future scalability (new beauty brands joining)
2. **Standardization:** Created naming conventions adopted organization-wide (how to name products, attributes)
3. **Working backward:** Focused on real problems (why are photos bad quality?) not just immediate symptoms
4. **Balance:** Split work between product owners (beauty brands improving submissions) and internal teams (extraction algorithms)
5. **Data quality:** Established best practices for RGB values, photo standards (lighting, resolution, angles)

### Metrics & Impact (Specific)
- **Replaced third-party tool** (cost savings)
- **Established standards** adopted across Beauty Tech organization
- **High data quality** validated through double-blind user experiments
- **Part of larger Beauty Tech data lake** processing **40TB/day**
- **Served 40M+ monthly customers** across 15+ countries
- **Created foundation** for future beauty brand partnerships (standardized onboarding)

---

## WHICH VERSION TO USE WHEN

### For "Cross-Functional Collaboration" Question
→ Use **VTO PROJECT** - 6 different teams/disciplines, technical artists (BIG PLUS for EA)

### For "Working with Technical Artists/Game Devs" Question
→ Use **VTO PROJECT** - rendering team collaboration, technical artists explicitly mentioned

### For "Standards Creation / Long-term Thinking" Question
→ Use **VTO PROJECT** - established org-wide standards for future partners

### For "Complex Pipeline" Question
→ Use **VTO PROJECT** - multi-stage pipeline across multiple teams

---

# USAGE STRATEGY FOR EA INTERVIEW

## Primary Story: PROJECT SCOTT
**Use for:** "End-to-End ML Cloud Application" question (Q1 - most likely)

**Why:**
- Cleaner "end-to-end" narrative (problem → solution → impact)
- More straightforward to explain in 30-45 seconds
- Clear ML/AI focus (RAG, LLM, SageMaker)
- Specific, impressive metrics (82%, 240 dev-hrs, 100%)
- Less complex team structure (easier to explain concisely)
- **Tyler already heard this one in recruiter screen and was impressed**

## Secondary Story: VTO PROJECT
**Use for:** "Cross-Functional Collaboration" question (Q2 - also very likely)

**Why:**
- More collaboration examples (6 different teams/disciplines)
- **Technical artists explicitly mentioned** (BIG PLUS for EA per Tyler)
- Shows working backward from customer needs
- Demonstrates standards creation and long-term thinking
- External team coordination (3D asset creation)
- Bridge between technical and creative

## Can Reference Both
If they ask multiple questions, you can reference both projects naturally:
- "I have another example of cross-functional collaboration from a different project..."
- Shows breadth of experience
- Both are legitimate, impressive projects at scale

---

# CRITICAL REMINDERS

- **BE CONCISE:** Start with 30-45 second version, offer to elaborate
- **WATCH CUES:** Stop when they say "Great" or "Perfect"
- **DON'T RAMBLE:** In recruiter screen you spent 2+ minutes when 30-45 seconds would work
- **LET THEM ASK:** Don't explain everything at once - answer the question, then pause
- **KEEP PROJECTS SEPARATE:** Don't mix Project Scott metrics with VTO project details

**Both projects demonstrate key competencies. Use strategically based on the question.**
