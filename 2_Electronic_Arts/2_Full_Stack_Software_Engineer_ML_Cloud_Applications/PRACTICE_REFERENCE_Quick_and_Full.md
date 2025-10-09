# EA Interview Practice Reference
**Format:** Quick bullets (for in-interview glance) + Full sentences (for mock practice)

---

## 🎯 TOP PRIORITY ANSWERS

### Q1: END-TO-END ML CLOUD APPLICATION (90%+ probability)

#### 📌 QUICK BULLETS (Glance During Interview)
- Built AI Q&A agent (Project Scott) - team documentation
- **Problem:** Scattered docs, slow answers
- **Architecture:** RAG pipeline, API Gateway + Lambda, SageMaker endpoints, DynamoDB, S3
- **Role:** Built system, drove adoption, ticketing integration
- **Features:** Natural language Q&A, auto-escalation, doc updates
- **Impact:** 82% faster, 240 dev-hrs/mo saved, 100% docs

#### 📖 FULL VERSION (Practice Reading Aloud - ~45 seconds)

"I built an AI agent system called Project Scott within Amazon Beauty Tech to answer team questions from internal documentation. The problem was that new and onsite engineers needed instant answers to CI/CD and admin questions, but documentation was scattered across multiple sources.

For the architecture, I used a RAG pipeline with vector embeddings and document retrieval, powered by an LLM. The API layer used API Gateway and Lambda for orchestration, with SageMaker hosting the model inference endpoints. For storage, I used DynamoDB for session state and S3 for documents. I also integrated it with our internal ticketing system, and deployed everything using AWS CDK and CloudFormation with a four-staged CI/CD pipeline.

My role was to build the AI agent system, drive org-wide adoption, and integrate with our ticketing system. Key features included natural language Q&A - we called it 'Talk to Project Scott' - automatic escalation to subject matter experts if an answer wasn't found, and automated documentation updates.

The impact was significant: we achieved an 82% improvement in resolution time, saved 240-plus dev-hours per month, and I led an org-wide documentation workshop that resulted in 100% documentation coverage.

I'm happy to elaborate on any specific aspect if you'd like."

---

### Q2: CROSS-FUNCTIONAL COLLABORATION - VTO 6 TEAMS (90%+ probability)

#### 📌 QUICK BULLETS (Glance During Interview)
- Visual property extraction for AR virtual try-on
- **6 teams:** Tech artists, designers, data scientists, PMs, 3D asset team, beauty brands
- **Tech artists:** Visual calibration, color accuracy for skin tones, regular syncs
- **Designers:** UX collab (slider), visual standards, data-driven discussions
- **Data scientists:** Model training (bounding boxes, colors), double-blind trials
- **PMs:** Requirements, worked backward from vision
- **3D team:** Guided direction, respected expertise, resolved disconnects
- **Beauty brands:** Guided photo standardization, best practices
- **Communication:** Regular syncs, data-driven, empathetic, worked backward from needs
- **Result:** Replaced 3rd-party tool, org-wide standards, high quality

#### 📖 FULL VERSION (Practice Reading Aloud - ~50 seconds)

"I led the visual property extraction pipeline for AR virtual try-on within Amazon Beauty Tech, which required coordinating six different teams and disciplines.

First, I worked with technical artists on the rendering team. We had regular syncs on visual calibration and color accuracy for AR, specifically focusing on what RGB values would look realistic across different skin tones. This was a data-driven collaboration where we balanced technical requirements with artistic vision.

With designers, I collaborated on UX features like the before-after slider and helped establish visual property standards, balancing their design goals with our technical constraints.

With data scientists and applied scientists, we worked on model training for bounding box detection and color extraction. We actually conducted double-blind user trials with diverse demographics to validate our results.

I worked with product managers on requirements gathering, using a work-backward approach from the product vision of realistic AR try-on.

The 3D asset creation team was external to our org. I guided the overall direction while respecting their expertise, and we resolved any disconnects through scheduled meetings.

