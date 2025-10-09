# EA Interview Prep - Comprehensive Guide
## Full Stack Software Engineer - ML Cloud Applications
**Interview Date:** Thursday, October 9, 2025, 1:00 PM - 2:00 PM PDT

---

## ⚠️ CRITICAL: TWO SEPARATE PROJECTS

**Project Scott** (AI Documentation Q&A) and **VTO Project** (Visual Property Extraction) are TWO DIFFERENT projects. Use strategically:
- **Q1 (End-to-End ML Cloud App):** Use Project Scott
- **Q2 (Cross-Functional Collaboration):** Use VTO Project
- See File 17 (Project_Story_Details.md) and File 21 (Project_Disambiguation_Analysis.md) for full details

---

## 🎯 MOST LIKELY QUESTIONS (Tier 1)

### Q1: END-TO-END ML CLOUD APPLICATION (90%+ probability)
**"Walk us through an end-to-end ML cloud application you built on AWS. What problem did it solve, how did you architect it, what was your role, and what was the impact?"**

**Why This Question:**
- Maps directly to role requirements
- Tyler emphasized "technical background in cloud-based full stack development, AI solutions"
- ChatGPT research identified this as THE most likely question

**Your Answer: Project Scott (AI Documentation Q&A System) - 30-45 seconds**

**Situation:** Built AI agent system to answer team questions from internal documentation within Amazon Beauty Tech.

**Problem:** New/onsite engineers needed instant answers to CI/CD/admin questions; documentation was scattered.

**Architecture:**
- **RAG Pipeline:** Vector embeddings, document retrieval, LLM-powered Q&A
- **API Layer:** API Gateway + Lambda for orchestration
- **ML/AI:** SageMaker for model hosting (inference endpoints)
- **Storage:** DynamoDB for session state, S3 for documents
- **Integration:** Internal ticketing system
- **Infrastructure:** AWS CDK + CloudFormation, 4-staged CI/CD
- **Monitoring:** CloudWatch + X-Ray for observability

**Role:** Built the AI agent system, drove org-wide adoption, integrated with ticketing.

**Key Features:** Natural language Q&A ("Talk to Project Scott"), automatic SME escalation, automated documentation updates.

**Impact:**
- **82% improvement** in resolution time
- **240+ dev-hours/month saved**
- **100% documentation coverage** (led org-wide documentation workshop)

*[Stop here - offer to elaborate if they want details]*

---

### Q2: CROSS-FUNCTIONAL COLLABORATION (90%+ probability)
**"Describe a time you collaborated with diverse technical and non-technical individuals (tech artists, content creators, data scientists). How did you ensure effective communication and successful outcome?"**

**Why:** Tyler emphasized this MULTIPLE times as "a big part of the role", need someone who "honestly, kind of enjoys that"

**Your Answer: Virtual Try-On Project (Visual Property Extraction) - 30-45 seconds**

**Situation:** Led visual property extraction pipeline for AR virtual try-on - required coordinating 6 different teams/disciplines.

**Key Collaborations:**
1. **Technical Artists (Rendering Team):** Visual calibration, color accuracy for AR. Regular syncs aligning technical requirements vs artistic vision for realistic skin tones.
2. **Designers:** UX collaboration (before/after slider), visual property standards. Data-driven discussions balancing design goals with technical constraints.
3. **Data Scientists/Applied Scientists:** Model training for bounding boxes and color extraction. Conducted double-blind user trials with diverse demographics.
4. **Product Managers:** Requirements gathering, worked backward from product vision (realistic AR try-on).
5. **3D Asset Creation Team (External):** Guided overall direction while respecting their expertise. Resolved disconnects with scheduled meetings.
6. **Beauty Brand Bridge Teams:** Guided standardization of product photo submissions, established best practices.

**Communication Strategies:**
- Regular syncs, clear documentation
- Data-driven discussions (real user experiments to validate color accuracy)
- Empathetic approach (acknowledged creative merit before presenting constraints)
- Worked backward from needs (why are photos bad quality?) not just symptoms

**Result:** Replaced third-party tool, established org-wide standards for future beauty brand partners, high data quality validated through experiments

