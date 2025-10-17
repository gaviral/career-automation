# EA Interview Prep Guide - VTO Project Focus
**Interview Date:** Thursday, October 9, 2025, 1:00 PM - 2:00 PM PDT  
**Interviewers:** Daniel Arguedas (Hiring Manager), Blaze Wallber (Director), Rhea Lauzon (Technical Director)

---

## ⏰ TIME CHECK: Interview at 1PM TODAY

---

## 🎯 PRIMARY QUESTIONS TO PREPARE

### Q1: "Tell Me About Yourself" (60-90 seconds MAX)

**Your Answer:**

"I'm a full-stack software engineer with 5 years at Amazon specializing in cloud-native ML applications on AWS. At Amazon Beauty Tech, I led a team of 8 engineers building AI-powered systems that processed 40TB/day serving 40M+ monthly customers across 15 countries.

My technical foundation is in Python, AWS serverless architecture—Lambda, SageMaker, API Gateway, DynamoDB—and Infrastructure as Code with CloudFormation. I've built end-to-end ML pipelines from data ingestion through model deployment and monitoring.

What I'm most proud of is my cross-functional collaboration experience. I've worked extensively with technical artists, designers, data scientists, product managers, and even external 3D asset teams. My UBC capstone involved game development where I led the technical team while bridging communication between engineers and creative teams.

I'm excited about this role at EA because it's a perfect technical match—full-stack ML cloud applications on AWS—and because I genuinely enjoy cross-functional collaboration, especially working with technical artists and content creators in the gaming space."

**[STOP. Breathe. Wait for their response.]**

---

### Q2: "Walk Me Through a Project End-to-End" (Use VTO Project)

**The 45-Second Core Story:**

"I'll walk you through the Visual Property Extraction pipeline I led at Amazon Beauty Tech for AR virtual try-on experiences.

**The Problem:** We needed to replace a costly third-party tool, and beauty brands were submitting non-standard product photos—different lighting, angles, backgrounds—causing inconsistent data quality for our AR try-ons.

**My Role:** Technical lead for the overall pipeline from product catalog through visual property extraction. I owned architecture, planning, and execution, consulting a senior engineer for design review.

**The Architecture:**
- Event-driven pipeline using AWS Step Functions and Lambda triggered by product catalog changes
- SageMaker Ground Truth for data labeling—trained models for bounding box detection and color extraction
- API Gateway + Lambda orchestration layer
- DynamoDB for state, S3 for artifacts
- Full Infrastructure as Code with AWS CDK, 4-staged CI/CD
- CloudWatch and X-Ray for observability

**The Collaboration—This is Key:** I coordinated across 6 different teams:
1. **Technical artists on the rendering team** for visual calibration and color accuracy
2. Designers for UX and visual property standards
3. Data scientists for model training
4. Product managers for requirements
5. External 3D asset creation team
6. Beauty brand bridge teams for photo submission standards

**The Impact:** Successfully replaced the third-party tool, established org-wide standards for future beauty brand partners, and ensured high data quality validated through double-blind user experiments with diverse demographics. This fed into the larger Beauty Tech data lake processing 40TB/day."

**[STOP. Offer to elaborate: "I can go deeper into any aspect—the technical architecture, the cross-team collaboration, or the impact metrics."]**

---

## 🎨 WORKING WITH TECHNICAL ARTISTS (Tyler Specifically Highlighted This)

### When They Ask: "Tell me about working with technical artists or game developers"

**Your Answer (60 seconds):**

"I have two strong examples. First, at Amazon Beauty Tech on the VTO project, I worked closely with technical artists on the rendering team. Our challenge was ensuring that extracted color values from product images looked realistic when rendered on different skin tones in AR.

**What I Did:**
- Scheduled regular syncs specifically for visual calibration discussions
- Conducted data-driven experiments: we ran double-blind tests with people of different genders and races using our demo app to validate that our RGB values translated to realistic AR experiences
- Bridged the gap between technical requirements and artistic vision—they cared about visual realism, I needed to ensure our data pipeline delivered the right color accuracy

**The Communication Approach:**
- I respected their expertise in visual rendering and face tracking
- Used shared visual references rather than just talking about RGB values
- Brought experimental data to discussions to align on what 'realistic' meant technically