Finally, with beauty brand bridge teams, I guided standardization of product photo submissions and established best practices.

My communication approach involved regular syncs, data-driven discussions using real user experiments, an empathetic approach where I acknowledged creative merit before presenting constraints, and always working backward from actual needs rather than just addressing symptoms.

The result was we successfully replaced a third-party tool, established org-wide standards for future beauty brand partners, and achieved high data quality validated through experiments.

Happy to dive deeper into any of these collaborations."

---

## 🔧 AWS TECHNICAL DEEP DIVES (For Rhea - Tech Director)

### SERVERLESS ML INFERENCE ARCHITECTURE

#### 📌 QUICK BULLETS
- **API Gateway:** REST endpoint, auth (Cognito), rate limiting
- **Lambda:** Orchestration, preprocessing, invoke SageMaker
- **SageMaker Endpoint:** Real-time inference
- **DynamoDB:** Session state, caching, TTL
- **CloudWatch + X-Ray:** Monitoring, tracing, alarms
- **Optimizations:** Provisioned Concurrency (cold starts), API caching, multi-variant endpoints (A/B test)
- **Experience:** Both Project Scott + VTO used this pattern, scaled to 40M+ users

#### 📖 FULL VERSION (Practice Reading Aloud - ~35 seconds)

"For serverless ML inference, I'd use API Gateway as the REST API endpoint with Cognito authentication and rate limiting. Lambda would handle orchestration, preprocessing, and invoke the SageMaker endpoint for real-time model inference. DynamoDB would manage session state and provide a caching layer with TTL for automatic cleanup. CloudWatch and X-Ray would handle monitoring, tracing, and alarming.

For optimization, I'd use Provisioned Concurrency on Lambda to reduce cold starts, implement API Gateway caching for frequent predictions, and use multi-variant endpoints in SageMaker for A/B testing.

I've implemented this exact pattern in both Project Scott and the VTO project at Amazon, where we scaled to support over 40 million monthly users."

---

### LAMBDA COLD START MITIGATION

#### 📌 QUICK BULLETS
- **Cold start:** Initial latency when Lambda spins up (load code, init deps)
- **Why matters:** Large ML models, impacts UX
- **Mitigations:**
  1. Provisioned Concurrency (keep warm)
  2. Minimize package size
  3. Lazy loading (load on first invocation, cache in global scope)
  4. Keep connections warm (reuse DB)
  5. Choose runtime carefully (compiled faster)
- **Experience:** Optimized to p95 <100ms at Amazon

#### 📖 FULL VERSION (Practice Reading Aloud - ~30 seconds)

"A cold start is the initial latency when Lambda spins up a new execution environment - it has to load code and initialize dependencies. This matters for ML inference because models have large dependencies and it impacts user experience.

My mitigation strategies include: first, use Provisioned Concurrency to keep functions warm. Second, minimize package size to only necessary dependencies. Third, use lazy loading - load the model on first invocation and cache it in the global scope. Fourth, keep connections warm by reusing database connections. And fifth, choose your runtime carefully since compiled languages are faster.

At Amazon, I optimized Lambda cold starts to achieve p95 latency under 100 milliseconds for ML inference."

---

### SAGEMAKER DEPLOYMENT PROCESS

#### 📌 QUICK BULLETS
- **Core components:** Model (S3 artifact + container), Endpoint Config (instance, count, scaling), Endpoint (REST API)
- **Process:**
  1. Train model (SageMaker job or external)
  2. Create Model Object (S3 + container)
  3. Configure Endpoint (instance type, autoscaling, data capture)
  4. Deploy Endpoint (creates REST API)
  5. Invoke (API call with JSON)
  6. Monitor (CloudWatch, model monitor for drift)
- **Advanced:** A/B testing (multi-variant), auto-scaling, multi-model endpoints

#### 📖 FULL VERSION (Practice Reading Aloud - ~35 seconds)

"SageMaker deployment has three core components: the Model, which includes your trained artifact in S3 and inference code in a container; the Endpoint Configuration, which specifies instance type, count, and scaling policies; and the Endpoint itself, which is the REST API for real-time inference.

