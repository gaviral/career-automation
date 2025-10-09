# EA Interview Prep Guide - Scannable Format
**Interview:** Thursday, October 9, 2025, 1:00 PM - 2:00 PM PDT  
**Interviewers:** Daniel Arguedas (Hiring Manager), Blaze Wallber (Director), Rhea Lauzon (Technical Director)

---

## ⏰ TIME: 1PM TODAY

---

## 🎯 Q1: "TELL ME ABOUT YOURSELF" (60-90 sec MAX)

**Answer:**

- *I'm a* **full-stack software engineer** *with* **5 years at Amazon** *specializing in* **cloud-native ML applications on AWS**

- *At* **Amazon Beauty Tech**, *I led a team of* **8 engineers** *building* **AI-powered systems**
  - *Processed* **40TB/day**
  - *Serving* **40M+ monthly customers** *across* **15 countries**

- *My technical foundation:*
  - **Python**
  - **AWS serverless architecture:** Lambda, SageMaker, API Gateway, DynamoDB
  - **Infrastructure as Code** *with* CloudFormation

- *I've built* **end-to-end ML pipelines** *from* **data ingestion** *through* **model deployment** *and* **monitoring**

- *What I'm most proud of is my* **cross-functional collaboration**
  - *Worked with* **technical artists**, **designers**, **data scientists**, **product managers**, **3D asset teams**
  - *At UBC, led* **game development capstone** *bridging* **engineers and creative teams**

- *I'm excited about EA because:*
  - **Perfect technical match** *(full-stack ML cloud apps on AWS)*
  - *I genuinely* **enjoy cross-functional collaboration** *with technical artists and content creators*
  - *As a* **FIFA player myself**, *I resonate with* **creating stellar fan experiences**

**[STOP. Breathe. Wait.]**

---

## 🎨 Q2: "WALK ME THROUGH A PROJECT" (Use VTO - 45 sec)

**Answer:**

- *I'll walk you through the* **Visual Property Extraction pipeline** *I led at* **Amazon Beauty Tech** *for* **AR virtual try-on**

**The Problem:**
- *Needed to replace* **costly third-party tool**
- **Beauty brands** *submitting* **non-standard product photos** *(different lighting, angles, backgrounds)*
  - *Causing* **inconsistent data quality** *for AR try-ons*

**My Role:**
- **Technical lead** *for* **overall pipeline** *(product catalog → visual properties)*
- *Owned* **architecture, planning, execution**
- *Consulted senior engineer for design review*

**The Architecture:**
- **Event-driven pipeline:** Step Functions + Lambda *(triggered by product catalog changes)*
- **SageMaker Ground Truth** *for* **data labeling** *(trained models for bounding boxes, color extraction)*
- **API Gateway + Lambda** *orchestration*
- **DynamoDB** *for state,* **S3** *for artifacts*
- **AWS CDK + CloudFormation** *(Infrastructure as Code)*
- **4-staged CI/CD** *(dev → gamma → pre-prod → prod)*
- **CloudWatch + X-Ray** *for observability*

**The Collaboration (KEY):**
- *Coordinated across* **6 different teams:**
  1. **Technical artists** *(rendering team - visual calibration, color accuracy)*
  2. **Designers** *(UX, visual property standards)*
  3. **Data scientists** *(model training)*
  4. **Product managers** *(requirements)*
  5. **External 3D asset creation team**
  6. **Beauty brand bridge teams** *(photo submission standards)*

**The Impact:**
- ✅ **Replaced third-party tool**
- ✅ **Established org-wide standards** *for future beauty brand partners*
- ✅ **High data quality** *validated through* **double-blind user experiments** *with diverse demographics*
- ✅ *Fed into larger* **Beauty Tech data lake** *processing* **40TB/day**

**[STOP. Offer: "I can go deeper into technical architecture, cross-team collaboration, or impact metrics."]**

---