**Second Example—UBC Capstone:**
At University of British Columbia, I led a game development capstone project where I was the technical lead but also the bridge between engineers and game designers/artists. I learned early that we speak different languages—they care about player experience and aesthetics, we care about frame rates and memory. I became the translator, ensuring design visions were technically feasible and technical constraints were understood creatively.

**Why This Matters for EA:** I genuinely enjoy this type of collaboration. It's challenging but rewarding to bridge technical and creative worlds, and I know that's a big part of this role per Tyler."

**[STOP. Wait for follow-up questions.]**

---

## 📊 VTO PROJECT - DEEP DIVE DETAILS (If They Ask to Elaborate)

### Technical Architecture Deep Dive

**Data Ingestion Layer:**
- Product catalog changes triggered SNS events
- Step Functions orchestrated multi-stage pipeline
- Lambda functions for preprocessing and validation
- S3 for raw product images and intermediate artifacts

**ML Pipeline:**
- **SageMaker Ground Truth:** Data labelers created bounding boxes inside product images (e.g., isolating lipstick from packaging)
- **Custom Models:** Data scientists developed in-house models for:
  - Bounding box detection (locating product within image)
  - Color extraction (precise RGB values for AR rendering)
- **Experimentation:** Conducted double-blind trials with diverse demographics wearing virtual lipsticks in demo app
- **Decision Tree Approach:** Early-stage data used for immediate averages, validated through real user experiments

**API & Storage:**
- API Gateway with Cognito authentication
- Lambda for orchestration and business logic
- DynamoDB for session state and metadata
- S3 for visual property data artifacts

**Infrastructure:**
- AWS CDK (TypeScript) generating CloudFormation
- 4-staged CI/CD: dev → gamma → pre-prod → prod
- CloudWatch for metrics and alarming
- X-Ray for distributed tracing

**Monitoring & Observability:**
- CloudWatch dashboards for pipeline health
- Custom metrics for data quality validation
- Alerting on processing failures
- X-Ray for end-to-end request tracing

---

### Cross-Functional Collaboration Details

**1. Technical Artists (Rendering Team):**
- **Context:** Applied scientists and technical artists handled real-time AR rendering, face tracking
- **Collaboration:** Regular syncs on visual calibration
- **Example Challenge:** "What RGB values look realistic across different skin tones in AR?"
- **My Approach:** Data-driven discussions using experimental results from real users
- **Outcome:** Aligned on color accuracy standards that balanced technical precision with visual realism

**2. Designers:**
- **Context:** Sister team (Customer Experience) owned front-end UX including before/after slider feature
- **Collaboration:** Visual property standards, UX requirements
- **Example Challenge:** Balancing design goals (immediate visual feedback) with technical constraints (processing time)
- **My Approach:** Prototyped solutions, showed trade-offs with real data
- **Outcome:** Agreed on asynchronous processing with progress indicators

**3. Data Scientists / Applied Scientists:**
- **Context:** Created and trained ML models for bounding boxes and color extraction
- **Collaboration:** Model training, validation experiments, feature engineering
- **Example Challenge:** Insufficient labeled training data initially
- **My Approach:** Established SageMaker Ground Truth pipeline, recruited data labelers
- **Outcome:** Built high-quality training dataset, improved model accuracy

**4. Product Managers:**
- **Context:** Defined requirements for what visual properties to extract
- **Collaboration:** Requirements gathering, working backward from product vision
- **Example Challenge:** Initial requirements were vague ("make AR try-on realistic")
- **My Approach:** Multiple iteration cycles, prototyped early to clarify disconnects
- **Outcome:** Concrete requirements: RGB values, product dimensions, texture data