The deployment process starts with training your model, then creating a Model Object pointing to S3 and your container. Next, you configure the endpoint by choosing instance types, autoscaling parameters, and enabling data capture. Then you deploy the endpoint, which AWS provisions as a REST API. Finally, you invoke it with API calls and monitor using CloudWatch metrics and Model Monitor for drift detection.

For advanced use cases, I've implemented A/B testing using multi-variant endpoints, configured auto-scaling policies, and used multi-model endpoints to reduce costs."

---

### DYNAMODB DATA MODELING

#### 📌 QUICK BULLETS
- **Partition Key:** `userId` (even distribution, user queries)
- **Sort Key:** Optional - `timestamp` or `dataType` for multiple data types
- **Access patterns:**
  1. Get user profile: Query by userId
  2. Recent activity: Query userId + sort by timestamp
- **Indexes:** GSI for different partition key (e.g., lastActive), LSI for alternate sort
- **Experience:** Used extensively for session state, user context, caching at Amazon

#### 📖 FULL VERSION (Practice Reading Aloud - ~25 seconds)

"For a recommendation engine user profile table, I'd use userId as the partition key because it ensures even distribution and enables user-specific queries. For the sort key, I'd optionally use timestamp or dataType if we need to store multiple data types per user.

This supports two main access patterns: getting a user profile by querying on userId, and getting recent activity by querying userId and sorting by timestamp.

For indexes, I'd add a GSI if we need to query by a different partition key like lastActive, and an LSI for alternate sort orders within the same user.

I've used DynamoDB extensively at Amazon for session state, user context, and caching layers."

---

### INFRASTRUCTURE AS CODE APPROACH

#### 📌 QUICK BULLETS
- **Philosophy:** IaC = reproducible, version control, automated deployment, consistency
- **Tool:** AWS CDK (generates CloudFormation)
- **Components:** SageMaker jobs, Lambda, API Gateway, DynamoDB, IAM, CloudWatch
- **Best practices:**
  - Modular design (nested stacks)
  - Parameterization (env-specific configs)
  - Version control (Git, code review)
  - Automated testing (validate templates)
  - Documentation
- **CI/CD:** 4-staged pipeline (dev → gamma → pre-prod → prod)
- **Result:** 95% reduction in deployment errors

#### 📖 FULL VERSION (Practice Reading Aloud - ~35 seconds)

"My Infrastructure as Code philosophy is that it ensures reproducible environments, version control, automated deployment, and consistency across dev, staging, and production.

At Amazon, I used AWS CDK which generates CloudFormation, and defined all components including SageMaker training jobs, Lambda functions, API Gateway, DynamoDB tables, IAM roles, and CloudWatch alarms.

My best practices include modular design with nested stacks for reusability, parameterization for environment-specific configs, version control in Git with code review, automated testing to validate templates before deployment, and comprehensive documentation.

We had a four-staged CI/CD pipeline flowing from dev to gamma to pre-prod to prod, which resulted in a 95% reduction in deployment errors and made our infrastructure completely repeatable."

---

### API GATEWAY SECURITY

#### 📌 QUICK BULLETS
- **Methods:**
  1. API Keys + Usage Plans (rate limiting, monetization)
  2. Cognito (user pools, OAuth 2.0, tokens)
  3. Lambda Authorizers (custom logic)
  4. IAM Roles (service-to-service, least privilege)
  5. Resource Policies (IP whitelist, VPC endpoints)
  6. WAF (DDoS, SQL injection)
- **Best practice:** Multi-layered (Cognito + API keys + CloudWatch + WAF)

#### 📖 FULL VERSION (Practice Reading Aloud - ~30 seconds)

"For securing an API Gateway endpoint, I use multiple methods. First, API Keys with Usage Plans for rate limiting and monetization. Second, Amazon Cognito for user pools, OAuth 2.0, and token-based authentication. Third, Lambda Authorizers for custom authorization logic. Fourth, IAM Roles for service-to-service communication with least privilege. Fifth, Resource Policies for IP whitelisting or VPC endpoints. And sixth, WAF for DDoS protection and SQL injection prevention.