---

### Q3: AWS SERVERLESS ARCHITECTURE (80%+ probability)
**"How would you design a serverless workflow for real-time ML inference using AWS Lambda? What AWS services would you integrate?"**

**Why:** JD specifically lists Lambda, SAM, SageMaker, API Gateway, DynamoDB

**Architecture Components:**
1. **API Gateway** - REST API endpoint, authentication (Cognito), rate limiting
2. **Lambda** - Orchestration, preprocessing, invoke SageMaker endpoint
3. **SageMaker Endpoint** - Real-time model inference
4. **DynamoDB** - Session state, user context, caching layer
5. **CloudWatch + X-Ray** - Monitoring, tracing, alarming
6. **SNS/SQS** - Async processing if needed

**Optimization Strategies:**
- Provisioned Concurrency for Lambda (reduce cold starts)
- API Gateway caching (frequent predictions)
- DynamoDB TTL (automatic cleanup)
- Multi-variant endpoints in SageMaker (A/B testing)

**Example:** Both Project Scott (AI Q&A) and VTO project used similar serverless patterns - scaled to support 40M+ monthly users

---

### Q4: GAME DEV / TECH ARTIST EXPERIENCE (70%+ probability)
**"Tell me about working with game developers or technical artists. What was your role and how did you ensure smooth collaboration?"**

**Why:** Tyler specifically said: "I would encourage you to talk about that" - "certainly a plus" and "would be beneficial"

**Option A: Amazon Beauty Tech VTO Project (Most Relevant)**
- **Situation:** Worked with technical artists on rendering team for AR virtual try-on
- **Role:** Technical lead coordinating visual property extraction pipeline with rendering team
- **Actions:** Regular syncs on visual calibration, data-driven discussions on color accuracy for different skin tones, conducted experiments to validate realism
- **Result:** Achieved high visual realism in AR try-on validated through double-blind user testing with diverse demographics

**Option B: UBC Capstone (Academic but Relevant)**
- **Situation:** Led technical team for game development capstone with game designers and artists
- **Role:** Technical lead + bridge between engineering and creative teams
- **Challenges:** Different vocabularies, technical constraints vs creative vision
- **Actions:** Facilitated communication, translated requirements both directions, prototyped early
- **Result:** Successfully launched game

---

## 🔧 TECHNICAL DEEP DIVES

### Lambda & Cold Starts
**Q: "What is a 'cold start' in AWS Lambda and how would you mitigate it for ML inference?"**

**Answer:**
- **Cold Start:** Initial latency when Lambda spins up new execution environment (load code, init dependencies)
- **Why It Matters:** ML models have large dependencies, impacts user experience
- **Mitigation:**
  1. Provisioned Concurrency (keep functions warm)
  2. Minimize package size (only necessary dependencies)
  3. Lazy loading (load model on first invocation, cache in global scope)
  4. Keep connections warm (reuse DB connections)
  5. Choose runtime carefully (compiled languages faster)
- **Experience:** Optimized Lambda cold starts at Amazon, achieved p95 <100ms

---

### SageMaker Deployment
**Q: "What are core components of SageMaker deployment? How would you deploy a trained ML model to a real-time endpoint?"**

**Core Components:**
1. **Model:** Trained artifact (S3) + inference code (container)
2. **Endpoint Configuration:** Instance type, count, scaling policies
3. **Endpoint:** REST API for real-time inference

**Deployment Process:**
1. Train Model (SageMaker training job or external)
2. Create Model Object (point to S3 artifact + container)
3. Configure Endpoint (choose instance, autoscaling min/max, data capture)
4. Deploy Endpoint (AWS creates REST API)
5. Invoke (API call with JSON payload)
6. Monitor (CloudWatch metrics, model monitor for drift)

**Advanced:** A/B testing (multi-variant endpoints), auto-scaling, multi-model endpoints

---

### DynamoDB Data Modeling
**Q: "Design a DynamoDB table for a real-time recommendation engine storing user profiles. What would be your primary key?"**

**Answer:**
- **Partition Key:** `userId` (ensures even distribution, enables user-specific queries)
- **Sort Key:** Optional - `timestamp` or `dataType` for multiple data types per user