**5. 3D Asset Creation Team (External to Beauty Tech):**
- **Context:** Specialized team created 3D models from our extracted properties
- **Collaboration:** Defined data format handoffs, API contracts
- **Example Challenge:** One instance where coordinate system context was misunderstood
- **My Approach:** Scheduled meeting to clarify, documented assumptions
- **Leadership Decision:** Respected their expertise (they're 3D modeling experts), guided overall direction without micromanaging
- **Outcome:** Smooth handoff pipeline, they handled 3D generation autonomously

**6. Beauty Brand Bridge Teams:**
- **Context:** Teams interfacing with beauty brand clients (L'Oréal, Maybelline, etc.)
- **Collaboration:** Improved product photo submission platform
- **Example Challenge:** Non-standard photo submissions (lighting, angles, backgrounds varied wildly)
- **My Approach:** Worked backward—"Why are photos bad quality?"—guided standardization of submission forms
- **Outcome:** Created internal standards for color values, naming conventions, photo quality (lighting, resolution, angles) adopted organization-wide

---

### Key Technical Decisions & Leadership

**Decision 1: Not Binding to Current State**
- Designed for scalability—new beauty brands joining continuously
- Created standardized onboarding process for future partners
- Established naming conventions adopted across Beauty Tech organization

**Decision 2: Working Backward from Real Problems**
- Didn't just fix immediate symptoms (bad data quality)
- Addressed root causes (product owner submission standards)
- Split work: beauty brands improved submissions, we improved extraction algorithms

**Decision 3: Leverage Partner Team Expertise**
- Consulted senior engineer for architecture design review
- Let 3D asset team handle their domain (didn't reinvent the wheel)
- Let rendering team (applied scientists) handle face tracking and AR
- Still guided them at high level to keep technical direction consistent

**Decision 4: Data Quality as Priority**
- Established best practices for RGB values through user experiments
- Double-blind validation with diverse demographics
- Not just extracting data, but ensuring it produced realistic AR experiences

---

### Impact & Metrics

**Direct Impact:**
- Successfully replaced third-party tool (cost savings)
- Established standards adopted across Beauty Tech organization for future partnerships
- High data quality validated through rigorous user experiments
- Created foundation for standardized beauty brand onboarding

**Broader Context:**
- Part of larger Beauty Tech data lake processing **40TB/day**
- Served **40M+ monthly customers** across 15+ countries
- Pipeline designed for scale and future growth

---

## 🎯 ADDRESSING TYLER'S KEY POINTS

### Tyler's Emphasis from Recruiter Screen:

✅ **"Cross-functional collaboration is a big part of the role"**
→ VTO project coordinated 6 teams across 3 time zones

✅ **"Need someone who honestly, kind of enjoys that"**
→ Emphasize: "I genuinely enjoy bridging technical and creative teams. It's challenging but rewarding."

✅ **"Talk about working with tech artists and game devs—that's certainly a plus"**
→ Amazon rendering team + UBC game dev capstone

✅ **"Technical background in cloud-based full stack development, AI solutions"**
→ VTO demonstrates full stack: data ingestion → ML pipeline → API → infrastructure → monitoring

✅ **"AWS experience"**
→ 5 years, extensive use of Lambda, SageMaker, Step Functions, DynamoDB, S3, CloudFormation

✅ **"Working across many different technologies"**
→ Event-driven architecture, ML training, serverless, IaC, multiple languages (Python, TypeScript)

---

## 🚀 ADDITIONAL STRONG PROJECT: PROJECT SCOTT (Backup Story)

**If they ask for another example or different angle:**

### Project Scott - 30-Second Version

"Another strong example is Project Scott, an AI agent system I built for answering team questions from internal documentation.

**The Problem:** New engineers had many technical questions (CI/CD, admin, infrastructure), documentation was scattered, SMEs repeatedly answered same questions.

**The Solution:** Built RAG-based AI agent with vector embeddings, LLM-powered Q&A, integrated with SageMaker for model hosting. Named it 'Project Scott' to anthropomorphize and encourage adoption. If AI couldn't find an answer, it automatically escalated to subject matter experts, then fed their responses back into documentation.

**The Architecture:** API Gateway + Lambda orchestration, SageMaker endpoints for inference, DynamoDB for session state, S3 for documents, CloudWatch/X-Ray for observability, AWS CDK + CloudFormation for IaC.

**The Impact:**
- **82% improvement** in resolution time
- **240+ dev-hours/month saved** across organization
- **100% documentation coverage** (led org-wide workshop)
- High adoption rate—became go-to resource

**Why I'm Mentioning This:** Shows different angle of my full-stack ML experience, and demonstrates leadership (drove org-wide adoption, led documentation workshop)."

**[Use this if they ask: "Tell me about another ML project" or "What's your experience with AI agents/LLMs?"]**

---

## 💼 ANTICIPATED BEHAVIORAL QUESTIONS

### "Describe a time you received difficult feedback"

**Example: VTO Project Architecture Review**

**Situation:** Early in VTO project, proposed initial architecture to senior engineer for review.

**Feedback:** "This design won't scale beyond small volume. Your Step Functions orchestration will timeout with large batches. Need to rethink data partitioning and parallel processing."

**Initial Reaction:** Felt defensive—I'd spent 3 days on that design. But took a step back.

**Action:** 
- Scheduled follow-up meeting to understand concerns deeply
- Asked clarifying questions about expected scale (turned out: 10x what I'd designed for)
- Acknowledged gaps in my initial assumptions
- Redesigned with parallel processing, optimized Lambda memory allocation, implemented DynamoDB caching layer

**Result:** Final architecture scaled to 40TB/day serving 40M+ users. Strengthened relationship with senior engineer—now proactively seek architecture reviews before full implementation.

**Learning:** Feedback is a gift. Senior engineers have context I don't. Now I always ask "What scale should this handle?" upfront.

---

### "Tell me about handling competing priorities from different teams"

**Example: VTO Project—Beauty Brand Submissions vs ML Model Training**

**Situation:** Beauty brand bridge teams wanted faster onboarding (pressure from executives to sign more brands). Data scientists needed higher quality training data (couldn't train good models without it).

**Conflict:** Bridge teams wanted to accept any photo submissions to speed onboarding. Data scientists wanted strict photo standards to ensure model accuracy.

**My Approach:**
- Facilitated meeting with both teams to align on priorities
- Brought data: showed experimental results proving low-quality photos = poor AR realism = bad customer experience = churn
- Proposed compromise: phased approach
  - **Phase 1:** Accept current submissions, use manual review bottleneck
  - **Phase 2:** Work with beauty brands to improve submission standards
  - **Phase 3:** Automated pipeline with high-quality inputs

**Communication:**
- Regular status updates to both teams
- Documented decisions and trade-offs
- Managed expectations on timelines

**Result:** Both teams bought in. Established photo standards that beauty brands adopted, improved data quality over time, no compromise on customer experience.

---

### "How do you ensure effective communication with non-technical stakeholders?"

**Example: Explaining ML Pipeline Delays to Product Managers**

**Challenge:** PMs didn't understand why color extraction took "so long" (in their view). Kept asking "Can't you just speed it up?"

**My Approach:**
1. **Visual Demonstrations:** Showed them side-by-side examples of "fast but inaccurate" vs "slower but accurate" color extraction in AR try-on
2. **User Impact:** Explained in terms they cared about—"Fast but wrong colors = customers buy wrong shade = returns = bad reviews"
3. **Analogies:** "It's like photo editing—you can apply a filter in 1 second, but professional color grading takes time for realism"
4. **Trade-off Transparency:** Gave options with clear trade-offs (speed vs accuracy vs cost)
5. **Regular Updates:** Bi-weekly syncs with dashboards showing progress, not just technical jargon

**Result:** PMs understood trade-offs, stopped pushing for speed over quality, advocated for realistic timelines with leadership.

**Key Learning:** Non-technical stakeholders care about user impact and business outcomes. Translate technical constraints into their language.

---

## 🔧 TECHNICAL DEEP-DIVE PREPARATION (for Rhea - Technical Director)

### AWS Serverless Architecture for Real-Time ML Inference

**High-Level Architecture:**

```
User → API Gateway → Lambda (orchestration) → SageMaker Endpoint (inference) → Lambda (post-processing) → Response
                                ↓
                         DynamoDB (caching, session state)
                                ↓
                         CloudWatch + X-Ray (monitoring)
```

**Component Breakdown:**

1. **API Gateway:**
   - REST API endpoint with resource policies
   - Cognito for authentication (user pools)
   - API keys + usage plans for rate limiting
   - Request/response transformation
   - Caching layer for frequently requested predictions

2. **Lambda (Orchestration):**
   - Preprocessing: input validation, feature engineering
   - Invoke SageMaker endpoint with boto3
   - Post-processing: format response, business logic
   - Error handling and retries
   - **Optimization:** Provisioned Concurrency to reduce cold starts
   - **Optimization:** Connection pooling (reuse SageMaker endpoint connections)

3. **SageMaker Endpoint:**
   - Real-time inference endpoint
   - Auto-scaling based on invocation metrics
   - Multi-variant for A/B testing
   - Data capture for model monitoring
   - Model artifact in S3, inference container

4. **DynamoDB:**
   - Session state (user context for multi-turn interactions)
   - Caching layer for recent predictions
   - TTL for automatic cleanup
   - On-demand billing or provisioned capacity with auto-scaling

5. **CloudWatch + X-Ray:**
   - CloudWatch Logs for Lambda execution logs
   - CloudWatch Metrics: invocation count, duration, errors, SageMaker latency
   - Custom metrics: prediction confidence, data quality
   - CloudWatch Alarms: trigger SNS on errors or latency spikes
   - X-Ray: distributed tracing across API Gateway → Lambda → SageMaker

6. **Infrastructure as Code:**
   - AWS CDK (TypeScript) or SAM (YAML)
   - Modular stacks for reusability
   - Environment-specific parameters (dev/staging/prod)
   - CI/CD pipeline with automated testing

**Scalability Considerations:**
- Lambda concurrency limits (account level, function level)
- SageMaker endpoint instance count and auto-scaling policies
- DynamoDB throughput (on-demand vs provisioned)
- API Gateway throttling limits

**Security:**
- IAM roles with least privilege
- VPC configuration for Lambda (if accessing private resources)
- Encryption at rest (S3, DynamoDB) and in transit (TLS)
- Secrets Manager for API keys and credentials

**Experience:** "I've implemented this exact pattern multiple times at Amazon for both Project Scott (AI Q&A) and VTO project (visual property extraction). Both scaled to support 40M+ monthly users."

---

### Lambda Cold Starts - Mitigation Strategies

**What is a Cold Start:**
- Initial latency when Lambda spins up new execution environment
- Load code, initialize dependencies, establish connections
- Critical for ML inference: large dependencies (ML libraries, model artifacts)

**Mitigation Strategies (from my experience):**

1. **Provisioned Concurrency:**
   - Keep functions warm (pre-initialized execution environments)
   - Cost trade-off: pay for idle capacity, but eliminate cold starts
   - Used this for critical paths in VTO pipeline

2. **Minimize Package Size:**
   - Only include necessary dependencies (not entire ML library if only using inference)
   - Use Lambda Layers for shared dependencies
   - Reduced deployment package from 250MB to 50MB in Project Scott

3. **Lazy Loading:**
   - Load ML model on first invocation, cache in global scope
   - Connection pooling (establish DB connections once, reuse)
   - Example: Load SageMaker endpoint connection once, reuse across invocations

4. **Runtime Optimization:**
   - Chose compiled languages for performance-critical paths (though Python for ML)
   - Increased Lambda memory allocation (more CPU = faster init)
   - Tested: 512MB vs 2GB memory—2GB had 50% faster cold starts for our workload

5. **Architecture Patterns:**
   - Offload heavy processing to SageMaker endpoints (keep Lambda lightweight)
   - Use Step Functions for orchestration (Lambda only does specific tasks)
   - Async processing via SQS/SNS for non-latency-sensitive workloads

**Metrics from My Projects:**
- Before optimization: p95 cold start ~500ms, p99 ~1200ms
- After optimization: p95 <100ms, p99 ~300ms
- Goal: Keep p95 under 100ms for good UX

---

### SageMaker Deployment Process

**Core Components:**

1. **Model:**
   - Model artifact (trained model in S3: .tar.gz with model files)
   - Inference code (custom Python script or framework container: TensorFlow, PyTorch, scikit-learn)
   - Container image (AWS pre-built or custom Docker image)

2. **Endpoint Configuration:**
   - Instance type (ml.m5.large for lightweight, ml.p3.2xlarge for GPU inference)
   - Instance count (start with 1, scale up)
   - Auto-scaling policies (target tracking on invocations per instance)
   - Data capture config (log inputs/outputs for model monitoring)
   - Multi-variant (A/B testing multiple model versions)

3. **Endpoint:**
   - REST API for real-time inference
   - Invoke via boto3 (Python SDK)
   - Returns predictions synchronously

**Deployment Steps (from my projects):**

1. **Train Model:**
   - SageMaker training job (AWS managed) OR
   - External training (local, another platform) → upload artifact to S3

2. **Create Model Object:**
   ```python
   model = sagemaker.Model(
       model_data='s3://bucket/model.tar.gz',
       image_uri='<container_image>',
       role='<IAM_role>',
   )
   ```

3. **Deploy Endpoint:**
   ```python
   predictor = model.deploy(
       instance_type='ml.m5.large',
       initial_instance_count=1,
       endpoint_name='my-endpoint'
   )
   ```

4. **Invoke for Inference:**
   ```python
   response = predictor.predict(input_data)
   ```

5. **Monitor:**
   - CloudWatch metrics: Invocations, ModelLatency, Overhead
   - SageMaker Model Monitor: data drift, model quality
   - Set alarms on error rates and latency

**Advanced Patterns:**
- **Multi-variant endpoints:** Deploy 2 model versions, route 90% to v1, 10% to v2 for A/B testing
- **Multi-model endpoints:** Host multiple models on single endpoint (cost optimization)
- **Auto-scaling:** Target 1000 invocations per instance, scale up/down automatically

**Experience:** "Used SageMaker extensively for both Project Scott (NLP models for Q&A) and VTO project (computer vision for bounding boxes and color extraction). Managed full lifecycle: training, deployment, monitoring, updates."

---

### DynamoDB Data Modeling for Real-Time Applications

**Design Principles:**

1. **Primary Key Design:**
   - **Partition Key (required):** Should distribute data evenly, enable primary access pattern
   - **Sort Key (optional):** Allows range queries within partition

**Example: User Profile for Recommendation Engine**

**Access Patterns:**
1. Get user profile by userId
2. Get user's recent activity (last 30 days)
3. Get user's preferences

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
- **Partition Key = userId:** Ensures even distribution (each user is a partition), enables user-specific queries
- **Sort Key = dataType#timestamp:** Allows querying by data type ("give me all PROFILE items") and sorting by timestamp ("recent activity first")

**Query Examples:**

```python
# Get user profile
response = table.query(
    KeyConditionExpression=Key('userId').eq('user123') & Key('dataType#timestamp').begins_with('PROFILE')
)

# Get recent activity (last 7 days)
response = table.query(
    KeyConditionExpression=Key('userId').eq('user123') & Key('dataType#timestamp').between('ACTIVITY#2025-10-02', 'ACTIVITY#2025-10-09'),
    ScanIndexForward=False  # Sort descending (most recent first)
)
```

**Global Secondary Index (GSI):**
If we need to query by `lastActive` timestamp across all users:

```
GSI:
- Partition Key: status (string: "ACTIVE" or "INACTIVE")
- Sort Key: lastActive (timestamp)
```

Now we can query: "Give me all active users sorted by last active time"

**Best Practices (from my experience):**
- **Avoid scans:** Always query with partition key
- **Use TTL:** Automatic deletion of expired data (session data, cache)
- **Batch operations:** BatchGetItem, BatchWriteItem for efficiency
- **On-demand vs provisioned:** On-demand for unpredictable traffic, provisioned with auto-scaling for steady traffic
- **DynamoDB Streams:** Trigger Lambda on data changes (used this in VTO project for downstream processing)

**Experience:** "Used DynamoDB extensively at Amazon for session state (Project Scott), caching (VTO project), and user context. Designed schemas for sub-100ms read latency at scale."

---

### Infrastructure as Code with CloudFormation/CDK

**Philosophy:**
- **Reproducibility:** Same infrastructure in dev, staging, prod
- **Version Control:** Infrastructure changes tracked in Git
- **Automation:** Deploy via CI/CD, no manual clicks in console
- **Consistency:** Eliminate configuration drift

**Tool: AWS CDK (Cloud Development Kit)**

**Why CDK over raw CloudFormation:**
- Write infrastructure in TypeScript/Python (familiar languages)
- Constructs (reusable components) vs repetitive YAML
- Compile-time checks (catch errors before deployment)
- Generates CloudFormation under the hood

**Example from Amazon Projects:**

**Project Structure:**
```
infrastructure/
├── lib/
│   ├── lambda-stack.ts       # Lambda functions
│   ├── api-stack.ts          # API Gateway
│   ├── ml-stack.ts           # SageMaker endpoints
│   ├── database-stack.ts     # DynamoDB tables
│   ├── monitoring-stack.ts   # CloudWatch alarms, dashboards
│   └── pipeline-stack.ts     # CI/CD pipeline
├── bin/
│   └── app.ts                # Entry point, defines stages
├── test/
│   └── infrastructure.test.ts
└── cdk.json
```

**Key Components I Deployed with CDK:**

1. **Lambda Functions:**
   ```typescript
   const orchestrationLambda = new lambda.Function(this, 'OrchestrationLambda', {
     runtime: lambda.Runtime.PYTHON_3_9,
     code: lambda.Code.fromAsset('lambda/orchestration'),
     handler: 'index.handler',
     timeout: Duration.seconds(30),
     memorySize: 1024,
     environment: {
       SAGEMAKER_ENDPOINT: sagemakerEndpoint.endpointName,
       DYNAMODB_TABLE: table.tableName,
     },
   });
   ```

2. **API Gateway:**
   ```typescript
   const api = new apigateway.RestApi(this, 'MLApi', {
     restApiName: 'ML Inference API',
     deployOptions: {
       stageName: 'prod',
       tracingEnabled: true,  // X-Ray
     },
   });
   
   const resource = api.root.addResource('predict');
   resource.addMethod('POST', new apigateway.LambdaIntegration(orchestrationLambda), {
     authorizationType: apigateway.AuthorizationType.COGNITO,
     authorizer: cognitoAuthorizer,
   });
   ```

3. **DynamoDB Table:**
   ```typescript
   const table = new dynamodb.Table(this, 'SessionTable', {
     partitionKey: { name: 'userId', type: dynamodb.AttributeType.STRING },
     sortKey: { name: 'timestamp', type: dynamodb.AttributeType.STRING },
     billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
     timeToLiveAttribute: 'ttl',
   });
   ```

4. **CloudWatch Alarms:**
   ```typescript
   const errorAlarm = orchestrationLambda.metricErrors().createAlarm(this, 'ErrorAlarm', {
     threshold: 10,
     evaluationPeriods: 1,
     alarmDescription: 'Alert when Lambda errors exceed 10 in 1 minute',
   });
   
   errorAlarm.addAlarmAction(new cw_actions.SnsAction(alertTopic));
   ```

**CI/CD Pipeline (4 Stages):**

1. **Dev:** Deploy on every commit to `dev` branch (no approval)
2. **Gamma:** Deploy on merge to `main` (automated tests, manual approval)
3. **Pre-Prod:** Deploy after Gamma success (canary deployment, 10% traffic)
4. **Prod:** Deploy after Pre-Prod validation (full rollout)

**Best Practices:**
- **Modular design:** Separate stacks for different components (easier to update, less blast radius)
- **Parameterization:** Environment-specific configs (e.g., instance types differ in dev vs prod)
- **Testing:** CDK has built-in testing (assert stack has X resources)
- **Documentation:** Inline comments, README with architecture diagrams

**Impact:** "Achieved 95% reduction in deployment errors, repeatable infrastructure across 4 environments, infrastructure changes code-reviewed just like application code."

---

## 🙋 QUESTIONS TO ASK INTERVIEWERS

### For Daniel (Hiring Manager):
1. "Can you tell me more about the day-to-day responsibilities in the first 90 days? Tyler mentioned learning the Frostbite codebase—how does that ramp-up typically look?"
2. "What does success look like for this role in the first 6 months?"
3. "How does this team collaborate with other EA studios? Are there opportunities to work on projects across multiple games?"

### For Blaze (Director):
1. "You oversee Production Operations & Technology across EA's global studios—what are the biggest operational challenges you're solving right now?"
2. "How do you see the role of AI/ML evolving in EA's content production workflows over the next few years?"
3. "What does effective cross-functional collaboration look like on your team? Any examples of recent successes?"

### For Rhea (Technical Director):
1. "What's the technical architecture for EA's online services? Are there specific scalability challenges you're tackling?"
2. "How does the team balance rapid experimentation with maintaining production stability?"
3. "What AWS services or cloud technologies is the team most excited about adopting or expanding?"

### General (If Time Allows):
1. "What do you enjoy most about working at EA?"
2. "How does the team stay up-to-date with rapidly evolving AI/ML technologies?"

---

## ⚠️ CRITICAL REMINDERS FROM LEARNING POINTS (File 11)

### DON'T RAMBLE (Top Priority):
- ❌ **What Went Wrong:** Spent 2+ minutes on Project Scott in recruiter screen when 30-45 seconds would work
- ✅ **Fix:** Answer in 30-60 seconds, THEN offer to elaborate
- ✅ **Technique:** "I can go deeper into any aspect—technical architecture, cross-team collaboration, or impact. What would be most useful?"

### WATCH INTERVIEWER CUES:
- If they say "Great" or "Perfect" → **STOP TALKING**
- If they're taking notes → **PAUSE** to let them catch up
- If they say "That's exactly what I was looking for" → **MOVE ON**

### USE STAR METHOD (60 seconds max):
- **S**ituation: 10 seconds
- **T**ask: 10 seconds
- **A**ction: 30 seconds
- **R**esult: 10 seconds (with metric)

### BE CONCISE FIRST:
- Give 2-3 key points
- Pause
- Let them ask for details
- Don't explain everything at once

---

## 📋 PRE-INTERVIEW CHECKLIST (Do This NOW)

### Physical Setup (30 minutes before):
- [ ] Test video/audio setup
- [ ] Good lighting (face clearly visible)
- [ ] Quiet room, no distractions
- [ ] Phone on silent
- [ ] Water nearby
- [ ] Close unnecessary browser tabs

### Documents to Have Open:
- [ ] This prep guide
- [ ] Job description (02_formatted_jd.md)
- [ ] Your resume
- [ ] Interviewer research (13_Interviewer_Names_Email_Chain.md)
- [ ] Notepad for taking notes during interview

### Mental Preparation:
- [ ] Practice "Tell me about yourself" OUT LOUD 3 times (time yourself: 60-90 seconds)
- [ ] Practice VTO project walkthrough OUT LOUD 2 times (time yourself: 45 seconds)
- [ ] Practice technical artist collaboration answer OUT LOUD 1 time (60 seconds)
- [ ] Take 5 deep breaths before joining call
- [ ] Mindset: "I'm qualified, I've done this work, I'm here to have a conversation"

---

## 🎯 YOUR COMPETITIVE ADVANTAGES (Confidence Boosters)

✅ **5 years AWS + ML experience** (exactly what they need)
✅ **VTO project perfectly demonstrates:** full-stack ML, AWS serverless, cross-functional collaboration, technical artist work
✅ **Project Scott as backup:** different angle of ML expertise (RAG, LLM, AI agents)
✅ **Game dev experience** (UBC capstone) = BIG PLUS per Tyler
✅ **Led team of 8 engineers** = leadership capability
✅ **Impressive metrics:** 82% improvement, 240 dev-hrs saved, 100% docs, 40TB/day, 40M+ users
✅ **Infrastructure as Code expertise** (AWS CDK, CloudFormation)
✅ **Cross-functional collaboration across 6 teams** = exactly what Blaze wants to see

---

## 🚀 YOU'VE GOT THIS!

**Remember:**
- You've built exactly what they're looking for
- You have the technical depth (Rhea will be impressed)
- You have the cross-functional experience (Blaze will be impressed)
- You have the full-stack ML expertise (Daniel will be impressed)
- Tyler already liked you in the recruiter screen
- **Just be concise, watch cues, and let them ask follow-up questions**

**Final Mindset:** This is a conversation between peers, not an interrogation. You're evaluating them as much as they're evaluating you. Be confident, be yourself, and show genuine enthusiasm for the role.

---

**GOOD LUCK! 🎮🚀**

