# EA Technical Interview - Cleaned Transcript
**Date:** Oct 9, 2025, 1:00 PM PDT  
**Candidate:** Aviral Garg  
**Interviewers:** Rhea Lauzon (Tech Director SRE), Blaze Wallber (Director Ops & Tech), Daniel Arguedas (Tech Lead)  
**Position:** Full Stack Software Engineer - ML Cloud Applications

---

## Opening & Introductions

**Rhea:** Launching Battlefield 6 tomorrow. Big energy, calm before storm. Expecting some chaos but excited.

**Blaze:** Director of Operations & Technology for marketing group at EA. Oversees operations tools and workflows for content delivery through artist teams.

**Daniel:** Tech lead on Blaze's team. Focus on tools and automations for artist productivity. Work with Frostbite engine, creating plugins/add-ons. Heavy on game capture and gameplay capture tools. Part of craft group generating trailers, screenshots, gameplay shots. Growing team to explore AI/ML solutions.

**Rhea:** Technical Director of Site Reliability Engineering in marketing org (separate from Blaze/Daniel's team). Operates EA app (e-commerce competitor to Steam) and social destinations. Here to help build new team arm from technical perspective - cloud scaling and reliability.

**Aviral:** Full-stack software engineer. 5 years Amazon, 1 year T4G (consultancy), multiple UBC internships and projects. Specialize in cloud-native ML applications on AWS. Led team of 8 engineers at Amazon Beauty Tech building AI-powered systems processing 40TB+ data, serving 40M+ monthly customers across 15 countries. Technical foundation: Python, AWS serverless (Lambda, SageMaker, API Gateway, DynamoDB), Infrastructure as Code (CDK, CloudFormation). Enjoy cross-functional collaboration with designers, data engineers, applied scientists, PMs, technical artists. Excited about EA because of perfect technical match and genuine enjoyment working with creative teams. FIFA fan, appreciate EA legacy. At bleeding edge of NLP/AI tools while being cautious about disadvantages.

---

## Project Discussion: Virtual Try-On (VTO)

**Daniel:** Asks about projects - were they maintenance or new builds?

**Aviral VTO Context:** Built from scratch. Amazon app feature: select lipstick → virtual try-on button → camera opens with AR → see lipstick on your face in real-time.

**Problem:** Third-party solution was expensive, non-extensible (wanted foundations/eyeliners), slow turnaround (bulk image processing), lack of control.

**Solution:** Proposed and led project to build in-house replacement.

**Daniel:** Asked for challenges and architectural details.

**Aviral Architecture:**
- Consumed entire Amazon product catalog
- Created data pipelines extracting/filtering lipstick images
- Extracted RGB colors and visual properties (finish types, particles)
- Evaluated 3 designs (ML Pigeon - internal framework; AWS Native Pipelines; **Step Functions + Serverless**)
- **Recommended:** Step Functions architecture built with AWS CDK/CloudFormation
- **Components:** Lambda, Athena, SQS, SNS, DynamoDB triggers
- **Pattern:** Event-driven serverless batch processing
- **Dual purpose:** Data generation for ML training AND production serving
- **Process:** 
  1. Initial: Send images to human data labelers for bounding boxes/color extraction
  2. Later: Trained ML models, replaced human step with SageMaker endpoints for batch processing
  3. Extracted colors, finish types, particles automatically

**Challenges:**
- Garbage in/garbage out with bad data
- Text issues: "unicorn red" color names (how to extract RGB?)
- Image issues: lighting variations causing wrong color detection (nail polish appearing yellowish when actually orange)
- Solution: modular design allowing plug-and-play of ML models
- Extended beyond lipsticks to foundations, eyeliners, bronzers

**Blaze:** How did you handle data quality - set parameters for storefront owners or retrofit solution?

**Aviral:** Both approaches. Worked backward from problem. During specific times of year, could change data submission requirements from brands (Maybelline, L'Oréal, etc.). Changes would take ~1 year. Meanwhile, built pipeline to handle existing data. Worked with artists and computer vision scientists on standards. Showed brands how to calculate correct RGB at source. Created pipeline achieving 93% success with existing data. After standards changed, pipeline remained essential because not all brands followed guidelines. Pipeline: filtered products → organized images → classification/categorization → automated data labeling → structured/unstructured data storage → event notifications → model creation → serving. Also served as data lake for sister teams (recommendations, front-end).

---

## Project Discussion: Project Scott

**Aviral Context:** Prototype addressing internal documentation complaints. Slack-integrated AI assistant.

**Functionality:**
- User asks question in Slack
- NLP/LLMs identify related topics
- RAG (Retrieval Augmented Generation) with Pinecone vector database
- Returns relevant documentation

**Innovation - Documentation Ownership:**
- Organization-wide initiative: every project has documentation owner (same as project owner)
- 3 workshops to establish 100% documentation coverage
- New team members know who to contact for any topic

**Smart Features:**
- Partial/zero match: Scott contacts subject matter experts
- Asks specific sub-questions (only missing parts, not full copy-paste)
- SMEs respond, Scott suggests documentation updates (one-click approval)
- Proactive agent mode: simulates new team member, asks questions to find documentation gaps

**Blaze:** How handle legacy data and old archives?

**Aviral:** Early prototype stage with challenges. Heavy red-teaming. Scott initially "bugged" developers frequently. Learned patterns: similar questions → similar documentation gaps → similar mistakes. System learned optimal suggestions and which SMEs to contact. Automated routing instead of sending everything to lead developer.

**Key Learning:** Don't create custom ML models. OpenAI/Anthropic do excellent job. Use local versions (AWS Bedrock) or smaller models (Ollama). Start simple, focus on prompt engineering. Became agentic handoff framework project vs custom ML model development.

---

## Unity/Game Development Experience

**Daniel:** Experience with Unity or 3D vector math?

**Aviral:** University and personal projects (no professional experience):

**UBC Capstone:** HoloLens mixed reality with neuroscientists. Unity-based app comparing normal brain vs diseased brain. Created front-end, back-end, automated smoke testing.

**Memory Palace VR:** Japanese language learning in virtual reality (Unity 3D). Hiragana characters placed as memorable objects in palace (e.g., key character looks like actual key → giant key placed in palace). Also learned first 50 periodic table elements this way. Combined backend with Unity front-end: Google APIs for dynamic image search while wearing VR headset → create/place 3D models in real-time. Platform for developers to submit 3D models with automatic population to local library.

---

## Scalability Deep-Dive with Rhea

**Rhea:** 40TB data catalog per day - scaling issues in pipeline/lambdas/step functions?

**Aviral:** Definitely had scaling issues early. Time-boxed exploration of available tools (Glue, Data Pipelines, etc.). Many failed scaling test or became too expensive. Looked for out-of-box solutions by changing data source format. Streaming data available (AWS Kinesis) but too expensive and unnecessary. **Solution: Parquet format with Athena**. Athena enabled ETL pipeline with SQL queries on S3 data - flexible, cost-effective. Avoided complex data engineering requirements. Worldwide expansion: multiple countries, data in S3 buckets, Athena queries handled everything cleanly. Simplified approach vs over-engineering.

**Rhea:** Issues 70-80% through implementation or after feature complete?

**Aviral:** Japan expansion: results suddenly garbage. Yellow lipsticks generating black 3D models. Root cause: certain brand used honey bee in images. Black/yellow bee caused color averaging issues. More extensibility problem than scaling. Happy to say no major late-stage scaling failures due to upfront planning.

**Rhea:** How designed scalability? Requirements or benchmarking?

**Aviral Operational Readiness:**
- Amazon practice: Operational Readiness Review (ORR) before implementation
- Checklist covering failure scenarios:
  - Upstream data failure: backup mechanisms
  - Lambda cold starts: mitigation strategies
  - Lambda non-responsive: avoid cost waste from spam retries
- Introduced exponential backoff (new Step Functions feature at the time)
- X-ray for bottleneck tracking
- Design principles: keep modular for plug-and-play, maintain full control
- Chose "Design 3" (Step Functions) to avoid handing off to other teams
- Cost-conscious with worldwide expansion in mind
- Started US marketplace → Japan → Europe → Asia → Mexico
- Contracts between sub-components with best practices:
  - Backoff mechanisms
  - Bottleneck tracking
  - Comprehensive logging
  - Quick debug capabilities
- Documented everything thoroughly

**Rhea:** "That is a very good answer."

---

## Team Structure & Role Context

**Blaze:** Marketing group creates content for entire EA portfolio (all franchises). Content types: screenshots, cinematic videos, capture trailers, live action.

**Tech group split into 2 functions:**
1. **Tech designers:** Pipeline efficiency, day-to-day project support. First responders to artist technical issues.
2. **Software engineering:** Forward-thinking, laying groundwork for tools. Recurring tech designer issues ticketed to software engineering for long-term solutions.

**Goal:** Make content creation more efficient through collaboration.

**Experiences org:** Massive collective of technical people, artists, programmers, brand folks, publishing folks. Everything surrounding games at EA.

---

## Aviral's Question: What Does Success Look Like?

**Daniel's Answer:**
- Support creators, optimize creation tools
- Expanding to new tools: production tracking, automated document generation (brand/legal briefs), automatic render validation (logo sizes, proportions, colors)
- Need AI-versed developers to explore ML model applications
- **Success criteria:**
  - **Autonomy:** No ML experts currently on team (focused on artist workflow tools)
  - Understand user needs independently
  - Design optimal solutions
  - Preview risks, foresee scalability issues
  - Present long-term adaptable solutions
  - Establish new ways of solving problems through AI

**Blaze's Answer:**
- Collaborate with existing tech and artist teams
- Find smart scalability solutions through AI
- **New technology, loose guidance**
- Thought starter to guide next development phase
- What person makes of the role
- High curiosity within org about these products
- Looking for excitement about applying this tech
- Happy to experiment and pivot
- Be subject matter expert in room

**Rhea's Answer:**
- Not directly on team but sister org
- EA has central teams working heavily in AI/ML
- **Collaboration across teams critical:** share information, curiosity, learning, harvest ideas, unified direction
- **EA problem:** Teams in silos, duplicating work unknowingly (same as Amazon)
- Eager to teach, share, be involved
- Build healthy AI/ML community

**Daniel:** Success also = interface with existing talent, find right people, build bridges across teams for project growth.

---

## Aviral's Follow-Up: Metrics & Data Access

**Question:** Greenfield/moonshot project concerns:
- How define "done"?
- Can success be measured?
- Access to data on how content creators use tools?
- Programmatic access to understand pain points?

**Blaze's Answer:**
- **Metrics:** Time to create specific asset types
- Standardized workback schedules for all assets
- Goal: accelerate these timelines
- **Tracking:** All effort tracking in **Airtable**
- Improved tracking over last couple years
- "Art for commerce" = gray area but improving
- **Artist access:** Team small enough for direct observation. Artists sit right behind Blaze. Very collaborative space. Most tool users in Vancouver (plus sister studios).

---

## Advice for Starting in Role

**Daniel:** Don't be shy. Ask everyone in all directions. Find right people and resources. Many teams working on related tech. EA-wide AI resources and products for experimentation. Company exploring third-party vs in-house solutions. **Initial phase: explore everything to build map of available resources**, then design based on that.

**Aviral reflection:** Sounds like subject matter expert mapping initiative from Amazon. Right up alley: create from scratch, know resources, leverage appropriately, time-box exploration, work backward from pain points, create pipelines/processes fixing issues while maintaining scalability/extensibility mindset for large company.

**Rhea:** Same as described but bigger scale - cross-studio, cross-teams, different company wings. Bit intimidating but fun. Don't be shy, find your people. Everyone usually willing to share, especially if excited about work.

---

## Interview Close & Next Steps

**Daniel:** "Pretty good and satisfied with your presentation of your background, way of thinking. That's pretty much what we're looking for."

**Blaze:** "Really enjoyed our conversation today."

**Rhea:** Thanked for time.

**Next Steps (Daniel):**
- Recruiter (Tyler) will contact
- Likely scheduling **second panel interview**
- Interviewing multiple candidates but **"you fit very well on what we're looking for"**
- Similar format but **more technical**
- **Content:** Coding skills - half AI/ML, half general programming
- Questions about: sorting optimization, OOP implementation, design patterns
- Possibly architecture questions: how design app architecture, MVC, design patterns
- **Language:** Python sufficient. Not deep C++/memory management.
- **Daniel will coordinate with interviewers** to ensure appropriate difficulty level
- After 2nd panel: yes/no decision

**Daniel's final comment:** "We appreciate your time and your clear and friendly way of explaining things. Hope we see you again in not a long time."

---

## Key Insights

**Strong signals:**
- Daniel: "you fit very well on what we're looking for"
- Rhea deeply engaged on scalability (her focus area)
- Blaze connected on documentation pain point
- All three appreciated clear communication and thought process

**Role requirements:**
- Autonomy in AI/ML space (no existing experts on immediate team)
- Cross-team collaboration and bridge-building
- Scalability-first mindset
- Forward-thinking tool development
- Subject matter expertise
- Teaching and knowledge sharing

**Cultural fit indicators:**
- "Don't be shy" mentioned multiple times
- Value exploration and experimentation
- Appreciate thoroughness (ORR, checklists)
- Working backward from problems
- Modular, extensible designs

**Technical alignment:**
- AWS serverless architecture (exact match)
- ML pipeline experience (VTO project)
- Agentic AI/RAG experience (Project Scott)
- Infrastructure as Code (CloudFormation/CDK)
- Cross-functional technical leadership
- Operational readiness mindset