## 🎨 Q3: "WORKING WITH TECHNICAL ARTISTS" (60 sec)

**Answer:**

**Example 1: Amazon Beauty Tech VTO Project**

- *Worked closely with* **technical artists** *on the* **rendering team**
- **The Challenge:** *Ensuring* **extracted color values** *from product images* **looked realistic** *when rendered on* **different skin tones in AR**

**What I Did:**
- *Scheduled* **regular syncs** *for* **visual calibration discussions**
- *Conducted* **data-driven experiments:**
  - **Double-blind tests** *with people of different* **genders and races**
  - *Using our demo app to validate* **RGB values** *translated to* **realistic AR experiences**
- *Bridged the gap between* **technical requirements** *and* **artistic vision**
  - *They cared about* **visual realism**
  - *I needed to ensure our* **data pipeline** *delivered* **right color accuracy**

**Communication Approach:**
- *Respected their* **expertise** *in visual rendering and face tracking*
- *Used* **shared visual references** *(not just RGB values)*
- *Brought* **experimental data** *to discussions to align on what "realistic" meant technically*

**Example 2: UBC Game Development Capstone**

- *Led* **game development capstone** *where I was* **technical lead** *and* **bridge** *between* **engineers and game designers/artists**
- *Learned:* **We speak different languages**
  - *They care about* **player experience** *and* **aesthetics**
  - *We care about* **frame rates** *and* **memory**
- *Became the* **translator** *ensuring* **design visions** *were technically feasible*

**Why This Matters:**
- *I genuinely* **enjoy** *this type of collaboration*
- *It's challenging but rewarding to* **bridge technical and creative worlds**
- *I know this is a* **big part of this role**

**[STOP. Wait for follow-up.]**

---

## 🔧 VTO PROJECT - TECHNICAL DEEP DIVE (If Asked)

### Technical Architecture

**Data Ingestion:**
- **Product catalog changes** *triggered* **SNS events**
- **Step Functions** *orchestrated* **multi-stage pipeline**
- **Lambda functions** *for preprocessing and validation*
- **S3** *for raw product images and intermediate artifacts*

**ML Pipeline:**
- **SageMaker Ground Truth:** *Data labelers created* **bounding boxes** *inside product images (e.g., isolating lipstick from packaging)*
- **Custom Models:** *Data scientists developed* **in-house models**:
  - **Bounding box detection** *(locating product within image)*
  - **Color extraction** *(precise RGB values for AR rendering)*
- **Experimentation:** *Conducted* **double-blind trials** *with diverse demographics wearing virtual lipsticks in demo app*
- **Decision tree approach:** *Early-stage data used for immediate averages, validated through real user experiments*

**API & Storage:**
- **API Gateway** *with* **Cognito authentication**
- **Lambda** *for orchestration and business logic*
- **DynamoDB** *for session state and metadata*
- **S3** *for visual property data artifacts*

**Infrastructure:**
- **AWS CDK (TypeScript)** *generating* **CloudFormation**
- **4-staged CI/CD:** dev → gamma → pre-prod → prod
- **CloudWatch** *for metrics and alarming*
- **X-Ray** *for distributed tracing*

---

### Cross-Functional Collaboration Details

**1. Technical Artists (Rendering Team):**
- **Context:** *Applied scientists and technical artists handled* **real-time AR rendering**, **face tracking**
- **Collaboration:** *Regular syncs on* **visual calibration**
- **Example Challenge:** *"What* **RGB values** *look realistic across different* **skin tones** *in AR?"*
- **My Approach:** **Data-driven discussions** *using experimental results from real users*
- **Outcome:** *Aligned on* **color accuracy standards** *that balanced* **technical precision** *with* **visual realism**

