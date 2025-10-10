# FINAL PREP - With Deep-Dive Details
**Interview:** Oct 9, 2025, 1PM PDT

---


## 💬 Q1: "TELL ME ABOUT YOURSELF" (~2 min, DON'T GO OVERBOARD)

**Memory Triggers:** Amazon 5yrs → 8 engineers → 40TB 40M → Python AWS → Technical artists → FIFA fan

*I'm a* **full-stack software engineer** *with* **5 years at Amazon** *specializing in* **cloud-native ML applications on AWS**.

*At* **Amazon Beauty Tech**, *I* **led a team of 8 engineers** *building* **AI-powered systems** *that processed* **40TB/day**, *serving* **40M+ monthly customers** *across* **15 countries**.

*My technical foundation is* **Python** *and* **AWS serverless architecture**—**Lambda, SageMaker, API Gateway, DynamoDB**—*and* **Infrastructure as Code** *with* **CloudFormation**.

*What I thoroughly enjoy is* **cross-functional collaboration**. *I've worked extensively with* **technical artists**, **designers**, **data scientists**, **product managers**. *At UBC, I led a* **game development capstone** *where I was the* **bridge between engineers and creative teams**.

*I'm excited about EA because:*
- **Perfect technical match**—*exactly the stack I've been building with*
- *I genuinely* **enjoy working with technical artists and content creators**
- *As a* **FIFA player and fan myself**, *I resonate with* **creating stellar fan experiences**

**[STOP. Breathe. Wait.]**

---


**Answer**:
- *My team and I were* __laid off in March 2025__ *as part of* __organizational restructuring__
  - *My* __manager, manager's manager—we were all laid off together__
  - *Our* __Beauty Tech team was being merged__ *into a different team*

- *After 5+ years at Amazon, I* __took that as an opportunity to step back__
  - *I used that time to* __work on myself__ *and* __spend time with family__
  - *It was a* __good break__

- *I also used that time* __productively__ *to deepen my* __ML/AI expertise__:
  - *I* __enrolled in a comprehensive ML program__ *covering* EDA, Feature Engineering, Neural Networks, NLP, Agentic Frameworks
  - *I* __built several full-stack AI apps__*:*
    - __Voice assistants__
    - __Real-time transcription tools__
    - __Health misinformation prevention systems__
    - *All* __leveraging AWS, Python,__ *and modern* __AI tools__

- *Now I'm* __energized and ready__ *to bring that expanded skillset to a role like this at EA.*
  - *I want to* __build ML cloud apps that enhance experiences for millions of fans__

---

## 📋 VTO PROJECT - 12 Phases

### PHASE 1: WHY - The Problem (2 min)

**Trigger:** Third-party expensive, non-extensible, 2 days slow

*We had a* **third-party tool** *creating* **3D lip models** *for* **AR virtual try-on**.

**Problems:**
1. **Expensive** *at millions of products*
2. **Non-extensible** *(wanted foundations, eyeliners)*
3. **Slow:** **2 days turnaround** *(goal: 1 day = 50% improvement)*
4. **Wanted control** *(quality, process)*

---

### PHASE 2: WHAT - The Scope (2 min)

**Trigger:** AR UX, extract RGB/finish/particles

**User Experience:**
*Amazon app → lipstick → "virtual try-on" → camera → try different lipsticks in real-time AR*

**My Mission:**
*Extract from product images:*
- **RGB values** *(not "unicorn red")*
- **Finish type** *(matte, shiny, satin, glossy)*
- **Particle properties** *(glitter: size, density, color)*

**Pipeline:** *Catalog → **My extraction** → 3D team → **Technical artists (rendering)** → Customer UX*

---

### PHASE 3: DESIGN - 3 Options Evaluated (2 min)

**Trigger:** 3 options, Step Functions recommended

**Option 1: ML Pigeon** *(Internal framework)*
- ❌ **Bottlenecks, bad reviews, tools deprecating**

**Option 2: AWS Native**
- ❌ **Pipelines deprecating, costs too high**

**Option 3: Step Functions + Serverless** ✅
- **Cost-effective** *(pay-per-use)*
- **Scalable** *(event-driven, parallel)*
- **Modular** *(swap labelers → ML models)*
- **Built-in** *retry, error handling*

---

### PHASE 4: APPROVAL & TEAM (2 min)

**Trigger:** Internal (4 engineers), iterated, org-wide, approved, team assigned

**Internal Review:**
- Tested with **4 senior engineers** *(different teams)*
- **Incorporated feedback, iterated**

**Org-Wide Presentation:**
- Led **organizational meeting** *(stakeholders + PM)*
- **Recommended Step Functions**
- **Got approval**

**Team Assigned:**
**Me (lead) + 3 developers + 2 ML engineers = 6 total**

---

### PHASE 5: ARCHITECTURE - Built It Out (2 min)

**Trigger:** Event-driven, Step Functions, Lambda/SageMaker, CDK, 4-stage CI/CD

