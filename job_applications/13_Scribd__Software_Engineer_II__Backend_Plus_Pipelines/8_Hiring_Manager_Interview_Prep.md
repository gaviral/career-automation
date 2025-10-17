# 🎯 HIRING MANAGER INTERVIEW PREP - Scribd
## Software Engineer II (Backend + Data pipelines)

**Interviewer**: Sachin (Senior Engineering Manager, 4+ years at Scribd)  
**Date**: Tuesday, Oct 15, 2025 @ 11:30 AM PST (2:30 PM EST)  
**Duration**: 30 minutes  
**Format**: Google Meet

---

## 🧠 GET INTO THE RIGHT MINDSET

### WHO THEY'RE LOOKING FOR:
- ⚡ **Backend + Data Engineering Expert** (unique combo)
- ⚡ **Large-scale distributed systems builder**
- ⚡ **Project leader** with storytelling skills
- ⚡ **Impactful engineer** (not just code, but business results)
- ⚡ **BONUS**: LLM/ML production experience

### CRITICAL REMINDER (Don't Repeat Vooban Mistake):
🚨 **ALIGN EVERY ANSWER TO JD REQUIREMENTS**
- This is a **Backend + Data Engineering role**
- Talk about: **pipelines, distributed systems, AWS, infrastructure**
- Use keywords: **Spark-like patterns, Terraform-equivalent (CDK), large-scale processing**
- Lead with: **40TB/day pipeline, 40M+ customers, metadata enrichment**
- NOT generic leadership stories - **tie everything to data/backend**