**2. Designers:**
- **Context:** *Sister team (Customer Experience) owned* **front-end UX** *including* **before/after slider**
- **Collaboration:** **Visual property standards**, **UX requirements**
- **Example Challenge:** *Balancing* **design goals** *(immediate visual feedback)* *with* **technical constraints** *(processing time)*
- **My Approach:** *Prototyped solutions, showed trade-offs with real data*
- **Outcome:** *Agreed on* **asynchronous processing** *with* **progress indicators**

**3. Data Scientists / Applied Scientists:**
- **Context:** *Created and trained* **ML models** *for* **bounding boxes** *and* **color extraction**
- **Collaboration:** **Model training**, **validation experiments**, **feature engineering**
- **Example Challenge:** **Insufficient labeled training data** *initially*
- **My Approach:** *Established* **SageMaker Ground Truth pipeline**, *recruited data labelers*
- **Outcome:** *Built* **high-quality training dataset**, *improved model accuracy*

**4. Product Managers:**
- **Context:** *Defined requirements for what* **visual properties** *to extract*
- **Collaboration:** **Requirements gathering**, *working backward from* **product vision**
- **Example Challenge:** *Initial requirements were vague ("make AR try-on realistic")*
- **My Approach:** **Multiple iteration cycles**, *prototyped early to clarify disconnects*
- **Outcome:** **Concrete requirements:** RGB values, product dimensions, texture data