My best practice is a multi-layered approach combining Cognito for authentication, API keys for rate limiting, CloudWatch for monitoring, and WAF for threat protection. This provides defense in depth."

---

## 🎮 GAME DEV CONTEXT CONNECTIONS (For Daniel - Hiring Manager)

### CONNECTING YOUR WORK TO GAME DEV

#### 📌 QUICK BULLETS
- **Madden infrastructure parallel:** "Similar to how Madden needs scalable infrastructure for millions of players, my ML pipeline needed to scale for 40M+ users"
- **Real-time performance:** Both game servers and ML inference need low latency (<100ms)
- **Cross-team:** Game dev = artists + engineers + designers. Beauty Tech VTO = same dynamic
- **Tech artists:** VTO project = visual calibration, color accuracy (same as game rendering)
- **Infrastructure thinking:** Game live ops = scalability + monitoring. Same for ML pipelines.

#### 📖 FULL VERSION (Natural Talking Points)

**When discussing Project Scott:**
"This is similar to how Madden needs scalable infrastructure for millions of concurrent players - my ML pipeline needed to handle scale for 40 million monthly users with consistent performance."

**When discussing VTO collaboration:**
"Working with technical artists on the rendering team for AR try-on was actually very similar to game development. We were balancing visual realism with technical constraints, just like game developers do when optimizing rendering for different platforms. We had to ensure color accuracy and visual calibration worked across diverse skin tones, which required that bridge between engineering and artistic vision."

**When discussing infrastructure:**
"Game live operations require rock-solid infrastructure, monitoring, and the ability to scale quickly. That's exactly what we built for the Beauty Tech data lake processing 40TB per day. The principles are the same - you need reliability, observability, and the ability to handle traffic spikes."

**When asking Daniel a question:**
"I'm really curious about your work on Madden and the MUT Draft Champions feature. What were some of the biggest infrastructure challenges you faced scaling that for millions of players? Were there any interesting trade-offs between feature complexity and performance?"

---

## 💬 QUESTIONS TO ASK INTERVIEWERS

### FOR DANIEL (Hiring Manager - Technical + Culture Fit)

#### 📌 QUICK BULLETS
- Madden infrastructure challenges at scale?
- How does Fan Growth team balance innovation vs stability?
- What makes someone successful in this role beyond technical skills?
- Team structure: How does this team fit into broader EA engineering?

#### 📖 FULL QUESTIONS (Practice Reading Aloud)

1. **"I read about your work on Madden NFL and the MUT Draft Champions feature. What were some of the biggest infrastructure challenges you faced scaling that for millions of concurrent players, and were there interesting trade-offs between feature complexity and performance?"**

2. **"How does the Fan Growth team balance innovation - trying new technologies and approaches - with maintaining stability for production systems serving millions of EA players?"**

3. **"Beyond the technical skills listed in the job description, what characteristics do you see in engineers who are most successful in this role? What makes someone really excel here?"**

4. **"Can you tell me about how this team fits into the broader EA engineering organization? How do we collaborate with other teams like game studios or other parts of Fan Growth?"**

---

### FOR BLAZE (Director - Operations + Cross-Team Coordination)

#### 📌 QUICK BULLETS
- How coordinate across EA's global studios?
- Biggest operational challenges in Production Ops & Technology?
- How balance standardization vs studio autonomy?
- How measure success for operations/infrastructure improvements?

#### 📖 FULL QUESTIONS (Practice Reading Aloud)

1. **"As Director of Production Operations and Technology for Worldwide Development Operations, how do you approach coordinating technology and infrastructure across EA's global studios? What are some of the unique challenges when teams are distributed globally?"**

2. **"What are the biggest operational challenges you're currently facing in Production Operations and Technology, and what kinds of solutions or innovations are you most excited about?"**