**Access Patterns:**
1. Get user profile: Query by `userId`
2. Recent activity: Query by `userId` + sort by `timestamp`

**Indexes:**
- **GSI:** If querying by `lastActive` (different partition key)
- **LSI:** If alternate sort order within same user

**Experience:** Used DynamoDB extensively for session state, user context, caching at Amazon

---

### Infrastructure as Code
**Q: "How do you approach Infrastructure as Code for ML applications? Describe using CloudFormation."**

**Philosophy:** IaC ensures reproducible environments, version control, automated deployment, consistency across dev/staging/prod

**Example from Amazon:**
- **Tool:** AWS CDK (generates CloudFormation)
- **Components:** SageMaker training jobs, Lambda functions, API Gateway, DynamoDB tables, IAM roles, CloudWatch alarms
- **Best Practices:**
  - Modular design (nested stacks for reusability)
  - Parameterization (environment-specific configs)
  - Version control (Git, code review)
  - Automated testing (validate templates before deployment)
  - Documentation (inline comments, README)
- **CI/CD:** 4-staged pipeline - dev → gamma → pre-prod → prod
- **Result:** 95% reduction in deployment errors, repeatable infrastructure

---

### API Gateway Security
**Q: "Different methods for securing API Gateway endpoint that invokes ML model?"**

**Answer:**
1. **API Keys + Usage Plans** - Simple, rate limiting, monetization
2. **Amazon Cognito** - User pools, OAuth 2.0, token-based auth
3. **Lambda Authorizers** - Custom authorization logic
4. **IAM Roles** - AWS service-to-service, least privilege
5. **Resource Policies** - IP whitelisting, VPC endpoints
6. **WAF** - DDoS protection, SQL injection prevention

**Best Practice:** Multi-layered approach - Cognito + API keys + CloudWatch + WAF

---

## 💼 BEHAVIORAL QUESTIONS

### Complex Technical Challenge
**Q: "Describe a complex technical challenge you faced building a cloud-based application. How did you diagnose and solve it?"**

**Option A: Scalability Challenge**
- **Situation:** Product catalog pipeline needed to process 40TB/day, existing architecture couldn't scale
- **Challenge:** Performance bottlenecks, cost optimization, data consistency
- **Diagnosis:** CloudWatch metrics, X-Ray tracing identified bottlenecks in Step Functions orchestration
- **Solution:** Redesigned with parallel processing, optimized Lambda memory, implemented DynamoDB caching
- **Result:** 50% efficiency improvement, cost-optimized, 99.9% uptime

**Option B: Cold Start Optimization**
- **Situation:** ML inference Lambda had 500ms+ cold starts impacting UX
- **Challenge:** Latency-sensitive application, large deployment package
- **Diagnosis:** Analyzed CloudWatch logs, profiled dependencies
- **Solution:** Minimized dependencies, Provisioned Concurrency, optimized model loading
- **Result:** Reduced p95 latency to <100ms

---

### Learning New Technologies
**Q: "Tell me about a time you quickly learned a new technology to complete a project."**

**Example: AWS CDK for Infrastructure as Code**
- **Situation:** Team transitioning from manual CloudFormation to AWS CDK (TypeScript-based IaC)
- **Timeline:** 2 weeks to become productive
- **Approach:** Official docs, workshops, built small POC, studied existing patterns, pair programming
- **Result:** Became go-to person for CDK, authored team's best practices guide, trained 3 engineers
- **Impact:** Team productivity +40%, deployment errors down 95%

**Philosophy:** Rapid learner - 2025 example: Built Bob (voice assistant) learning OpenAI Whisper, multi-threading, real-time audio processing. Live Transcriber package (7.8K downloads) in weeks.

---

### Receiving Difficult Feedback
**Q: "Tell me about receiving difficult feedback from a team member. How did you respond?"**