**5. 3D Asset Creation Team (External):**
- **Context:** *Specialized team created* **3D models** *from our extracted properties*
- **Collaboration:** *Defined* **data format handoffs**, **API contracts**
- **Example Challenge:** *Coordinate system context was misunderstood*
- **My Approach:** *Scheduled meeting to clarify, documented assumptions*
- **Leadership Decision:** *Respected their* **expertise** *(they're 3D modeling experts)*, *guided overall direction without micromanaging*
- **Outcome:** **Smooth handoff pipeline**, *they handled 3D generation autonomously*

**6. Beauty Brand Bridge Teams:**
- **Context:** *Teams interfacing with beauty brand clients* **(L'Oréal, Maybelline, etc.)**
- **Collaboration:** *Improved* **product photo submission platform**
- **Example Challenge:** **Non-standard photo submissions** *(lighting, angles, backgrounds varied wildly)*
- **My Approach:** *Worked backward—"Why are photos bad quality?"—guided* **standardization** *of submission forms*
- **Outcome:** *Created* **internal standards** *for color values, naming conventions, photo quality adopted* **organization-wide**

---

### Key Technical Decisions

**1. Not Binding to Current State:**
- *Designed for* **scalability** *(new beauty brands joining continuously)*
- *Created* **standardized onboarding process** *for future partners*
- **Naming conventions** *adopted across* **Beauty Tech organization**

**2. Working Backward from Real Problems:**
- *Didn't just fix immediate symptoms (bad data quality)*
- *Addressed* **root causes** *(product owner submission standards)*
- *Split work:* **Beauty brands** *improved submissions,* **we improved** *extraction algorithms*

**3. Leverage Partner Team Expertise:**
- *Consulted* **senior engineer** *for architecture design review*
- *Let* **3D asset team** *handle their domain (didn't reinvent the wheel)*
- *Let* **rendering team** *(applied scientists)* *handle face tracking and AR*
- *Still* **guided** *at high level to keep technical direction consistent*

**4. Data Quality as Priority:**
- *Established* **best practices** *for* **RGB values** *through user experiments*
- **Double-blind validation** *with diverse demographics*
- *Not just extracting data, but ensuring it produced* **realistic AR experiences**

---

## 🚀 PROJECT SCOTT (Backup Story - If Asked)

**30-Second Version:**

- *Built* **AI agent system** *(Project Scott)* *for answering team questions from* **internal documentation**

**The Problem:**
- **New engineers** *had many technical questions (CI/CD, admin, infrastructure)*
- **Documentation scattered**, **SMEs repeatedly answered same questions**

**The Solution:**
- **RAG-based AI agent** *with* **vector embeddings**, **LLM-powered Q&A**
- *Integrated with* **SageMaker** *for model hosting*
- *Named it* **"Project Scott"** *to anthropomorphize and encourage adoption*
- *If AI couldn't find answer:* **Automatically escalated to SMEs**, *then fed responses back into documentation*

**The Architecture:**
- **API Gateway + Lambda** *orchestration*
- **SageMaker endpoints** *for inference*
- **DynamoDB** *for session state*
- **S3** *for documents*
- **CloudWatch/X-Ray** *for observability*
- **AWS CDK + CloudFormation** *for IaC*

**The Impact:**
- ✅ **82% improvement** *in resolution time*
- ✅ **240+ dev-hours/month saved** *across organization*
- ✅ **100% documentation coverage** *(led org-wide workshop)*
- ✅ **High adoption rate** *(became go-to resource)*

**[Use if asked: "Tell me about another ML project" or "AI agents/LLMs experience"]**

---

## 💼 BEHAVIORAL QUESTIONS

### "Describe a time you received difficult feedback"

**Example: VTO Architecture Review**

**Situation:**
- *Early in VTO project, proposed initial architecture to* **senior engineer** *for review*

**Feedback:**
- *"This design won't* **scale** *beyond small volume. Your* **Step Functions** *orchestration will* **timeout** *with large batches. Need to rethink* **data partitioning** *and* **parallel processing**."*

**Initial Reaction:**
- *Felt defensive—spent* **3 days** *on that design*
- *But took a step back*

**Action:**
- *Scheduled* **follow-up meeting** *to understand concerns deeply*
- *Asked clarifying questions about* **expected scale** *(turned out:* **10x** *what I'd designed for)*
- *Acknowledged gaps in initial assumptions*
- **Redesigned** *with* **parallel processing**, *optimized* **Lambda memory allocation**, *implemented* **DynamoDB caching layer**

**Result:**
- *Final architecture scaled to* **40TB/day** *serving* **40M+ users**
- *Strengthened relationship with senior engineer*
- *Now* **proactively seek architecture reviews** *before full implementation*

**Learning:**
- **Feedback is a gift**
- *Senior engineers have* **context I don't**
- *Now I always ask* **"What scale should this handle?"** *upfront*

---

### "Handling competing priorities from different teams"

**Example: VTO - Beauty Brand Submissions vs ML Model Training**

**Situation:**
- **Beauty brand bridge teams** *wanted* **faster onboarding** *(pressure from executives)*
- **Data scientists** *needed* **higher quality training data** *(couldn't train good models without it)*

**Conflict:**
- *Bridge teams wanted to* **accept any photo submissions** *to speed onboarding*
- *Data scientists wanted* **strict photo standards** *to ensure model accuracy*

**My Approach:**
- *Facilitated meeting with both teams to* **align on priorities**
- *Brought* **data:** *showed experimental results proving* **low-quality photos = poor AR realism = bad customer experience = churn**
- *Proposed* **compromise: phased approach**
  - **Phase 1:** *Accept current submissions, use manual review bottleneck*
  - **Phase 2:** *Work with beauty brands to improve submission standards*
  - **Phase 3:** *Automated pipeline with high-quality inputs*

**Communication:**
- **Regular status updates** *to both teams*
- **Documented decisions** *and trade-offs*
- **Managed expectations** *on timelines*

**Result:**
- *Both teams bought in*
- *Established* **photo standards** *that beauty brands adopted*
- *Improved* **data quality** *over time*
- *No compromise on* **customer experience**

---

### "Effective communication with non-technical stakeholders"

**Example: Explaining ML Pipeline Delays to PMs**

**Challenge:**
- **PMs** *didn't understand why* **color extraction** *took "so long"*
- *Kept asking* **"Can't you just speed it up?"**

**My Approach:**

1. **Visual Demonstrations:**
   - *Showed* **side-by-side examples** *of* **"fast but inaccurate"** *vs* **"slower but accurate"** *color extraction in AR try-on*

2. **User Impact:**
   - *Explained in terms they cared about:* **"Fast but wrong colors = customers buy wrong shade = returns = bad reviews"**

3. **Analogies:**
   - *"It's like photo editing—you can apply a filter in 1 second, but* **professional color grading** *takes time for realism"*

4. **Trade-off Transparency:**
   - *Gave* **options** *with* **clear trade-offs** *(speed vs accuracy vs cost)*

5. **Regular Updates:**
   - **Bi-weekly syncs** *with* **dashboards** *showing progress, not just technical jargon*

**Result:**
- *PMs* **understood trade-offs**
- *Stopped pushing for* **speed over quality**
- *Advocated for* **realistic timelines** *with leadership*

**Learning:**
- *Non-technical stakeholders care about* **user impact** *and* **business outcomes**
- **Translate technical constraints** *into their language*

---

## 🔧 TECHNICAL DEEP-DIVE (for Rhea - Technical Director)

### AWS Serverless Architecture for Real-Time ML Inference

**High-Level:**

```
User → API Gateway → Lambda → SageMaker Endpoint → Response
                        ↓
                   DynamoDB (cache)
                        ↓
                CloudWatch + X-Ray
```

**Components:**

1. **API Gateway:**
   - **REST API endpoint** *with* **resource policies**
   - **Cognito** *for authentication (user pools)*
   - **API keys + usage plans** *for rate limiting*
   - **Request/response transformation**
   - **Caching layer** *for frequent predictions*

2. **Lambda (Orchestration):**
   - **Preprocessing:** *input validation, feature engineering*
   - *Invoke* **SageMaker endpoint** *with boto3*
   - **Post-processing:** *format response, business logic*
   - **Error handling and retries**
   - **Optimization:** **Provisioned Concurrency** *to reduce cold starts*
   - **Optimization:** **Connection pooling** *(reuse SageMaker connections)*

3. **SageMaker Endpoint:**
   - **Real-time inference endpoint**
   - **Auto-scaling** *based on invocation metrics*
   - **Multi-variant** *for A/B testing*
   - **Data capture** *for model monitoring*
   - *Model artifact in* **S3**, *inference container*

4. **DynamoDB:**
   - **Session state** *(user context for multi-turn interactions)*
   - **Caching layer** *for recent predictions*
   - **TTL** *for automatic cleanup*
   - **On-demand billing** *or provisioned capacity with auto-scaling*

5. **CloudWatch + X-Ray:**
   - **CloudWatch Logs** *for Lambda execution*
   - **CloudWatch Metrics:** *invocation count, duration, errors, SageMaker latency*
   - **Custom metrics:** *prediction confidence, data quality*
   - **CloudWatch Alarms:** *trigger SNS on errors or latency spikes*
   - **X-Ray:** *distributed tracing across* **API Gateway → Lambda → SageMaker**

6. **Infrastructure as Code:**
   - **AWS CDK (TypeScript)** *or* **SAM (YAML)**
   - **Modular stacks** *for reusability*
   - **Environment-specific parameters** *(dev/staging/prod)*
   - **CI/CD pipeline** *with automated testing*

**Experience:**
- *"I've implemented this exact pattern multiple times at Amazon for* **Project Scott** *(AI Q&A)* *and* **VTO project** *(visual property extraction)*. *Both scaled to support* **40M+ monthly users**."*

---

### Lambda Cold Starts - Mitigation

**What is a Cold Start:**
- **Initial latency** *when Lambda spins up* **new execution environment**
- *Load code, initialize dependencies, establish connections*
- *Critical for ML inference:* **large dependencies** *(ML libraries, model artifacts)*

**Mitigation Strategies:**

1. **Provisioned Concurrency:**
   - *Keep functions* **warm** *(pre-initialized execution environments)*
   - *Cost trade-off: pay for idle capacity, but* **eliminate cold starts**
   - *Used for* **critical paths** *in VTO pipeline*

2. **Minimize Package Size:**
   - *Only include* **necessary dependencies** *(not entire ML library)*
   - *Use* **Lambda Layers** *for shared dependencies*
   - *Reduced deployment package from* **250MB to 50MB** *in Project Scott*

3. **Lazy Loading:**
   - *Load ML model on* **first invocation**, *cache in* **global scope**
   - **Connection pooling** *(establish DB connections once, reuse)*
   - *Example: Load SageMaker endpoint connection once, reuse across invocations*

4. **Runtime Optimization:**
   - *Increased* **Lambda memory allocation** *(more CPU = faster init)*
   - *Tested:* **512MB vs 2GB** *memory—2GB had* **50% faster cold starts**

5. **Architecture Patterns:**
   - *Offload heavy processing to* **SageMaker endpoints** *(keep Lambda lightweight)*
   - *Use* **Step Functions** *for orchestration (Lambda only does specific tasks)*
   - **Async processing** *via SQS/SNS for non-latency-sensitive workloads*

**Metrics:**
- *Before optimization:* **p95 cold start ~500ms**, **p99 ~1200ms**
- *After optimization:* **p95 <100ms**, **p99 ~300ms**
- **Goal:** *Keep p95 under 100ms for good UX*

---

### SageMaker Deployment

**Core Components:**

1. **Model:**
   - **Model artifact** *(trained model in S3: .tar.gz)*
   - **Inference code** *(custom Python script or framework container)*
   - **Container image** *(AWS pre-built or custom Docker)*

2. **Endpoint Configuration:**
   - **Instance type** *(ml.m5.large for lightweight, ml.p3.2xlarge for GPU)*
   - **Instance count** *(start with 1, scale up)*
   - **Auto-scaling policies** *(target tracking on invocations per instance)*
   - **Data capture config** *(log inputs/outputs for model monitoring)*
   - **Multi-variant** *(A/B testing multiple model versions)*

3. **Endpoint:**
   - **REST API** *for real-time inference*
   - *Invoke via* **boto3** *(Python SDK)*
   - *Returns predictions synchronously*

**Deployment Steps:**

1. **Train Model** *(SageMaker training job OR external → upload to S3)*
2. **Create Model Object** *(point to S3 artifact + container)*
3. **Deploy Endpoint** *(AWS creates REST API)*
4. **Invoke** *(API call with JSON payload)*
5. **Monitor** *(CloudWatch metrics, SageMaker Model Monitor for drift)*

**Advanced:**
- **Multi-variant endpoints:** *Deploy 2 model versions, route 90% to v1, 10% to v2 for A/B testing*
- **Multi-model endpoints:** *Host multiple models on single endpoint (cost optimization)*
- **Auto-scaling:** *Target 1000 invocations per instance, scale up/down automatically*

**Experience:**
- *"Used SageMaker extensively for* **Project Scott** *(NLP models for Q&A)* *and* **VTO project** *(computer vision for bounding boxes, color extraction)*. *Managed full lifecycle: training, deployment, monitoring, updates."*

---

### DynamoDB Data Modeling

**Design Principles:**

**Primary Key:**
- **Partition Key (required):** *Should distribute data evenly, enable primary access pattern*
- **Sort Key (optional):** *Allows range queries within partition*

**Example: User Profile for Recommendation Engine**

**Access Patterns:**
1. *Get user profile by userId*
2. *Get user's recent activity (last 30 days)*
3. *Get user's preferences*

**Table Design:**

```
Primary Key:
- Partition Key: userId (string)
- Sort Key: dataType#timestamp (string)

Attributes:
- userId: "user123"
- dataType#timestamp: "PROFILE#2025-10-09" or "ACTIVITY#2025-10-09T13:00:00"
- data: { ... user profile or activity data ... }
```

**Why This Design:**
- **Partition Key = userId:** *Ensures* **even distribution**, *enables* **user-specific queries**
- **Sort Key = dataType#timestamp:** *Allows querying by data type and sorting by timestamp*

**GSI (Global Secondary Index):**
- *If querying by* **lastActive** *timestamp across all users*
- **Partition Key:** status *(ACTIVE/INACTIVE)*
- **Sort Key:** lastActive *(timestamp)*

**Best Practices:**
- **Avoid scans:** *Always query with partition key*
- **Use TTL:** *Automatic deletion of expired data (session, cache)*
- **Batch operations:** *BatchGetItem, BatchWriteItem for efficiency*
- **On-demand vs provisioned:** *On-demand for unpredictable traffic*
- **DynamoDB Streams:** *Trigger Lambda on data changes (used in VTO for downstream processing)*

**Experience:**
- *"Used DynamoDB extensively at Amazon for* **session state** *(Project Scott)*, **caching** *(VTO)*, *and* **user context**. *Designed schemas for* **sub-100ms read latency** *at scale."*

---

### Infrastructure as Code with CloudFormation/CDK

**Philosophy:**
- **Reproducibility:** *Same infrastructure in dev/staging/prod*
- **Version Control:** *Infrastructure changes tracked in Git*
- **Automation:** *Deploy via CI/CD, no manual clicks*
- **Consistency:** *Eliminate configuration drift*

**Tool: AWS CDK**

**Why CDK over raw CloudFormation:**
- *Write infrastructure in* **TypeScript/Python** *(familiar languages)*
- **Constructs** *(reusable components)* *vs repetitive YAML*
- **Compile-time checks** *(catch errors before deployment)*
- *Generates* **CloudFormation** *under the hood*

**CI/CD Pipeline (4 Stages):**

1. **Dev:** *Deploy on every commit to* `dev` *branch (no approval)*
2. **Gamma:** *Deploy on merge to* `main` *(automated tests, manual approval)*
3. **Pre-Prod:** *Deploy after Gamma success (* **canary deployment, 10% traffic**)*
4. **Prod:** *Deploy after Pre-Prod validation (* **full rollout**)*

**Best Practices:**
- **Modular design:** *Separate stacks for different components (easier updates, less blast radius)*
- **Parameterization:** *Environment-specific configs (instance types differ in dev vs prod)*
- **Testing:** *CDK has built-in testing (assert stack has X resources)*
- **Documentation:** *Inline comments, README with architecture diagrams*

**Impact:**
- *"Achieved* **95% reduction in deployment errors**, **repeatable infrastructure** *across 4 environments, infrastructure changes* **code-reviewed** *just like application code."*

---

## 🙋 QUESTIONS TO ASK INTERVIEWERS

### For Daniel (Hiring Manager):
1. *"Can you tell me more about the* **day-to-day responsibilities** *in the first 90 days? Tyler mentioned learning the* **Frostbite codebase**—*how does that ramp-up typically look?"*
2. *"What does* **success look like** *for this role in the* **first 6 months**?"*
3. *"How does this team* **collaborate with other EA studios**? *Are there opportunities to work on projects* **across multiple games**?"*

### For Blaze (Director):
1. *"You oversee* **Production Operations & Technology** *across EA's global studios—what are the* **biggest operational challenges** *you're solving right now?"*
2. *"How do you see the role of* **AI/ML evolving** *in EA's content production workflows over the next few years?"*
3. *"What does* **effective cross-functional collaboration** *look like on your team? Any examples of recent successes?"*

### For Rhea (Technical Director):
1. *"What's the* **technical architecture** *for EA's online services? Are there specific* **scalability challenges** *you're tackling?"*
2. *"How does the team balance* **rapid experimentation** *with maintaining* **production stability**?"*
3. *"What* **AWS services or cloud technologies** *is the team most excited about adopting or expanding?"*

### General:
1. *"What do you* **enjoy most** *about working at EA?"*
2. *"How does the team* **stay up-to-date** *with rapidly evolving* **AI/ML technologies**?"*

---

## ⚠️ CRITICAL REMINDERS (From Learning Points)

### DON'T RAMBLE (Top Priority):
- ❌ **What Went Wrong:** *Spent* **2+ minutes** *on Project Scott in recruiter screen when* **30-45 seconds** *would work*
- ✅ **Fix:** *Answer in* **30-60 seconds**, *THEN offer to elaborate*
- ✅ **Technique:** *"I can go deeper into any aspect—technical architecture, cross-team collaboration, or impact. What would be most useful?"*

### WATCH INTERVIEWER CUES:
- *If they say* **"Great"** *or* **"Perfect"** → **STOP TALKING**
- *If they're* **taking notes** → **PAUSE** *to let them catch up*
- *If they say* **"That's exactly what I was looking for"** → **MOVE ON**

### USE STAR METHOD (60 seconds max):
- **S**ituation: 10 seconds
- **T**ask: 10 seconds
- **A**ction: 30 seconds
- **R**esult: 10 seconds (with metric)

### BE CONCISE FIRST:
- *Give* **2-3 key points**
- **Pause**
- *Let them ask for details*
- *Don't explain everything at once*

---

## 📋 PRE-INTERVIEW CHECKLIST

### Physical Setup (30 min before):
- [ ] **Test video/audio**
- [ ] **Good lighting** *(face visible)*
- [ ] **Quiet room**
- [ ] **Phone on silent**
- [ ] **Water nearby**
- [ ] **Close unnecessary tabs**

### Documents Open:
- [ ] **This prep guide**
- [ ] **Job description** *(02_formatted_jd.md)*
- [ ] **Your resume**
- [ ] **Interviewer research** *(13_Interviewer_Names_Email_Chain.md)*
- [ ] **Notepad** *for notes*

### Mental Prep:
- [ ] **Practice "Tell me about yourself" OUT LOUD 3 times** *(60-90 sec)*
- [ ] **Practice VTO walkthrough OUT LOUD 2 times** *(45 sec)*
- [ ] **Practice technical artist answer OUT LOUD 1 time** *(60 sec)*
- [ ] **Take 5 deep breaths** *before joining*
- [ ] **Mindset:** *"I'm qualified, I've done this, this is a conversation"*

---

## 🎯 YOUR COMPETITIVE ADVANTAGES

✅ **5 years AWS + ML experience** *(exactly what they need)*
✅ **VTO project demonstrates:** *full-stack ML, AWS serverless, cross-functional, technical artist work*
✅ **Project Scott as backup:** *different ML angle (RAG, LLM, AI agents)*
✅ **Game dev experience** *(UBC capstone)* = **BIG PLUS per Tyler**
✅ **Led team of 8 engineers** = *leadership capability*
✅ **Impressive metrics:** 82% improvement, 240 dev-hrs saved, 100% docs, 40TB/day, 40M+ users
✅ **Infrastructure as Code** *(AWS CDK, CloudFormation)*
✅ **Cross-functional collaboration across 6 teams** = *exactly what Blaze wants*
✅ **FIFA player** = *genuine fan, resonate with fan growth mission*

---

## 🚀 YOU'VE GOT THIS!

**Remember:**
- *You've built exactly what they're looking for*
- *You have the technical depth (Rhea will be impressed)*
- *You have the cross-functional experience (Blaze will be impressed)*
- *You have the full-stack ML expertise (Daniel will be impressed)*
- **Tyler already liked you**
- **Just be concise, watch cues, let them ask follow-ups**

**Final Mindset:**
- *This is a* **conversation between peers**, *not an interrogation*
- *You're evaluating them as much as they're evaluating you*
- **Be confident, be yourself, show genuine enthusiasm**

---

**GOOD LUCK! 🎮🚀**