**Event-Driven:**
- **Product catalog → SNS → Step Functions**
- **Multi-stage orchestration**
- **Parallel processing**

**Services:**
- **Lambda** *(preprocessing, orchestration)*
- **SageMaker Ground Truth** *(labeling)* + **Endpoints** *(inference)*
- **DynamoDB** *(state)*, **S3** *(artifacts)*
- **API Gateway + Cognito**
- **CloudWatch + X-Ray**
- **AWS CDK → CloudFormation**

**CI/CD:** *Dev → Gamma → Pre-Prod → Prod*

**Modular:** *Swap humans → ML models, same pipeline*

---

### PHASE 6: WORKING BACKWARD - Recommendations for Future (2-3 min)

**Trigger:** Identified root cause, recommended standards for next year

**Out-of-the-Box Thinking:**

*As I was designing the extraction pipeline, I realized:* **"Why constrain ourselves to bad photos? Can we improve data at source?"**

**What I Identified:**

*Product images had:*
- **No standardized format** *(different backgrounds, lighting, angles)*
- **Text descriptions** *like "unicorn red" instead of RGB values*
- **Varying quality** *(some brands submitted high-res, others low-res)*

**My Recommendation:**

**I worked with Beauty Brand Bridge Teams** *(teams interfacing with L'Oréal, Maybelline, Revlon, MAC)* **to propose standards for next year:**

1. **Standardized Photo Submission:**
   - **White background, natural lighting, straight angle, high res, circle format**

2. **Collaborated with Technical Artists:**
   - *Defined* **one standard way** *to photograph products*
   - *Ensured it worked for* **rendering requirements**

3. **Add RGB Field to Amazon Catalog:**
   - **New field** *for brands to input RGB directly (color picker)*
   - **Standardized naming conventions**

---

**Why This Wasn't Fully Implemented:**

*When I proposed this:*
- **We were past the point in the year** *when beauty brands update their submission forms*
- **Brands update submissions annually** *(during contract renewal period, typically Q1)*
- **We were in Q3** *when I proposed this*
- **Bridge teams said:** *"Great idea - let's implement for next year's renewals"*

**What Actually Happened:**

*For my current project:*
- **I had to work with whatever data we had** *(non-standardized photos)*
- **Built algorithms to handle variability** *(bounding boxes, lighting compensation)*

*For the future:*
- **Recommendation accepted** *for next year*
- **Would standardize data at source** *(better long-term solution)*
- **My pipeline would still handle both** *(standardized and non-standardized)* **for backwards compatibility**

---

### PHASE 7: DATA LABELING - Bounding Boxes (2 min)

**Trigger:** SageMaker Ground Truth, bounding boxes, avoid shine

**Challenge:**
*Images:* **Varying lighting, angles, shine from studio lights**

**Solution:**
- **SageMaker Ground Truth** *workflows*
- **Data labelers** *create boxes around lipstick (not packaging)*
- **Right pixels** *(avoids shine)*
- **Training data** *for ML models*

---

### PHASE 8: TESTING & EXPERIMENTS - Proving It Works (3-4 min)

**Trigger:** Averaging first, then 40→80 people experiments, 23%→93%, 4-way comparison

**Initial Testing (No ML Yet):**

*While data scientists trained models:*
- **Bounding box pixels → Average RGB → Initial estimate**
- **Proof of concept**
- **Generate data for experiments**

**Double-Blind Experiments:**

**Round 1:**
- **Bought actual lipsticks** *(L'Oréal, Maybelline, MAC)*
- **40 participants:** *different genders, ethnicities, skin tones*
- **9 lipsticks each**
- **Wore real lipsticks** *→ ground truth photos*

**Round 2 (After ML):**
- **80 participants** *from Japan, Mexico, France, US*
- *Even I wore lipstick* *(every gender)*

**4-Way Comparison:**
1. **Real** *(ground truth)*
2. **Third-party** *(baseline)*
3. **Our averaging**
4. **Our ML**

**Results:**
- **Averaging: 23% success**
- **First ML: 60-70% success**
- **Optimized ML: 93% success**

**Built Internal App:**
- **Automated scoring, aggregation**
- **Fed back to data scientists**

**Technical Artists Collaboration:**

*Weekly syncs with* **rendering team**:
- **"What RGB values look realistic on different skin tones?"**
- *Brought* **experimental data** *(not just specs)*
- *Aligned on* **precision vs realism**
- **Example:** *Added reflectance values for glossy lipsticks per their feedback*

**Inclusivity:**
*ML depends on data—data is usually* **non-inclusive**.
**We ensured:** *Every gender, face type, skin tone represented*

---

### PHASE 9: ML MODELS - Parallel Pipelines (2 min)

**Trigger:** Data scientists built, I architected, parallel (labelers+ML), 65%→92%

**Collaboration:**
- *They:* **Trained models** *(bounding box, color, finish, particles)*
- *I:* **Architected pipelines** *(flow, SageMaker integration, feedback loop)*

**Parallel Pipelines:**
- **Data labeling:** *New/edge cases → humans → training*
- **ML inference:** *Most products → SageMaker → automated*

**Continuous Learning:**
- *Realism scores → feedback → retraining*
- **Accuracy: 65% → 92%**

**Edge Case:** **Honeybee bug** *(yellow lipstick had honeybee in background → model detected it → fixed)*

---

### PHASE 10: CROSS-TEAM - 6 Teams Throughout (2 min)

**Trigger:** 6 teams - technical artists FIRST

*Throughout project, coordinated* **6 teams**:

**1. Technical Artists (Rendering) - CLOSEST:**
- **Weekly syncs**, **experimental data**, **added reflectance values**

**2. Designers (Customer UX):**
- **Before/after slider**, **balanced design vs constraints**

**3. Data Scientists:**
- *I:* **infrastructure, data, feedback** / *They:* **models** / **10K+ labeled images**

**4. Product Managers:**
- *Vague → concrete requirements* / **Multiple iterations**

**5. 3D Asset Team (External):**
- **API contracts**, **respected expertise**, **<5% error rate**

**6. Beauty Brand Bridge Teams:**
- **Worked on recommendations** *for future photo standards*

---

### PHASE 11: ROLLOUT - AB Testing & Expansion (3 min)

**Trigger:** AB test 60% increase, 15 countries phased

**AB Testing in US:**
- **50/50 split** *(in-house vs third-party)*
- **Web Labs monitoring**
- **60% increase** *in feature usage/rating*
- **Safety:** *Exponential backoff, quick rollback*

**Edge Case:**
- **Japan:** *Different product photos*
- *Stopped rollout, improved models*
- **Unified models** *for Japan + US*

**Marketplace Expansion:**

**Scoped US first** *(figure out kinks)* **→ Then scaled**

**Phased:**
1. **US**
2. **Japan**
3. **Europe** *(UK, Germany, France, Italy, Spain)*
4. **Asia** *(China, India, Singapore)*
5. **Latin America** *(Mexico, Brazil)*

**Total: 15 countries**

**Why Phased:**
- **Risk mitigation**, **localization**, **gradual scale** *(100K → millions products/day)*

---

### PHASE 12: IMPACT & LEARNING (3 min)

**Trigger:** 50% turnaround, 93% accuracy, foundation reuse, org standards

**Measured Impact:**

**1. Turnaround:** **2 days → 1 day (50%)**

**2. Cost Savings:**
- **Replaced third-party**
- **Projected significant savings** *(millions of products)*
- **Additional savings** *from foundation reuse*

**3. Quality:**
- **93% success** *(vs 23% averaging)*
- **92% ML accuracy** *(vs 65% initial)*
- **60% increase** *in usage/rating*

**4. Scale:**
- **Millions of products**, **15 countries**
- **40TB/day** *in data lake*
- **40M+ monthly customers**

**5. Extensibility:**
- *Expected* **only lipsticks**
- **Foundations** *reused entire pipeline* *(not rebuilt)*
- *Other team* **added features to existing pipeline**
- *Roadmap:* **eyeliners, eyeshadows, nail polish**

**Organizational Impact:**

**1. Recommendation Accepted for Next Year:**
- **Photo standards** *(to be implemented in next contract renewal)*
- **RGB catalog field** *(in roadmap for Q1 next year)*

**2. Pipeline Reusability:**
- **Other team used my pipeline** *for foundations*
- **Saved them 3-6 months** *of development time*

**Key Learning:**

**Don't just solve immediate technical problem—work backward to address root causes.**

*Could have built better algorithms. Instead:* **Identified root cause (bad photos)** **and recommended fix at source** *(even though couldn't implement immediately)*.

**Lasting impact** *(recommendations for future)* **vs one-time fix**.

---

## 🚀 PROJECT SCOTT (Only If Asked)

**Trigger:** Workshop 100% docs, prototype, projected 240 hrs

**Problem:** *Incomplete docs, new hires ask repeatedly, SMEs answer same questions*

**Workshop (100% TRUE):**
- **Led org-wide workshop**
- **Created SME reference table** *(topics → people)*
- **Assigned ownership, deadlines**
- **Result: 100% documentation completion**

**Prototype (TRUE):**
- **Project Scott** *- AI agent Slack bot*
- **RAG-based** *(Vector DB + LLM)*
- *Found answer → responds / Partial → contacts SME with* **specific details**
- **Ticketing integration, code analysis, autonomous agents**
- **LLM agnostic** *(new models every month)*

**Impact (PROJECTED):**
- **Projected 240+ dev-hours/month** *saved*
- **Near 100% docs** *(from workshop + suggestions)*

---

## 🙋 QUESTIONS FOR THEM

**1.** *"What does success look like to you for this role?"* **(To all three)**

**2.** *"If starting today, what learnings would you share? X, kick us off?"* **(If same answer)**

---

## ⚠️ FINAL REMINDERS

- **30 min for VTO** (let them guide)
- **Watch cues** (stop at "Great")
- **Technical artists FIRST** (Tyler's ask)
- **Phase 6: Recommendation for future** (not fully implemented - timing issue)
- **Be flexible** (follow their lead)
- **You did this** - 5 years, fully verifiable
- **40M+ users** - massive scale

---

## 🎯 YOU'VE GOT THIS!

**GOOD LUCK! 🎮🚀**

---

---

# 💡 DEEP-DIVE SECTIONS (If They Ask More)

---

## PHASE 1 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "Why was the third-party tool non-extensible?"**
*Their system was designed specifically for lipsticks. Different product types have different visual properties:*
- **Foundations:** *Need skin tone matching, coverage type (full/medium/light)*
- **Eyeliners:** *Need line thickness, smudge-proof properties*
- **Eyeshadows:** *Need pigmentation levels, blendability*
*The third-party tool wasn't designed to handle these different property types.*

**Q: "What was the business impact of the cost?"**
*At scale:*
- **Millions of beauty products** *in Amazon catalog*
- **Third-party charged per product** *processed*
- **Projected cost savings** *from in-house solution were significant*
- *Additional cost savings when* **expanding to foundations** *(reusing same pipeline)*

---

## PHASE 2 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "How does the full AR experience work?"**

*Full pipeline:*
1. **Face tracking** *(rendering team - applied scientists)*: *Identifies lips, tracks movement in real-time*
2. **3D lip model creation** *(3D asset team)*: *Uses my extracted properties to create 3D model*
3. **Real-time rendering** *(technical artists)*: *Applies 3D model to tracked lips with proper lighting, shadows*
4. **Before/after slider** *(Customer Experience team - designers)*: *Swipe to see with/without lipstick*

**Q: "What did you own end-to-end?"**
*I owned:*
- **Data ingestion** *(product catalog → filtering → images)*
- **Visual property extraction** *(bounding boxes, RGB, finish, particles)*
- **API handoff** *(send standardized properties to 3D team)*
- **Pipeline infrastructure** *(Lambda, SageMaker, Step Functions)*
- **Monitoring** *(CloudWatch, X-Ray)*

*I did NOT own:*
- **3D modeling** *(specialized team)*
- **AR rendering** *(technical artists, applied scientists)*
- **Front-end UX** *(Customer Experience team)*

---

## PHASE 3 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "What were the specific bottlenecks with ML Pigeon?"**
*ML Pigeon issues:*
- **Performance:** *Processing 10K products took 6+ hours (we needed sub-hour)*
- **Support:** *Customer support team response time was 2-3 days*
- **Control:** *Couldn't customize extraction algorithms for our needs*
- **Dependencies:** *Used internal tools scheduled for deprecation in Q3 2024*

**Q: "Why were costs too high with AWS native?"**
*AWS native approach:*
- **AWS Data Pipeline** *was the orchestration service we'd use*
- **Problem:** *Charged per pipeline execution + idle server time*
- **At our scale:** *Millions of products → thousands of pipeline executions → prohibitive costs*
- **Step Functions:** *Much cheaper at scale (pay per state transition, not per execution)*

**Q: "Why Step Functions specifically over other orchestrators?"**

**Alternatives considered:**

1. **Apache Airflow:**
   - *Pros:* **Mature, lots of integrations**
   - *Cons:* **Need to manage servers** *(EC2, monitoring, scaling)*, **heavyweight**, **team not familiar**

2. **AWS Glue:**
   - *Pros:* **AWS-native, good for data transformation**
   - *Cons:* **Focused on ETL**, **not general-purpose orchestration**, **less flexible for our multi-stage workflow**

3. **Custom Lambda chain:**
   - *Pros:* **Full control**
   - *Cons:* **Hard to maintain**, **no visual workflow**, **manual error handling**, **complex state management**

**Why Step Functions won:**
- **Visual workflow** *(non-engineers can see pipeline)*
- **Built-in features** *(retry with exponential backoff, error handling, parallel execution, wait states)*
- **AWS-native** *(no servers to manage)*
- **Can pause/resume** *(useful for long-running jobs)*
- **Cost-effective** *(pay per state transition: $0.025 per 1000 transitions)*

---

## PHASE 4 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "What feedback did you get from senior engineers?"**

**Feedback received:**

1. **From senior backend engineer:**
   - *"This design won't scale beyond small volume. Your Step Functions orchestration will timeout with large batches. Need to rethink data partitioning and parallel processing."*
   - **My response:** *Redesigned with parallel processing, optimized Lambda memory, implemented DynamoDB caching*

2. **From senior ML engineer:**
   - *"How will you handle model updates? Need versioning strategy."*
   - **My response:** *Added multi-variant SageMaker endpoints for A/B testing models*

3. **From infrastructure engineer:**
   - *"What's your observability strategy?"*
   - **My response:** *Added CloudWatch dashboards, X-Ray tracing, alarms on key metrics*

4. **From sister team senior engineer:**
   - *"How will this integrate with our front-end UX?"*
   - **My response:** *Defined API contract, async processing with status endpoints*

**Q: "How did you present to org-wide meeting?"**

*Presentation structure:*
1. **Problem statement** *(5 min)*: *Why replace third-party*
2. **Three design options** *(10 min)*: *Pros/cons of each*
3. **Recommendation** *(5 min)*: *Why Step Functions, with cost/benefit analysis*
4. **Q&A** *(10 min)*: *Addressed concerns*
5. **Timeline** *(5 min)*: *Phased approach - prototype → pilot → full rollout*

---

## PHASE 5 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "How did you optimize Lambda functions?"**

**Lambda optimization:**

1. **Memory tuning:**
   - *Started with* **128MB** *(too slow)*
   - *Tested:* **512MB, 1GB, 2GB**
   - **Found optimal: 1GB** *(sweet spot for cost/performance)*
   - *More memory =* **more CPU** *(faster execution)*

2. **Cold start reduction:**
   - **Provisioned Concurrency** *for critical paths (preprocessing)*
   - **Lazy loading:** *Load dependencies on first invocation, cache in global scope*
   - **Connection pooling:** *Reuse DynamoDB/S3 connections across invocations*
   - **Result:** *p95 cold start <100ms (down from ~500ms)*

3. **Timeout optimization:**
   - *Initially:* **3 minutes** *(sometimes timed out)*
   - *Analyzed:* **90% complete in 30 seconds**
   - *Set:* **2 minutes** *(buffer for edge cases)*
   - *For long-running:* **Offload to SageMaker batch transform** *(not Lambda)*

4. **Deployment package:**
   - **Minimized dependencies** *(only necessary libraries)*
   - **Used Lambda Layers** *for shared code*
   - **Result:** *Deployment package 50MB (down from 250MB)*

**Q: "How does Step Functions orchestration work?"**

**Step Functions workflow:**

1. **State 1: Validate Product**
   - *Lambda function validates product catalog entry*
   - *Checks: has images, valid product type, not already processed*

2. **State 2: Fetch Images (Parallel)**
   - *Parallel Lambda invocations fetch images from S3*
   - *Can process 10 images simultaneously*

3. **State 3: Route Decision**
   - *Choice state: send to data labelers OR ML model?*
   - *Decision based on: product type, image quality score, historical data*

4. **State 4a: SageMaker Ground Truth Job** *(if labelers)*
   - *Creates labeling job*
   - **Wait state:** *Waits for labelers to finish (can take hours)*

4. **State 4b: SageMaker Endpoint Invocation** *(if ML)*
   - *Invokes endpoint for inference*
   - *Typically completes in seconds*

5. **State 5: Post-Processing**
   - *Lambda function validates extracted properties*
   - *Formats for 3D team API*

6. **State 6: Store Results**
   - *Writes to DynamoDB (metadata)*
   - *Writes to S3 (visual properties JSON)*

7. **State 7: Trigger Downstream**
   - *SNS notification to 3D team that properties are ready*

**Error Handling:**
- **Retry** *with exponential backoff (3 attempts, 2s/4s/8s delays)*
- **Catch** *errors → send to Dead Letter Queue (SQS)*
- **Alarm** *on DLQ messages → oncall notification*

---

## PHASE 6 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "If you could have implemented this, what would the impact be?"**

**Projected impact:**

1. **Data quality:** *Standardized photos would eliminate 60-70% of edge cases*
2. **Model accuracy:** *ML models would likely reach 95%+ accuracy (vs 92% we achieved)*
3. **Processing speed:** *Fewer retries, less preprocessing needed*
4. **Cost:** *Less compute for handling variability*
5. **Extensibility:** *Easier to expand to foundations, eyeliners (same standard)*

**Q: "What did you do instead?"**

*Since I couldn't fix at source:*
1. **Built robust bounding box detection** *(handles various backgrounds)*
2. **Lighting normalization** *(algorithms to compensate for studio lights)*
3. **Quality scoring** *(route low-quality images to human labelers)*
4. **Experiments with real lipsticks** *(validate that our extraction works despite photo variability)*

*This approach worked, but would have been easier with standardized photos.*

---

## PHASE 7 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "How does SageMaker Ground Truth work?"**

**Workflow:**

1. **Created labeling job:**
   - *Uploaded images to S3*
   - *Defined task:* **"Draw bounding box around lipstick product (not packaging, not background)"**
   - *Provided examples* **("good" and "bad" labels)**

2. **Assigned to data labelers:**
   - **Amazon Mechanical Turk** *(public workforce)*
   - **Multiple labelers per image** *(3-5)* **for consensus**
   - **Quality control:** *If labelers disagree >20%, send to expert labeler*

3. **Received results:**
   - **Bounding box coordinates** *(x, y, width, height)*
   - **Confidence score** *(based on labeler agreement)*
   - **Stored in S3** *(JSON format)*

4. **Fed to ML training:**
   - **First 500 labeled images** *→ trained initial model*
   - **Model auto-labels next batch** *→ humans validate*
   - **Active learning loop:** *Model suggests, humans correct, retrain*

**Cost:**
- **$0.08 per image** *labeled (Mechanical Turk)*
- **10,000 images** *→ $800 for labeling*
- *Much cheaper than third-party tool*

**Q: "Why bounding boxes specifically?"**

*Without bounding boxes:*
- **Entire image** *includes packaging, background, studio lighting*
- **RGB average** *would be skewed by non-lipstick pixels*
- **Example:** *Silver packaging → adds gray tint to color extraction*

*With bounding boxes:*
- **Only lipstick pixels** *extracted*
- **More accurate RGB** *values*
- **Handles products with complex packaging**

---

## PHASE 8 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "How did you recruit 80 participants across multiple countries?"**

**Recruitment:**

1. **Internal Amazon employees:**
   - **Email to org** *(Beauty Tech, sister teams)*
   - **Free lipsticks as incentive** *(people loved this!)*
   - **Flexible participation** *(could do at home with phone camera)*

2. **Reached out to international teams:**
   - **Japan team:** *5 participants*
   - **Mexico team:** *3 participants*
   - **France team:** *2 participants*
   - **US team:** *70 participants*

3. **Ensured diversity:**
   - **Actively recruited** *underrepresented groups*
   - **Goal:** *Equal representation across skin tones*
   - **Achieved:** *Roughly equal distribution*

**Q: "How did the internal app work?"**

**App architecture:**

1. **Built on AWS:**
   - **S3 static website** *(HTML/JS/CSS)*
   - **API Gateway + Lambda** *(backend)*
   - **DynamoDB** *(store scores)*

2. **User workflow:**
   - **Login** *(Cognito - Amazon employees only)*
   - **Upload 4 screenshots:**
     - *Real lipstick photo*
     - *Third-party rendering*
     - *Our averaging rendering*
     - *Our ML rendering*
   - **Score each** *(1-10: how close to real?)*
   - **Submit** *(stored in DynamoDB)*

3. **Admin dashboard:**
   - **View aggregated scores** *(mean, median, std dev)*
   - **Filter by:** *Skin tone, lipstick color, participant demographics*
   - **Export to CSV** *(data scientists used this)*

4. **Took 2 weeks to build:**
   - **1 week:** *Backend (API, database)*
   - **1 week:** *Frontend (UI, image upload)*
   - **Reusable:** *Used same app for foundation experiments later*

**Q: "What did the experimental results tell you?"**

**Key insights:**

1. **Averaging approach:**
   - **Only 23% success** *(people preferred ours over third-party)*
   - **Problem:** *Didn't account for lighting, texture variations*
   - **Good for:** *Proof of concept, but not production*

2. **First ML models (60-70%):**
   - **Better than averaging**
   - **Problem:** *Struggled with certain skin tones (darker tones), certain colors (reds)*
   - **Action:** *Data scientists retrained with more diverse data*

3. **Optimized ML (93%):**
   - **Significantly better than third-party**
   - **Still struggled with:** *Very glossy lipsticks (reflectance hard to capture)*
   - **Action:** *Added reflectance values to extraction per technical artists' request*

4. **Demographic insights:**
   - **Asian skin tones:** *Our ML worked best (96% success)*
   - **Black skin tones:** *Took longer to optimize (started at 85%, got to 92%)*
   - **This informed:** *Need for equity in training data*

---

## PHASE 9 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "What models did the data scientists use?"**

**Models deployed:**

1. **Bounding Box Detection:**
   - **Architecture:** *Faster R-CNN (object detection)*
   - **Training:** *10,000 labeled images from Ground Truth*
   - **Accuracy:** *98% (IoU >0.9)*
   - **Inference time:** *~200ms per image*

2. **Color Extraction:**
   - **Architecture:** *Custom CNN (regression)*
   - **Input:** *Cropped image (from bounding box)*
   - **Output:** *RGB values (3 continuous values)*
   - **Training:** *Labeled data from experiments (ground truth colors)*
   - **Accuracy:** *Mean absolute error <5 RGB units*

3. **Finish Classification:**
   - **Architecture:** *ResNet-50 (classification)*
   - **Classes:** *Matte, Shiny, Satin, Glossy*
   - **Accuracy:** *89% (4-class)*

4. **Particle Detection:**
   - **Architecture:** *Custom CNN (binary + regression)*
   - **Output:** *Has particles (yes/no), particle size, density*
   - **Accuracy:** *Binary 95%, size/density MAE <10%*

**Q: "How did the continuous learning loop work?"**

**Feedback loop:**

1. **Experimental scores** *fed back to data scientists*
2. **Identified failure cases:**
   - *Which lipsticks had low scores?*
   - *Which demographics struggled?*
   - *What patterns in failures?*

3. **Retrained models:**
   - **Added more training data** *(focused on failure cases)*
   - **Adjusted model architecture** *(added layers, changed loss function)*
   - **Hyperparameter tuning** *(learning rate, batch size)*

4. **Redeployed to SageMaker:**
   - **Multi-variant endpoints** *(90% traffic to old model, 10% to new)*
   - **A/B tested** *(compare scores)*
   - **If better → full rollout** *(100% to new model)*

5. **Repeated every 2-3 weeks:**
   - **Cycle time:** *2 weeks data collection → 1 week retraining → 1 week testing*
   - **Result:** *Steady improvement from 65% to 92%*

---

## PHASE 10 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "Give specific examples of collaboration with each team"**

**1. Technical Artists - Detailed Example:**

*Issue that came up:*
- **Glossy lipsticks** *looked flat in AR*
- *They said:* **"We need reflectance values, not just color"**
- *I didn't know:* **What are reflectance values?**

*How we solved it:*
- **Scheduled deep-dive meeting** *(1 hour)*
- *They explained:* **Reflectance = how light bounces off surface** *(specular vs diffuse)*
- *I asked:* **"How do we extract this from product images?"**
- *They said:* **"Analyze pixel variance in high-lighting areas"**
- **I implemented** *new extraction algorithm*
- **They validated** *with rendering tests*
- **Result:** *Glossy lipsticks looked realistic*

**2. Designers - Detailed Example:**

*Issue:*
- **Designers wanted** *immediate visual feedback (< 1 second)*
- **My pipeline took** *5-10 seconds (extraction + 3D generation + rendering)*
- *Conflicting requirements*

*How we solved it:*
- **Prototyped two approaches:**
  - **Approach A:** *Cache pre-rendered lipsticks (limited colors)*
  - **Approach B:** *Async processing with progress indicator*
- **Showed prototypes** *to designers*
- **Approach A:** *They said "feels limiting"*
- **Approach B:** *They said "acceptable if progress bar is smooth"*
- **Implemented Approach B** *with WebSocket real-time updates*

**3. Data Scientists - Detailed Example:**

*Issue:*
- **Initial models only 65% accurate**
- *They said:* **"Need more training data"**
- *I had:* **Only 500 labeled images**

*How we scaled:*
- **I set up SageMaker Ground Truth at scale:**
  - *Increased labeling job size to 10,000 images*
  - *Recruited more labelers (Mechanical Turk)*
  - *Implemented quality control (consensus voting)*
- **They trained on larger dataset**
- **Accuracy jumped to 85%**
- **Continued iterating** *(eventually reached 92%)*

**4. Product Managers - Detailed Example:**

*Issue:*
- **Initial requirement:** *"Make AR try-on realistic"*
- *Too vague to implement*

*How we clarified:*
- **I asked:** *"What does 'realistic' mean technically?"*
- **Multiple iterations:**
  - **Iteration 1:** *I showed averaging approach → PM said "colors are off"*
  - **Iteration 2:** *I showed bounding boxes → PM said "better but still not right"*
  - **Iteration 3:** *I showed ML models → PM said "closer, but glossy doesn't look real"*
  - **Iteration 4:** *I added reflectance → PM said "now that's realistic!"*
- **Resulted in concrete requirements:**
  - **RGB values** *(±5 units accurate)*
  - **Finish type** *(89%+ accuracy)*
  - **Reflectance** *(for glossy/shiny)*
  - **Particle properties** *(for glitter)*

**5. 3D Asset Team - Detailed Example:**

*Issue:*
- **Coordinate system misunderstanding**
- *I sent:* **Bottom-left origin**
- *They expected:* **Top-left origin**
- **3D models were flipped**

*How we fixed it:*
- **Scheduled meeting** *(30 min)*
- **Documented assumptions:**
  - *Created API contract document*
  - *Specified coordinate system explicitly*
  - *Added validation:* **"If y-coordinate > image_height, throw error"**
- **Added unit tests** *(catch this early)*
- **Result:** *Error rate dropped from 15% to <5%*

**6. Beauty Brand Bridge Teams - Detailed Example:**

*Collaboration:*
- **I met with bridge team lead** *(manages L'Oréal, Maybelline accounts)*
- **Proposed photo standards** *for next year*
- *They said:* **"Makes sense, but brands won't change mid-year"**
- **We agreed:** *Propose during Q1 renewals next year*
- *They helped me:* **Understand brand submission process, pain points, what's realistic to ask**
- **My recommendation:** *Became part of next year's brand onboarding guidelines*

---

## PHASE 11 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "How did you monitor AB tests?"**

**Monitoring setup:**

1. **Web Labs** *(Amazon's internal A/B testing tool)*:
   - **Variant A:** *Third-party tool*
   - **Variant B:** *Our in-house tool*
   - **50/50 random assignment** *(per customer)*

2. **Metrics tracked:**
   - **Feature usage:** *% of customers who clicked "virtual try-on"*
   - **Feature rating:** *1-5 stars after using*
   - **Conversion:** *% who clicked "Add to Cart" after try-on*
   - **Load time:** *Time to first render*
   - **Error rate:** *% of failed renders*

3. **Dashboard:**
   - **Real-time CloudWatch dashboard**
   - **Comparison:** *Variant A vs B side-by-side*
   - **Statistical significance:** *Chi-square test, p<0.05*

4. **Results:**
   - **Feature usage:** *+60% (Variant B)*
   - **Rating:** *4.2 → 4.6 stars*
   - **Conversion:** *+15% (Variant B)*
   - **Load time:** *Slightly slower (8s vs 6s) but acceptable*
   - **Error rate:** *<1% (similar to Variant A)*

5. **Decision:**
   - **Statistically significant improvement**
   - **Approved for 100% rollout** *(week 3 of AB test)*

**Q: "What was different about Japan?"**

**Japan-specific issues:**

1. **Different packaging styles:**
   - **US/Europe:** *Cylindrical lipstick tubes*
   - **Japan:** *Square/rectangular tubes, different materials*
   - **Our bounding box model:** *Trained mostly on cylindrical → struggled with square*

2. **Different lighting in product photos:**
   - **US/Europe:** *Studio lighting (bright, even)*
   - **Japan:** *Natural lighting (softer, shadows)*
   - **Our color extraction:** *Calibrated for studio → off by ~10 RGB units for natural*

3. **Different beauty preferences:**
   - **US/Europe:** *Bold colors (reds, pinks)*
   - **Japan:** *Subtle colors (nudes, light pinks)*
   - **Our ML models:** *Trained more on bold → less accurate on subtle*

**How we fixed it:**

1. **Collected Japan-specific training data:**
   - **1,000 Japanese product images**
   - **Labeled with Ground Truth**

2. **Retrained models:**
   - **Combined US + Japan data** *(12,000 total images)*
   - **Unified model** *that works for both*

3. **Validated:**
   - **Ran experiments with Japanese employees** *(5 participants)*
   - **Scores improved from 75% to 90%** *(on par with US)*

4. **Rolled out unified model:**
   - **Deployed to US and Japan** *(same model)*
   - **Result:** *Works well for both markets*

**Q: "How did you handle the 15-country scale?"**

**Scaling challenges:**

1. **Load increased:**
   - **1 country (US):** *100K products/day*
   - **15 countries:** *1.2M products/day* *(12x increase)*

2. **How we scaled:**
   - **Lambda:** *Already auto-scales*
   - **SageMaker endpoints:** *Increased from 2 instances to 20* *(auto-scaling policy)*
   - **DynamoDB:** *Switched from provisioned to on-demand* *(handles spikes better)*
   - **Step Functions:** *No changes needed* *(scales automatically)*

3. **Cost management:**
   - **Spot instances** *for SageMaker training jobs* *(70% cost savings)*
   - **S3 Intelligent-Tiering** *(auto-move old images to cheaper storage)*
   - **Lambda memory optimization** *(reduced from 2GB to 1GB where possible)*

4. **Monitoring:**
   - **CloudWatch alarms per marketplace** *(alert if one marketplace has issues)*
   - **X-Ray tracing** *(identify bottlenecks)*
   - **On-call rotation** *(24/7 coverage for 15 countries across time zones)*

---

## PHASE 12 - IF THEY ASK MORE

#### 💡 IF THEY ASK MORE:

**Q: "How did other team reuse your pipeline for foundations?"**

**Foundation project:**

1. **Different extraction requirements:**
   - **Lipsticks:** *RGB, finish, particles*
   - **Foundations:** *RGB, coverage type (full/medium/light), undertone (warm/cool/neutral)*

2. **Modular design enabled reuse:**
   - **They kept:** *Data ingestion, bounding boxes, pipeline infrastructure*
   - **They swapped:** *ML models (trained new models for foundation-specific properties)*
   - **Same Step Functions workflow** *(just different Lambda functions for foundation logic)*

3. **Time savings:**
   - **If built from scratch:** *6 months (estimate)*
   - **Reusing my pipeline:** *2 months (actual)*
   - **Saved:** *4 months*

4. **My role:**
   - **Consulted with their team** *(2 meetings/week for first month)*
   - **Helped them understand architecture**
   - **Reviewed their changes** *(code review)*
   - **Didn't do the work** *(they implemented foundation-specific logic)*

**Q: "What would you do differently if starting over?"**

**Improvements:**

1. **Implement photo standards earlier:**
   - *If I'd proposed this in Q1 instead of Q3, might have gotten it implemented*
   - **Learning:** *Timing matters - align with contract renewal cycles*

2. **More aggressive model retraining:**
   - *Took 6 months to reach 92% accuracy*
   - *Could have parallelized experiments, reached 92% in 3-4 months*

3. **Better documentation:**
   - *When other team reused pipeline, they had lots of questions*
   - **Learning:** *Document architecture decisions, not just code*

4. **Earlier Japan testing:**
   - *Should have done smoke tests in Japan before full rollout*
   - *Would have caught packaging/lighting issues earlier*

5. **More stakeholder communication:**
   - *Sometimes PMs/designers felt out of loop*
   - **Learning:** *Weekly status updates to all stakeholders (not just when needed)*

