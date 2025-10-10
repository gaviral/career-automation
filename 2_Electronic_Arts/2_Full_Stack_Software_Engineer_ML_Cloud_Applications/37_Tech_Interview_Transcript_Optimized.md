# EA Technical Interview - Optimized Transcript
**Date:** Oct 9, 2025 | **Position:** Full Stack SW Engineer - ML Cloud  
**Interviewers:** Rhea Lauzon (SRE Tech Director), Blaze Wallber (Director Ops/Tech), Daniel Arguedas (Tech Lead)

---

## INTERVIEWERS

**Blaze Wallber** - Director Operations & Technology, Marketing
- Oversees operations tools/workflows for artist content delivery
- Focus: cross-functional collaboration, pipeline efficiency

**Daniel Arguedas** - Tech Lead (Hiring Manager)
- Tools/automations for artist productivity
- Frostbite engine plugins, game capture tools
- Craft group: trailers, screenshots, gameplay content
- Hiring for AI/ML exploration

**Rhea Lauzon** - Tech Director, Site Reliability Engineering
- EA app operations (e-commerce, social destinations)
- Here for: cloud infrastructure, scaling, reliability perspective

---

## AVIRAL'S BACKGROUND

**Experience:** 5yr Amazon Beauty Tech + 1yr T4G consultancy + UBC internships/projects

**Amazon Beauty Tech:** Led 8 engineers, AI systems processing 40TB/day, 40M+ customers, 15 countries

**Technical Stack:** Python, AWS serverless (Lambda, SageMaker, API Gateway, DynamoDB), IaC (CDK, CloudFormation)

**Collaboration:** Technical artists, designers, data scientists, PMs, cross-functional teams

**EA Interest:** Perfect technical match, enjoys creative team collaboration, FIFA fan

**AI/ML Approach:** Bleeding edge adoption, cautious about pitfalls

---

## PROJECT 1: VIRTUAL TRY-ON (VTO)

### Problem
Third-party AR lipstick try-on tool: expensive, non-extensible, slow (2-day turnaround), no control

### Solution Built
In-house replacement extracting RGB, finish types, particles from product images for 3D asset creation

### Architecture (Recommended Design #3)
- **Pattern:** Event-driven serverless batch processing
- **Stack:** Step Functions (CDK/CloudFormation), Lambda, Athena, SQS, SNS, DynamoDB
- **Data:** Parquet format with Athena SQL queries on S3
- **ML Pipeline:** Human labelers → SageMaker endpoints (replaced humans)
- **Scope:** Lipsticks → foundations, eyeliners, bronzers