### YOUR COMPETITIVE ADVANTAGE:
- ✅ **Perfect tech stack match** (AWS Lambda/SageMaker/Step Functions = Scribd's AWS stack)
- ✅ **Exact scale experience** (40TB/day → hundreds of millions of documents)
- ✅ **BONUS qualification**: LLM/ML production (most candidates won't have this)
- ✅ **Built what they need**: Data lake consumed cross-org (exact Scribd use case!)

---

## 🎯 INTERVIEW STRUCTURE (30 MINUTES)

### What Sachin Will Evaluate:
1. **Technical Project Walk-through** (15-20 min)
   - Large-scale distributed systems
   - Backend + data engineering tech stack
   - Infrastructure-as-code
   - Challenges, trade-offs, architectural choices
   - **End result with metrics**

2. **Your Goals & Fit** (5 min)
   - What you're looking for (team culture, role type)

3. **Your Questions** (5-10 min)
   - Interest in Scribd, research depth

### What Makes Impact (Per Neha):
- ✅ **Impactful project** (first 15-20 min to make impression)
- ✅ **Compelling storytelling** (structured, not rambling)
- ✅ **Technical depth** (know your numbers, architecture decisions)
- ✅ **Genuine interest** (research, thoughtful questions)

---

## 🎤 PROJECT WALK-THROUGH: THE WINNING ANSWER

### **PRIMARY PROJECT: Beauty Tech Data Lake (40TB/day Pipeline)**

**Opening Statement** (30 seconds):
- *At Amazon, I* __led the design and build of our Beauty Tech data lake__
  - __Processing 40TB/day__ *of* __product catalog data__
  - __Serving 40M+ customers monthly__ *across* __15+ countries__
  - *It became the* __upstream data source__ *for* __multiple downstream teams__*:*
    - __Recommendations team__
    - __Customer experience team__
    - __Product managers__ *(natural language queries)*
  - __50% efficiency improvement__ *and* __$30K annual cost savings__

### **ARCHITECTURE** (The Technical Meat):

**Core Components:**
- __Distributed serverless pipeline__
  - **AWS Step Functions** *for* __orchestration__ *(Spark-like patterns)*
  - **Lambda** *for* __data processing__ *(auto-scaling)*
  - **DynamoDB** *for* __metadata storage__ *(high-throughput)*
  - **Athena** *for* __querying large datasets__ *(SQL on S3)*

- __Infrastructure-as-code__
  - **AWS CDK** *(equivalent to Terraform)*
  - __4-stage CI/CD pipeline__
  - __CloudWatch & X-Ray__ *for* __distributed tracing__

- __Data flow__
  - __Ingest__ → __Transform__ → __Enrich__ → __Serve__
  - __Visual properties extraction__ *(color, shimmer, texture from product images)*
  - __Metadata classification__ *(ML model integration)*

### **CHALLENGES & TRADE-OFFS**:

**Challenge 1: Inconsistent Data**
- **Problem**: No standard naming *("unicorn red", particle size "large/medium/small")*
- **Trade-off**: __Manual curation__ vs. __ML-automated extraction__
- **Decision**: __Hybrid approach__
  - __Computer vision models__ *for* __color/texture extraction__
  - __Human validation__ *for* __quality assurance__
- **Result**: __Accurate metadata__ *for* __AR try-on experience__

**Challenge 2: Scale & Cost**
- **Problem**: __40TB/day__ *growth*, __cost escalating__
- **Trade-off**: __Always-on infrastructure__ vs. __serverless__
- **Decision**: __Serverless (Lambda + Step Functions)__
  - __Auto-scaling__ *based on demand*
  - __Pay-per-use__ *pricing*
- **Result**: __$30K annual savings__, __handles growth automatically__

**Challenge 3: Cross-Team Consumption**
- **Problem**: Multiple teams *need* __different views of data__
- **Trade-off**: __Team-specific pipelines__ vs. __unified data lake__
- **Decision**: __Unified data lake__ *with* __flexible querying__
  - **Athena** *for* __SQL queries__
  - **Natural language interface__ *(for PMs)*
  - __Metadata APIs__ *(for downstream services)*
- **Result**: __One source of truth__, __reduced duplication__, __faster development__

### **IMPACT & RESULTS**:
- ✅ __Served 40M+ customers__ *monthly across* __15+ countries__
- ✅ __50% efficiency improvement__ *in data processing*
- ✅ __$30K annual cost savings__
- ✅ __Cross-org adoption__ *(recommendations, CX, product teams)*
- ✅ __Enabled AR try-on__ *(makeup products - COVID use case)*
- ✅ __Org-wide accolades__ *for* __operational readiness__

---

## 🎤 BACKUP PROJECT: AI Agent (If Time Permits or Asked)

**Project Scott - AI Documentation Agent:**
- __RAG pipeline__ *with* __vector databases__
- __Metadata extraction__ *from* __internal docs__
- __LLM-powered summarization, classification__
- __82% resolution time improvement__
- __240+ dev-hours saved/month__

**Why This Matters**:
- Scribd needs: "__LLM-powered metadata enrichment, summarization, classification, extraction__"
- I've done: "__Exactly this in production__"

---

## 🎤 WHAT YOU'RE LOOKING FOR (Team Culture / Role)

**When Sachin Asks: "What are you looking for?"**

**Your Answer** (Concise, 60 seconds):
- __Impactful work at scale__
  - *I love* __solving complex data challenges__ *that* __serve millions of users__
  - *Processing* __hundreds of millions of documents__ *is exactly the scale I thrive at*

- __Technical growth__
  - *I'm* __excited about the intersection__ *of* __ML, data engineering, and distributed systems__
  - *Learning* __Spark/Databricks__ *while leveraging my* __Step Functions/AWS experience__
  - *Deepening* __LLM integration__ *in production pipelines*

- __Collaborative team culture__
  - *I love* __working with cross-functional teams__ *(ML engineers, product, research)*
  - *At Amazon, I* __led 8-person teams__ *and* __org-wide initiatives__
  - *I value* __learning from others__ *and* __sharing knowledge__

- __Mission-driven**
  - *Scribd's mission to* __"spark human curiosity"__ *and* __democratize knowledge__ *resonates deeply*
  - __Content discovery__ *and* __trust__ *through high-quality metadata is meaningful work*

---

## ❓ QUESTIONS TO ASK SACHIN (CRITICAL - Shows Research & Interest)

### **MUST-ASK** (Pick Top 3):

1. ⭐ **"You mentioned the team works across all three products—Scribd, Everand, and Slideshare. How does the data pipeline differ across document types (ebooks vs. audiobooks vs. presentations)?"**
   - *Shows*: You listened to Neha, understand the scope
   - *Probes*: Technical depth of role

2. ⭐ **"I understand the team is driving AI initiatives at Scribd. What specific LLM use cases are you focusing on for metadata enrichment? Summarization, classification, or others?"**
   - *Shows*: Awareness of AI direction, your LLM expertise
   - *Probes*: How you can contribute immediately

3. ⭐ **"What's the biggest data engineering challenge the team is tackling right now? Is it scale, data quality, integration complexity, or something else?"**
   - *Shows*: Problem-solving mindset
   - *Opens*: Discussion of how your experience applies

### **GOOD-TO-ASK** (If Time):

4. **"How does the team balance moving fast on AI initiatives with ensuring data accuracy and quality at this scale?"**
   - *Connects to*: Your experience with validation, monitoring

5. **"What's the tech stack split between Python, Scala, and Ruby? Which would I primarily work in?"**
   - *Practical*: Day-to-day clarity

6. **"How does the team collaborate with applied research and product teams? What does that look like day-to-day?"**
   - *Shows*: Interest in cross-functional work

7. **"What does success look like for this role in the first 6 months?"**
   - *Shows*: Results-oriented thinking

---

## 🚨 CRITICAL DON'TS (Avoid Rambling - Neha's Feedback)

❌ **DON'T**:
- Ramble or go off on tangents (you did this with Neha!)
- Say "I don't have Spark/Databricks" (reframe as "equivalent experience")
- Give generic leadership stories (tie to backend/data!)
- Speak for more than 2-3 minutes without pausing
- Use vague terms ("worked on stuff") - **be specific**

✅ **DO**:
- **Start with the punchline** (scale, impact, then details)
- **Use metrics constantly** (40TB/day, 40M+ users, 50% improvement)
- **Pause and check** ("Does that answer your question?")
- **Connect to Scribd** ("This is similar to what Scribd needs because...")
- **Show enthusiasm** ("This is exciting because...")

---

## 💡 KEY TALKING POINTS (Memorize These Numbers)

### **Your Scale Experience:**
- __40TB/day__ *data processing*
- __40M+ customers__ *monthly*
- __15+ countries__ *served*
- __50% efficiency improvement__
- __$30K annual cost savings__
- __82% resolution time improvement__ *(AI agent)*
- __240+ dev-hours saved/month__ *(AI agent)*

### **Your Tech Stack Match:**
- **AWS Lambda** ✅ *(listed in JD)*
- **AWS SageMaker** ✅ *(listed in JD)*
- **CloudWatch** ✅ *(listed in JD)*
- **Infrastructure-as-code** ✅ *(CDK = Terraform equivalent)*
- **Step Functions** ✅ *(Spark-like orchestration patterns)*
- **Python** ✅ *(expert level)*

### **Spark/Databricks - How to Talk About It:**

**If Asked: "Do you have Spark/Databricks experience?"**

**Your Answer** (Honest but Positive):
- *I haven't used* __Spark or Databricks specifically at Amazon__
- *But I have* __deep experience with the patterns and problems they solve__*:*
  - __Distributed data processing__ *(40TB/day)*
  - __ETL pipelines__ *(transform, aggregate, enrich)*
  - __Parallel processing__ *(Lambda concurrency, Step Functions parallelism)*
  - __Large-scale transformations__ *(product catalog data)*

**Connect to Your Experience:**
- __AWS Step Functions__ *is similar to* __Spark DAGs__
  - *Both* __orchestrate complex workflows__
  - *Both* __handle distributed processing__
  - *Both* __manage retries, error handling, parallelism__

- __AWS Glue & Athena__ *use* __Spark under the hood__
  - **Athena** *uses* __Presto__ *(SQL engine on distributed data)*
  - **Glue** *uses* __PySpark__ *for* __ETL jobs__
  - *I've* __written SQL queries__ *in* __Athena__ *over* __large S3 datasets__

**Your Confidence Statement:**
- *I'm* __very familiar with distributed data processing patterns__
- *I'm* __confident I'll ramp up quickly__ *on* __Spark/Databricks__
- *At Amazon, I* __picked up new frameworks fast__ *(learned Kotlin, Ruby basics, Scala exposure)*
- __The concepts translate directly__ *(partitioning, shuffling, transformations, actions)*

---

## 📚 SPARK QUICK REFERENCE (Know These Concepts)

### **What Spark Is:**
- __Distributed data processing framework__
- __In-memory computation__ *(faster than Hadoop MapReduce)*
- __Handles big data__ *(terabytes to petabytes)*
- __Supports multiple languages__ *(Python/PySpark, Scala, Java, R)*

### **Core Concepts (Know These Terms):**
- **RDD** *(Resilient Distributed Dataset)*: Fundamental data structure
- **DataFrame**: Structured data (like SQL tables)
- **DAG** *(Directed Acyclic Graph)*: Execution plan (like Step Functions!)
- **Transformations**: Lazy operations (map, filter, join)
- **Actions**: Trigger execution (collect, count, save)
- **Partitioning**: Distribute data across nodes
- **Shuffling**: Redistribute data (expensive operation)

### **Spark vs. Your Experience (The Parallels):**

| **Spark Concept** | **Your AWS Equivalent** | **What to Say** |
|-------------------|-------------------------|-----------------|
| Spark DAG | Step Functions workflow | "Similar orchestration patterns" |
| PySpark transformations | Lambda data processing | "Distributed transformations at scale" |
| Spark partitioning | Lambda concurrency | "Parallel processing across nodes" |
| Spark DataFrames | Athena SQL queries | "Structured data operations" |
| Spark cluster | Lambda auto-scaling | "Elastic compute for data processing" |

### **Smart Talking Points:**

**If Discussing Spark:**
- "I understand __Spark's strength is in-memory distributed processing__"
- "My __Step Functions experience__ *translates well*—__both orchestrate complex DAGs__"
- "I've used __Athena__ *(which uses Presto)* *for* __SQL on large datasets__—__similar to Spark SQL__"
- "I'm __excited to learn Databricks__—*it's the natural evolution of my AWS data engineering work*"

**If Asked About Learning Curve:**
- "I've __picked up multiple languages at Amazon__ *(Kotlin, Ruby, Scala basics)*"
- "The __core concepts__ *(distributed processing, partitioning, transformations)* __are familiar from my 40TB/day pipeline work__"
- "I'm a __fast learner__ *and* __love diving into new frameworks__"

---

## 🎯 REFRAME STRATEGY (If Spark Comes Up)

**DON'T SAY**:
- ❌ "I don't have Spark experience"
- ❌ "I've never used Databricks"

**DO SAY**:
- ✅ "I haven't used Spark specifically, but I've solved the same problems with Step Functions and Lambda at 40TB/day scale"
- ✅ "I'm very familiar with distributed data processing patterns—Spark is the natural next tool in my toolkit"
- ✅ "I've used Athena extensively, which uses Presto under the hood—similar distributed SQL processing"

### **Your Bonus Qualifications:**
- __LLM integration__ *in production pipelines*
- __RAG systems__ *with vector databases*
- __Metadata extraction, summarization, classification__ *(exactly what JD mentions!)*
- __ML model deployment__ *(SageMaker Endpoints)*

---

## 🎯 CLOSING STATEMENT (If Time)

**When Sachin Wraps Up:**
- __Thank you, Sachin__. *This has been a great conversation*
- *I'm* __really excited about this role__
  - *The combination of* __backend engineering, large-scale data pipelines, and LLM integration__ *is exactly where I want to grow*
  - *And Scribd's mission of* __democratizing knowledge__ *through* __high-quality metadata is deeply meaningful*
- *I'm* __confident I can hit the ground running__
  - *My* __40TB/day pipeline experience__ *translates directly to* __processing hundreds of millions of documents__
  - *Plus, I bring* __bonus LLM/ML production experience__ *that can accelerate the team's AI initiatives*
- __Looking forward to next steps!__

---

## ⏰ TIME MANAGEMENT (30-Minute Interview)

**0-2 min**: Introductions, rapport building  
**2-20 min**: Project walk-through (YOUR MAIN CHANCE - MAKE IT COUNT!)  
**20-25 min**: Your goals/what you're looking for  
**25-30 min**: Your questions for Sachin  

**CRITICAL**: Keep project story to **15-18 minutes max**. Pause frequently. Check if Sachin wants more detail.

---

---

## 📄 POTENTIAL RESUME (From Vooban - Company 14)

# Aviral Garg
* Vancouver, British Columbia, Canada
* aviral.garg@icloud.com
* [in/aviralgarg](https://www.linkedin.com/in/aviralgarg)
* [aviralgarg.com](https://aviralgarg.com/)

## SUMMARY
A highly creative Full Stack Software Engineer with over 5 years of experience specializing in the design, development, & maintenance of scalable, cloud-based applications that leverage ML & Generative AI. Proven expertise in building end-to-end, AI-driven solutions & automation pipelines on AWS that accelerate product development & enable rapid experimentation.

## SKILLS
*   **AI/ML:** Generative AI (OpenAI, Anthropic, Gemini, Ollama), Agentic Orchestration & Frameworks (LangChain, CrewAI, Google Agent Kit, Autogen), MCP, RAG, NLP, LLMs, Model Deployment (SageMaker Endpoints, Batch Transform), Vector Databases, Python (ML Libraries), Intent Recognition, Query Parsing.
*   **Cloud & DevOps (AWS):** Lambda, SageMaker, API Gateway, DynamoDB, Cognito, AWS CDK & CloudFormation (IaC), SAM, SSM, Step Functions, S3, EC2, ECS, CloudWatch, X-Ray, SNS, SQS, Glue, Athena.
*   **Languages & Frameworks:** Python (Flask, FastAPI), Node.js, React, TypeScript, Kotlin, C#.
*   **Developer Tools & Version Control:** Git, Docker, Cursor, Windsurf, Linear, Playwright, Unity3D, n8n, Plotly, D3.js, Matplotlib.

## EXPERIENCE
**Software Development Engineer**
**Amazon - Beauty Tech Team**
**February 2021 – March 2025, Vancouver, BC**
*   Led a team of 8 engineers, designers, & data scientists to deploy serverless data pipelines with 50% increased efficiency.
*   Leveraged AWS Step Functions, Lambda, DynamoDB, SageMaker, & Athena; automatically scaled for growth, processed 40TB/day of product catalog data, & served 40M+ monthly customers across 15+ countries.
*   Built 4-staged AWS CDK CI/CD pipelines using CloudWatch & X-Ray for granular system monitoring & bottleneck tracing. Received org-wide accolades for robust documentation & operational readiness for every step of the SDLC.
*   Built internal-documentation-powered AI agents to provide instant answers to CI/CD admin questions, identify documentation gaps, & flag outdated content. Improved question resolution time by 82%, with projected savings of 240+ dev-hrs/month from integration with the internal admin ticketing system.
*   Led an organization-wide documentation workshop, establishing a systematic platform for subject-matter-expert reference & reaching 100% completion of product & CI/CD documentation for the Beauty Tech organization.
*   Spearheaded CI/CD-driven store-page-builder project for Amazon clients using React & Python.
*   Integrated external microservices & A/B testing framework, increasing client customization capabilities by 300%.
*   Automated monthly business reports for the recommendations team, reducing manual reporting time by 90%.
*   Led a team of 4 to win first place at the Amazon 2022 Hackathon with an Augmented Reality iOS makeup-tutorial app.

**Software Development Engineer**
**Amazon - Prime Pantry Team**
**June 2020 - February 2021, Vancouver, BC**
*   Architected robust Kotlin applications achieving 100% test coverage for Prime Pantry API development.
*   Optimized API performance, reducing page-load impact by 37% & increasing add-to-cart conversion rates by 2.5%, which directly contributed to over $3 million monthly revenue for the Prime Pantry platform.
*   Cut setup time by 75% & saved 3,528 dev-hrs/year by automating Prime Pantry API developer onboarding & environment setup while eliminating setup-related errors.
*   Built automated CI/CD pipelines in AWS CDK, saving 12+ dev-hrs/week & cutting deployment errors by 95%.
*   Delivered $30K in annual cost savings through systematic AWS CI/CD optimization & usage policy implementation.
*   Led organization-wide CodeGuru Profiler adoption across 7 projects, reducing on-call incidents & maintenance hours.

**AI Software Engineer**
**T4G Limited**
**October 2018 – December 2019, Vancouver, BC**
*   Architected NLP chatbots with full CI/CD, leveraging Azure DevOps, using Node.js & SQL, securing $100K+ contracts.
*   Demonstrated AI capabilities to enterprise clients, establishing the company's reputation in the AI/ML space.
*   Developed mission-critical C# desktop applications & SSIS data integration packages serving 50+ million users globally.
*   Optimized promo-code generation, achieving 40% efficiency improvement & enabling 4 additional high-value contracts.
*   Automated extraction of 10 years of Git version history from 15 applications, saving 7 dev-hrs/week with Python scripts.

**Software Engineer**
**Texavie Technologies Inc.**
**December 2017 - May 2018, Vancouver, BC**
*   Engineered cross-platform mobile, desktop, & mixed-reality headset proof-of-concepts in Unity3D.
*   Demonstrated wearable prototypes, securing investor interest & validating product-market fit for AR/VR technologies.
*   Developed critical prototype debugging tools reducing calibration time by 60% & enabling on-time product launch.
*   Built cross-platform game development pipelines for Windows, macOS, & Linux, doubling the target customer base.

## PROJECTS (2025)
**FoodFlow Intelligence Platform - Multi-Agent Food Delivery Analytics**
*   Architected multi-agent ecosystem integrating LangChain, CrewAI, Google Agent Kit, and Autogen for food delivery analytics.
*   Built conversational AI interface enabling natural English queries with automated Plotly, D3.js, and Matplotlib visualizations.
*   Designed streaming analytics engine with SQL data warehouse integration and external API connections.
*   Implemented agent communication framework with message passing, load balancing, and auto-scaling systems.
*   Deployed Kubernetes-based infrastructure with CI/CD pipelines and monitoring solutions.
*   Developed prompt optimization laboratory with A/B testing and intent classification models.

**Bob - AI-Powered Development Assistant**
*   Built a multi-threaded personal voice assistant with 8 operational modes for hands-free development & accessibility.
*   Reduced Agentic AI platform costs by 40x through extensive prompt engineering & optimization techniques.
*   Implemented zero speech data loss during processing with real-time speech-to-tool-calls conversion.
*   Integrated OpenAI Whisper for local ML-based speech recognition with real-time audio processing pipeline.

**Live Transcriber (7.8K downloads) – Real-Time Speech Processing**
[pypi.org/project/livetranscriber](https://pypi.org/project/livetranscriber)
*   Deployed a multi-threaded open-source Python package with real-time speech transcription & zero data loss.
*   Architected a single-file WebSocket wrapper around Deepgram API with async/await supporting sync & async callbacks.
*   Implemented comprehensive resource management with automatic cleanup, graceful shutdown, & error handling.
*   Created a seamless PyPI distribution with proper dependency management, enabling pip installation & integration.

**Pre-bunker health communications system - Health Misinformation Prevention**
[github.com/gaviral/pre_bunker_health_communications_system](https://github.com/gaviral/pre_bunker_health_communications_system)
*   Built AI agents for health misinformation prevention, simulating public reactions & generating evidence-backed prebunks.
*   Created a comprehensive prototype with implementation across 19 versions achieving 65-80% risk reduction.
*   Built a 5-stage pipeline: Claim Extraction, Risk Assessment, Audience Simulation, Evidence Validation, Countermeasures.
*   Developed 12 specialized agent personas for comprehensive audience simulation with multi-source evidence validation.
*   Created a FastAPI web interface with async processing & real-time risk assessment.
*   Developed a novel Misinterpretability@k metric for quantifying health communication risk.

**Resume Coach – Full-Stack AI Application**
[coach.aviralgarg.com](https://coach.aviralgarg.com/)
*   Built full-stack GPT-powered AI app with LangChain on AWS Lambda, API Gateway, DynamoDB, S3 & CloudFront.
*   Created a React 19 + TypeScript frontend with a CI/CD pipeline using GitHub Actions, deploying to production.
*   Implemented session persistence with DynamoDB TTL & contextual follow-up chat system.

## EDUCATION
**Machine Learning Program**
**Interview Kickstart • 2025**
*   Coursework: EDA & Feature Engineering, Regression & Classification, Model Evaluation, Model Fine-Tuning, Supervised, Unsupervised & Reinforcement Learning, Neural Networks, NLP, Agents Frameworks.

**B.A.Sc., Computer Engineering (Software Engineering Major)**
**University of British Columbia • Vancouver, BC • 2019**

---

## 🧘 PRE-INTERVIEW RITUAL (DO THIS NOW - 5 MINUTES)

1. **Practice Out Loud** (Per your learning: you rambled without practice!)
   - Say the opening statement 3x
   - Say architecture section 2x
   - Say one challenge/trade-off 2x

2. **Review These Numbers**:
   - 40TB/day
   - 40M+ customers
   - 50% efficiency
   - $30K savings
   - 82% improvement (AI agent)

3. **Deep Breath**:
   - This is **YOUR project** (you built it!)
   - You're **EXACTLY what they need** (backend + data + LLM!)
   - Be **CONFIDENT but CONCISE**

---

## 🎯 FINAL REMINDERS

✅ **Start strong** - First 20 min = make or break  
✅ **Be specific** - Numbers, tech, architecture details  
✅ **Connect to Scribd** - "This is similar to what you need because..."  
✅ **Show enthusiasm** - "This is exciting!" "I love this challenge!"  
✅ **ASK great questions** - Shows you did research, genuinely interested  

**You've got this! You're the perfect candidate!** 🚀

---

## 📝 POST-INTERVIEW ANALYSIS (Oct 15, 2025)

### ✅ **WHAT WENT WELL:**
- **Strong project walkthrough**: Beauty Tech data lake (40TB/day, 40M+ customers, $30K savings)
- **Handled Spark question effectively**: Explained you used Spark patterns with Step Functions, interested in learning
- **Project Scott discussion**: RAG pipeline, FAISS/Pinecone, Slack integration, dynamic agent creation
- **Cost optimization insight**: Shared 40% reduction by breaking down LLM tasks with Python code (resonated with Sachin)
- **Good questions**: Asked about Scribd/Everand/Slideshare differences, current challenges
- **Positive ending**: Sachin said "glad to hear you've got the experience" and it "will come handy"

### 🎯 **KEY LEARNINGS ABOUT SCRIBD:**
**Team of 10, two main domains:**
1. **Content Moderation** (Content Trust): Policy enforcement using Google tools, fingerprints, LLMs
2. **Content Enrichment** (Metadata Extraction/Generation):
   - Title generation (improve SEO)
   - Table of contents generation
   - Document translation (keeping structure/fonts/images intact)

**Current Challenges (2026 Focus):**
- **Scalability**: 250M documents, hitting OpenAI limits
- **Multi-LLM complexity**: Different model capabilities (multimodal = screenshots), 27 pages/doc × 250M = 6.5B images
- **Vision**: Self-serving platform (team submits prompt → select model → run inference → export data)

**Tech Stack:**
- Spark/Scala on Airflow (older pipelines)
- AWS (Lambda, SQS) with custom framework (newer pipelines)
- Heavy SageMaker usage
- Experimenting with Gemini (large context, cheap)

### 🔧 **AREAS TO REFINE:**
- Got flustered pulling up questions at end (but recovered well)
- Could have been slightly more concise in some explanations

### 🚀 **NEXT STEPS:**
- Neha will reach out with next steps
- **Likely outcome**: Strong positive impression, your cost optimization + LLM experience aligned perfectly with their 2026 vision

### 💡 **INTERVIEW CLOSING NOTES:**
- Sachin stayed extra minutes to answer questions (good sign)
- Explicitly said your experience will be helpful for the team
- **Overall assessment**: STRONG performance, good fit for role