**Example: Code Review Feedback**
- **Situation:** Senior engineer reviewed proposed architecture, pointed out scalability issues I'd missed
- **Feedback:** "This design won't scale beyond 1000 users. Need to rethink data partitioning."
- **Initial Reaction:** Felt defensive (spent 3 days on design), but took a step back
- **Response:** Scheduled follow-up to understand concerns, asked clarifying questions, acknowledged gaps, proposed revised design
- **Outcome:** Final architecture scaled to 40M+ users. Strengthened relationship. Learned valuable lesson.
- **Learning:** Feedback is a gift. Now proactively seek architecture reviews before implementation.

---

### Handling Competing Priorities
**Q: "How do you manage competing deadlines and demands from different departments?"**

**Answer:**
- **Prioritization:** Impact vs effort matrix, align with business goals
- **Communication:** Regular syncs with stakeholders, set expectations early
- **Documentation:** Clear status updates, blockers, dependencies
- **Delegation:** Leverage team strengths (led 8-person team at Amazon)
- **Example:** Amazon Beauty Tech - juggled 3 parallel projects (virtual try-on pipeline, CI/CD optimization, documentation initiative). Used JIRA, bi-weekly syncs, delegated by expertise. All delivered on time.

---

### Why EA / Fan Growth?
**Q: "Why are you interested in working at Electronic Arts and specifically within Fan Growth?"**

**Answer:**
Three main reasons:
1. **Technical Match:** Role perfectly aligns - full-stack ML cloud applications on AWS, exactly what I've built for 5+ years. Excited to apply serverless, SageMaker, IaC expertise to gaming.
2. **Cross-Functional Collaboration:** Team works with tech artists, content creators - my UBC game dev experience and Amazon Beauty Tech collaboration prepared me. Tyler mentioned this is a big part of the role, and honestly, I enjoy that.
3. **Mission Alignment:** Fan Growth's focus on elevating customer experiences through technology resonates. Building tools that maximize fan fun, creating engaging content - that's meaningful work. Contributing to EA's franchises would be exciting.

---

## 📋 PREPARATION CHECKLIST

### Before Interview
- [ ] Practice BOTH project pitches 30-45 seconds out loud 5+ times (Project Scott AND VTO)
- [ ] Practice top 10 questions with STAR method
- [ ] Time yourself (60 seconds max per answer)
- [ ] Review AWS service docs (Lambda, SageMaker, CloudFormation, DynamoDB, API Gateway)
- [ ] Prepare 3-5 questions to ask interviewers
- [ ] Test video/audio setup 30 minutes before
- [ ] Have resume, JD, this doc open during interview

### During Interview
- [ ] Be concise (30-60 seconds, offer to elaborate)
- [ ] Watch for interviewer cues (stop when they say "Great")
- [ ] Use STAR method for behavioral questions
- [ ] Draw diagrams for system design if possible
- [ ] Highlight cross-functional collaboration naturally
- [ ] Show enthusiasm for EA / gaming / marketing tech
- [ ] Ask thoughtful questions at the end

---

## 🎯 CRITICAL REMINDERS

**From Tyler:**
- This is NOT a coding interview - focus on technical background discussion
- Cross-functional collaboration emphasized MULTIPLE times
- Game dev experience is a BIG PLUS - mention naturally
- They want someone who "enjoys" cross-functional work

**From Learning Points (File 15):**
- BE CONCISE: Answer in 30-60 seconds, offer to elaborate
- WATCH CUES: Stop when they say "Great" or "Perfect"
- DON'T RAMBLE: You spent 2+ minutes on Project Scott in recruiter screen when 30-45 seconds would work

**Your Strengths:**
1. ✅ 5 years AWS + ML experience (exactly what they need)
2. ✅ TWO strong projects: Project Scott (AI Q&A) + VTO (Visual Property Extraction)
3. ✅ Cross-functional collaboration (6 teams on VTO: tech artists, designers, data scientists, PMs, 3D asset team, beauty brand teams)
4. ✅ Game dev experience + technical artist collaboration (unique differentiator Tyler highlighted)
5. ✅ Infrastructure as Code (AWS CDK, 4-staged CI/CD)
6. ✅ Scalability + Impact (82% improvement, 240 dev-hrs saved, 100% docs, 40TB/day, 40M+ users)

**You've got this! 🚀**