### Key Challenges
1. **Data quality:** "Unicorn red" text, lighting variations in images
2. **Scaling:** Evaluated Glue, Data Pipelines, ML Pigeon (failed cost/scale tests)
3. **Athena solution:** Cost-effective ETL, avoided complex data engineering
4. **Japan expansion:** Honey bee in brand images caused black/yellow color averaging issues
5. **Vendor standards:** Worked with brands (Maybelline, L'Oréal) on RGB submission standards (1yr timeline), built pipeline for existing data (93% success)

### Operational Readiness
- ORR checklist: failure scenarios, backup mechanisms, cold start mitigation, exponential backoff
- X-ray bottleneck tracking
- Modular design: plug-and-play components, full control
- Worldwide expansion: US → Japan → Europe → Asia → Mexico
- Contracts between components, comprehensive logging, quick debug capability

### Impact
- Data lake for sister teams (recommendations, front-end)
- Extended to multiple product categories
- No late-stage scaling failures due to upfront planning

---

## PROJECT 2: PROJECT SCOTT

### Problem
Internal documentation complaints, knowledge gaps for new team members

### Solution
Slack-integrated AI assistant using NLP, RAG (Pinecone vector DB), LLMs

### Innovation: Documentation Ownership
- Org-wide initiative: every project has doc owner (same as project owner)
- 3 workshops → 100% documentation coverage
- New members know who to contact for any topic

### Features
- **Topic identification:** NLP classifies question topics
- **Partial/zero match:** Contacts SMEs with specific sub-questions (not full copy-paste)
- **Auto-update:** SMEs respond → Scott suggests doc updates (one-click approval)
- **Proactive agents:** Simulates new team member, finds documentation gaps preemptively

### Technical Approach
Early prototype with heavy red-teaming. System learned patterns, optimal suggestions, automated SME routing.

**Key Learning:** Don't build custom ML models. Use OpenAI/Anthropic (Bedrock local versions) or small models (Ollama). Focus on prompt engineering and agentic handoff frameworks.

---

## UNITY/GAME DEV EXPERIENCE

**UBC Capstone:** HoloLens mixed reality (Unity) for neuroscience - brain disease comparison. Front-end, back-end, automated smoke testing.

**Memory Palace VR:** Japanese language learning (Unity 3D). Hiragana characters as memorable 3D objects. Google API integration for dynamic image search in VR. Platform for developer 3D model submissions.

---

## SCALABILITY DISCUSSION (RHEA)

**Q:** 40TB/day - scaling issues in pipeline?

**A:** Early issues with Glue, Data Pipelines (cost/scale failures). **Athena + Parquet** solved: ETL via SQL on S3, avoided complex data engineering, cost-effective worldwide expansion.

**Q:** Issues 70-80% through implementation?

**A:** Japan expansion color issues (bee images). More extensibility than scaling. No major late-stage failures due to upfront planning.

**Q:** How designed for scalability?

**A:** Amazon ORR (Operational Readiness Review):
- Failure scenario checklists (upstream data, cold starts, non-responsive lambdas)
- Exponential backoff (new Step Functions feature)
- X-ray bottleneck tracking
- Modular plug-and-play design
- Cost-conscious with expansion roadmap
- Component contracts with best practices
- Comprehensive logging, quick debug paths

**Rhea:** "That is a very good answer."

---

## TEAM STRUCTURE & ROLE

**Marketing Group:** Content for entire EA portfolio (all franchises)
- Screenshots, cinematic videos, capture trailers, live action

**Tech Group (2 Functions):**
1. **Tech Designers:** Day-to-day artist support, first responders
2. **Software Engineering:** Forward-thinking tools, long-term solutions

**Experiences Org:** Massive collective (technical, artists, programmers, brand, publishing)

---

## SUCCESS CRITERIA (All 3 Interviewers)

### Daniel
- **Autonomy:** No ML experts on immediate team
- Understand user needs independently
- Design optimal solutions, preview risks, foresee scalability
- Establish new AI problem-solving approaches
- New use cases: production tracking, auto document generation (brand/legal briefs), render validation (logos, proportions, colors)

### Blaze
- Collaborate with tech/artist teams
- Find smart AI scalability solutions
- **Loose guidance, new technology**
- Be thought starter, guide next development phase
- High org curiosity about products
- Experiment, pivot, be SME in room

### Rhea
- **Collaboration across EA teams critical** (many AI/ML teams in silos)
- Share information, curiosity, learning
- Build healthy AI/ML community
- Interface with existing talent, build bridges

---

## METRICS & DATA ACCESS (BLAZE)

**Tracking:** Airtable - time to create asset types, standardized workback schedules

**Access:** Small team, direct observation (artists sit behind Blaze), collaborative Vancouver space

**Nature:** "Art for commerce" = gray area but improving tracking

---

## ADVICE FOR NEW HIRE (ALL 3)

**Daniel:** Don't be shy. Ask everyone. Find people/resources. Many teams on related tech, EA-wide AI resources/products. Company exploring third-party vs in-house. **Initial phase: explore everything, build resource map, then design.**

**Rhea:** Same but bigger scale - cross-studio, cross-teams, different wings. Intimidating but fun. People willing to share, especially if excited.

**Aviral reflection:** SME mapping from Amazon applies. Create from scratch, know resources, time-box exploration, work backward from pain points, maintain scalability/extensibility mindset.

---

## NEXT STEPS (DANIEL)

Tyler (recruiter) will contact for **second panel interview**

**Format:** Similar but **more technical**
- **Content:** Coding (50% AI/ML, 50% general programming)
- **Topics:** Sorting optimization, OOP, design patterns, app architecture (MVC), ML parameters/environment setup
- **Language:** Python sufficient (not deep C++/memory management)
- Daniel coordinating with interviewers on difficulty level

**Decision:** Yes/no after 2nd panel

**Feedback:** "You fit very well on what we're looking for" | "Clear and friendly way of explaining things" | "Hope we see you again in not a long time"

---

## KEY TAKEAWAYS

### Strong Signals
- Daniel: "fit very well," satisfied with background/thinking
- Rhea: deeply engaged scalability discussion (her area)
- Blaze: connected on documentation pain point
- All appreciated clear communication, thought process

### Role Requirements
- Autonomy (no existing ML experts on team)
- Cross-team collaboration, bridge-building
- Scalability-first mindset
- Forward-thinking tool development
- Subject matter expertise, teaching, knowledge sharing

### Cultural Fit
- "Don't be shy" (repeated emphasis)
- Value exploration, experimentation
- Thoroughness (ORR, checklists)
- Working backward from problems
- Modular, extensible designs

### Technical Alignment
- AWS serverless architecture (exact match)
- ML pipeline experience (VTO)
- Agentic AI/RAG (Project Scott)
- Infrastructure as Code
- Cross-functional technical leadership
- Operational readiness mindset

### Context
- **Battlefield 6 launching Oct 10** (day after interview)
- Hiring for multiple roles, org developing
- Team small, Vancouver-based, collaborative
- EA has multiple AI/ML teams (potential for silos)