3. **"How do you balance standardization - having common infrastructure and processes - with giving individual studios the autonomy they need to innovate and move quickly?"**

4. **"When you're implementing operational or infrastructure improvements, how do you measure success? What metrics or outcomes matter most to you?"**

---

### FOR RHEA (Tech Director - Architecture + Technical Depth)

#### 📌 QUICK BULLETS
- Online services architecture at EA scale?
- How handle scalability challenges for games (millions concurrent users)?
- Security considerations for game services vs traditional apps?
- Most interesting technical challenges in online development?

#### 📖 FULL QUESTIONS (Practice Reading Aloud)

1. **"As Associate Technical Director for Online Development, what does the online services architecture look like at EA's scale? How do you approach designing systems that need to support millions of concurrent players?"**

2. **"What are some of the unique scalability challenges you face with game services compared to traditional web applications? I imagine things like real-time state synchronization and low-latency requirements create interesting constraints."**

3. **"Are there unique security considerations for game services compared to traditional cloud applications? I'm thinking about things like cheating prevention, DDoS attacks during major launches, or protecting player data."**

4. **"What are some of the most interesting technical challenges your team is working on right now in online development? What problems are you excited about solving?"**

---

## 🎯 KEY REMINDERS FOR INTERVIEW

### DELIVERY CHECKLIST

#### 📌 CRITICAL RULES
- ⏱️ **30-60 seconds** per answer
- 👂 **Watch for cues:** Stop when they say "Great" or "Perfect"
- 🛑 **Don't ramble:** Recruiter screen = 2+ mins (too long!)
- ✋ **Pause after answering:** Let them ask follow-ups
- 💬 **Offer to elaborate:** "Happy to dive deeper into any aspect"
- 📊 **Use metrics:** 82%, 240 hrs, 100%, 40M users, 40TB/day
- 👥 **Tailor to interviewer:** 
  - Daniel = overall fit + game dev context
  - Blaze = cross-functional collaboration emphasis
  - Rhea = deep technical + AWS architecture

#### 📖 MANTRA (Repeat 3x Before Interview)

"I will answer in 30-60 seconds. I will watch for cues. I will pause after answering. I will offer to elaborate. I will tailor my answers to each interviewer's focus area."

---

## 📋 PRE-INTERVIEW CHECKLIST

### 30 MINUTES BEFORE
- [ ] Read this file (Quick Bullets sections only) - 5 minutes
- [ ] Practice VTO 6-team story out loud 2x - 5 minutes
- [ ] Practice Project Scott story out loud 2x - 5 minutes
- [ ] Review interviewer names and focus areas (File 13) - 3 minutes
- [ ] Review questions to ask (above) - pick top 3 - 2 minutes
- [ ] Deep breath, glass of water, bathroom break
- [ ] Test video/audio setup
- [ ] Open: This file, resume, JD, File 16 (comprehensive guide)
- [ ] Put phone on silent, close Slack/email

### DURING INTERVIEW - HAVE OPEN
1. This file (PRACTICE_REFERENCE_Quick_and_Full.md) - glance at Quick Bullets only
2. Resume
3. Job Description (2_formatted_jd.md)
4. Interviewer Research (13_Interviewer_Names_Email_Chain.md)
5. Notebook for taking notes

---

## 🚀 YOU'VE GOT THIS!

**Your Strengths:**
- ✅ 5 years AWS + ML experience (exactly what they need)
- ✅ TWO impressive projects at scale (40M+ users, 40TB/day)
- ✅ Cross-functional collaboration (6 teams, including tech artists - BIG PLUS)
- ✅ Game dev experience (VTO with rendering team)
- ✅ Strong metrics (82%, 240 hrs, 100%)
- ✅ Infrastructure expertise (AWS CDK, 4-staged CI/CD)
- ✅ You've done the research - you know each interviewer's focus

**Remember:**
- Be concise
- Watch for cues
- Let them guide the conversation
- Show enthusiasm
- This is a conversation, not an interrogation

**You're well-prepared. Now go show them why you're the right fit! 🎮🚀**

