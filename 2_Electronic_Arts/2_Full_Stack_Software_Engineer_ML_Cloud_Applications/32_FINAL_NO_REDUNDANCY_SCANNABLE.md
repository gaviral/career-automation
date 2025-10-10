# FINAL INTERVIEW PREP - Clean & Scannable
**Interview:** Oct 9, 2025, 1PM PDT (1 hour)
**Interviewers:** Daniel (Hiring Mgr), Blaze (Director), Rhea (Tech Director)

---

## ⚠️ STRATEGY

**PRIMARY:** VTO (Visual Property Extraction) - 100% true, 30 min depth
**SECONDARY:** Project Scott (Workshop + Prototype) - Use only if asked

---

## 📋 VTO PROJECT - Phase-by-Phase

### PHASE 1: WHY - Problem Statement (2 min)

**Trigger:** Third-party expensive, non-extensible, control, 2 days→1 day

*We had a* **third-party tool** *creating* **3D lip models** *for* **AR virtual try-on**.

**Why Replace It:**

1. **Expensive** *at millions of products scale*
2. **Non-extensible** *(wanted foundations, eyeliners, eyeshadows)*
3. **Wanted control** *(quality, turnaround time)*
4. **Slow turnaround:** **2 days** *(goal: cut to 1 day = 50%)*

---

### PHASE 2: WHAT - Project Scope (2 min)

**Trigger:** AR lipstick UX, extract RGB/finish/particles, pipeline flow

**User Experience:**
*Amazon app → lipstick → "virtual try-on" → camera → face tracking → try lipsticks in real-time AR*

**What I Extracted:**
- **RGB color values** *(not "unicorn red")*
- **Finish type** *(matte, shiny, satin, glossy)*
- **Particle properties** *(glitter: size, density, color)*

**Pipeline Flow:**
*Product catalog → **My pipeline** → 3D team → **Rendering team (technical artists)** → Customer UX*

---

### PHASE 3: DESIGN - System Design (2-3 min)

**Trigger:** 3 options, Step Functions recommended

**Option 1: ML Pigeon (Internal Framework)**
- ❌ **Bottlenecks**, **bad reviews**, **tools deprecating**

**Option 2: AWS Native Services**
- ❌ **Data pipelines deprecating**, **costs too high**

**Option 3: Step Functions + Serverless** ✅ **RECOMMENDED**
- **Cost-effective** *(pay-per-use, no idle servers)*
- **Scalable** *(event-driven, parallel)*
- **Modular** *(plug-and-play: swap labelers → ML models)*
- **Future-proof** *(not deprecated)*

**Why Step Functions:**
- Jobs take **days** *(don't want servers idle)*
- **Visual workflow** *(easy debug)*
- **Built-in retry/error handling**
- **Native AWS integration** *(Lambda, SageMaker, DynamoDB)*

---

### PHASE 4: APPROVAL - Review Process (2 min)

**Trigger:** Internal review (4 engineers), iterated, org-wide, approved, team assigned

**Step 1: Internal Team**
- Tested design with **4 senior engineers** *(different teams/orgs)*
- **Incorporated feedback**
- **Iterated** *(minor modifications)*

**Step 2: Org-Wide Presentation**
- Led **organizational meeting** *(all technical stakeholders + PM)*
- Presented **3 options**, recommended **Step Functions**
- **Got approval**

**Team Assigned:**
**Me (lead) + 3 developers + 2 ML engineers = 6 total**

---

### PHASE 5: ARCHITECTURE - Implementation (2-3 min)

**Trigger:** Event-driven, Step Functions orchestrate, Lambda/SageMaker, DynamoDB/S3, CDK, CloudWatch

**Event-Driven Pipeline:**
- **Product catalog changes → SNS → Step Functions**
- **Step Functions** *orchestrate multi-stage*
- **Parallel processing** *where possible*

**Key Services:**
- **Lambda:** *Preprocessing, orchestration, validation*
- **SageMaker Ground Truth:** *Data labeling*
- **SageMaker Endpoints:** *ML inference*
- **DynamoDB:** *State tracking, metadata*
- **S3:** *Images, artifacts, model files*
- **API Gateway + Cognito:** *API layer*
- **CloudWatch + X-Ray:** *Monitoring, tracing*
- **AWS CDK (TypeScript) → CloudFormation**

**CI/CD: 4 Stages**
1. **Dev** *(auto on commit)*
2. **Gamma** *(merge, tests, approval)*
3. **Pre-Prod** *(canary 10%)*
4. **Prod** *(full rollout)*

**Modular Design:**
*Initially:* **Human labelers** → *Later:* **Swap in ML models** → *Same pipeline, different component*

---

### PHASE 6: DATA LABELING - Bounding Boxes (2 min)

**Trigger:** SageMaker Ground Truth, bounding boxes, avoid shine, exact pixels

**The Challenge:**
*Product images:* **Varying lighting, angles, shine from studio lights**

**Solution: Bounding Boxes**
- **SageMaker Ground Truth** *workflows*
- **Data labelers** *create boxes around lipstick (not packaging)*
- **Identifies right pixels** *(avoids shine/reflections)*
- **Creates training data** *for ML models*

---

### PHASE 7: INITIAL TESTING - Averaging (2 min)

**Trigger:** No ML yet, averaging pixels, proof of concept, parallel development

**Approach:**
*While data scientists trained models:*
- Take **bounding box pixels**
- **Average RGB values**
- **Initial color estimate**

**Purpose:**
- **Proof of concept** *(does this work?)*
- **Generate data** *for experiments*
- **Don't block** *on ML development*

---

### PHASE 8: EXPERIMENTS - Double-Blind Testing (3-4 min)

**Trigger:** 40→80 people, bought lipsticks, diverse demographics, 4-way, 23%→93%

**The Challenge:**
*How do we know extracted colors* **look realistic in AR on different skin tones**?

**Experiment Setup:**

**Round 1:**
- **Bought actual lipsticks** *(L'Oréal, Maybelline, Revlon, MAC)*
- **40 participants:**
  - **Different genders**
  - **Different ethnicities** *(Asian, Black, White, Hispanic)*
  - **Different skin tones**
- **9 lipsticks each**
- **Wore real lipsticks** *→ reference photos (ground truth)*

**Round 2 (After ML):**
- **80 participants** *(high adoption)*
- *From* **Japan, Mexico, France, US**
- *Even I wore lipstick* *(every gender represented)*
- *Everyone loved free lipsticks!*

**4-Way Comparison:**
1. **Real lipstick** *(ground truth)*
2. **Third-party tool** *(baseline)*
3. **Our averaging**
4. **Our ML model**

**Scoring:** *1-10 scale: how close to real?*

**Results:**
- **First (averaging):** **23% success rate**
- **Second (first ML):** **60-70% success rate**
- **Final (optimized):** **93% success rate**

**Built Internal App:**
- *Upload screenshots*
- **Automated scoring** *aggregation*
- **Fed back to data scientists** *for improvement*

**Collaboration with Technical Artists:**

*Weekly syncs with* **rendering team**:
- **Key question:** *"What RGB values look realistic on different skin tones?"*
- *Brought* **experimental data** *(not just specs)*
- *Aligned on* **technical precision vs artistic realism**
- **Example:** *For glossy lipstick, they needed* **reflectance values** *→ I added to pipeline*

**Inclusivity Principle:**

*ML models depend on data—data is usually* **non-inclusive**.

**We ensured:**
- **Equity and equality** *in training data*
- **Every gender, face type, skin tone** *represented*
- *Became* **foundational principle** *throughout*

---

### PHASE 9: ML MODELS - Parallel Pipelines (2-3 min)

**Trigger:** Data scientists built models, I architected pipelines, parallel (labelers+ML), 65%→92%

**Collaboration:**
*Worked with* **2 ML engineers** *(my team)* **+ data scientists**:
- *They:* **Trained models**
- *I:* **Architected pipelines** *(data flow, SageMaker integration, continuous learning)*

**Models Trained:**
1. **Bounding box detection** *(auto-find lipstick)*
2. **Color extraction** *(sophisticated - lighting, texture)*
3. **Finish classification** *(matte/shiny/satin/glossy)*
4. **Particle detection** *(glitter quantification)*

**Parallel Pipelines:**
- **Data labeling:** *New/edge cases → humans → training data*
- **ML inference:** *Most products → SageMaker → automated*

**Continuous Learning:**
- *Realism scores* → **feedback** *to data scientists*
- **Model retraining** *with new data*
- **Accuracy: 65% → 92%**

**Funny Edge Case:**
**Honeybee bug** *→ Yellow lipstick image had honeybee in background → model detected it as product → Fixed with better bounding boxes*

---

### PHASE 10: WORKING BACKWARD - Photo Standards (2-3 min)

**Trigger:** Contact beauty brands, standardize submissions, white circle, add RGB catalog field

**Out-of-the-Box Thinking:**

*Instead of just building better algorithms, I asked:* **"Why constrain ourselves to bad photos? Can we improve data at source?"**

**Actions Taken:**

**1. Contacted Beauty Brand Bridge Teams**
- *Teams interfacing with* **L'Oréal, Maybelline, Revlon, MAC**
- *Asked them to work with brands on* **photo standards**

**2. Standardized Photo Submission**
- **White background**
- **Natural lighting** *(not studio shine)*
- **Straight-on angle**
- **High resolution**
- **Circle format** *(lipstick centered)*

**3. Collaborated with Technical Artists**
- *Defined* **one standard way** *to photograph*
- *Ensured it worked for* **rendering requirements**

**4. Added RGB Field to Amazon Catalog**
- *Not just images*
- **Field for brands** *to input* **RGB values directly** *(color picker tools)*
- **Standardized naming** *(no more "unicorn red")*

**Impact:**
- **Higher quality data** *from day one (new partners)*
- **Standards adopted organization-wide**
- **Faster onboarding** *(don't fix photos after)*
- **Lasting organizational impact** *(not just technical fix)*

---

### PHASE 11: CROSS-TEAM - 6 Teams (3 min)

**Trigger:** 6 teams - technical artists FIRST

**1. Technical Artists (Rendering) - CLOSEST**
- **Weekly visual calibration syncs**
- *Brought* **experimental data** *to discussions*
- **Example:** *Added reflectance values for glossy lipsticks per their feedback*

**2. Designers (Customer Experience)**
- **Before/after slider UX**
- *Balanced* **design goals** *(immediate feedback)* **vs constraints** *(processing time)*
- **Solution:** *Async processing with progress indicators*

**3. Data Scientists / Applied Scientists**
- *I provided:* **Infrastructure, data, feedback**
- *They provided:* **Models**
- **10,000+ labeled images** *(scaled from 500)*

**4. Product Managers**
- *Vague requirements ("realistic") →* **Concrete** *(RGB, finish, particles, reflectance)*
- **Multiple iterations** *with prototypes*

**5. 3D Asset Team (External)**
- **Defined API contracts**
- **Respected expertise** *(guided, didn't micromanage)*
- **<5% error rate** *on handoffs*

**6. Beauty Brand Bridge Teams**
- **Standardized photo submissions**
- **Org-wide standards** *for future partners*

---

### PHASE 12: AB TESTING & ROLLOUT (2-3 min)

**Trigger:** AB testing, 60% usage increase, exponential backoff, Web Labs

**AB Testing in US:**

**Setup:**
- **50/50 traffic split** *(in-house vs third-party)*
- **Monitored** *with Web Labs (Amazon's testing tool)*
- **Collaborated with web engineers** *to track metrics*

**Results:**
- **60% increase** *in virtual try-on* **feature usage and rating**

**Safety Mechanisms:**
- **Exponential backoff** *to A version (third-party) on issues*
- **Quick rollback** *if problems*
- **Don't lose customer trust**

**Edge Cases:**
- **Japan:** *Different product photos (packaging styles)*
- *Initially saw issues in smoke testing*
- **Stopped rollout**, *improved models*
- **Created unified models** *for Japan + US*
- **Modular design** *made adaptation easy*

---

### PHASE 13: MARKETPLACE EXPANSION (2 min)

**Trigger:** US→15 countries, phased (Japan/Europe/Asia/Mexico), scoped US first

**Strategy:**
**Scoped to US first** *(figure out kinks)* → **Then scale**

**Phased Rollout:**
1. **US** *(largest, easiest monitoring)*
2. **Japan** *(different products, skin tones)*
3. **Europe** *(UK, Germany, France, Italy, Spain)*
4. **Asia** *(China, India, Singapore)*
5. **Latin America** *(Mexico, Brazil)*
**Total: 15 countries**

**Why Phased:**
- **Risk mitigation** *(issues contained)*
- **Localization** *(different catalogs)*
- **A/B testing** *per marketplace*
- **Gradual scale** *(100K → millions products/day)*

**Learning:**
*Different markets behave differently (not just* **volume**, *but* **different kinds** *of products)*

---

### PHASE 14: IMPACT & LEARNING (3 min)

**Trigger:** 50% turnaround, 93% accuracy, foundation reuse, org standards, work backward

**Measured Impact:**

**1. Turnaround Time:**
**2 days → 1 day (50% improvement)**

**2. Cost Savings:**
- **Replaced third-party tool**
- **Projected significant savings** *at millions of products*
- **Additional projected savings** *from foundation reuse*

**3. Quality:**
- **93% success rate** *(vs 23% averaging, vs third-party baseline)*
- **92% ML accuracy** *(up from 65%)*
- **60% increase** *in feature usage/rating*

**4. Scale:**
- **Millions of products** *across* **15 countries**
- **40TB/day** *in larger Beauty Tech data lake*
- **40M+ monthly customers**

**5. Extensibility - Foundation Reused:**
- *Initially expected* **only lipsticks**
- *After success:* **Foundations** *expanded*
- **Entire pipeline reused** *(not rebuilt)*
- *Other team* **implemented features into existing pipeline**
- *Roadmap:* **Eyeliners, eyeshadows, nail polish**

**Organizational Impact:**

**1. Standards Adopted Org-Wide:**
- **Photo submission** *(background, lighting, angle)*
- **Naming conventions** *(no more "unicorn red")*
- **RGB value standards**
- *Applied to* **all future beauty brand partnerships**

**2. Standardized Onboarding:**
- **New brands follow guidelines** *from day one*
- **Faster onboarding**
- **Higher quality data** *immediately*

**Key Learning:**

**Don't just solve immediate technical problem—work backward to address root causes.**

*Could have built increasingly sophisticated algorithms for bad photos. Instead, worked with* **beauty brand bridge teams** *to* **improve data at source**.

*Created* **lasting organizational impact** *(standards for future)* **vs one-time technical fix**.

*Took into all future projects:* **"What's root cause? How fix upstream?"**

---

## 🚀 PROJECT SCOTT (Only If Asked)

**Trigger:** Workshop 100% docs, prototype AI, projected 240 hrs, LLM agnostic

### The Problem:
**Documentation incomplete**, **new hires spend time asking**, **SMEs answer same questions repeatedly**

### The Workshop (100% TRUE):

*Led* **org-wide documentation workshop**:
- **Assigned SMEs** *to topics*
- **Created SME reference table** *(topic → people)*
- **Assigned ownership** *(everyone responsible)*
- **Review deadlines**
- **Result: 100% documentation completion**

### The Prototype (TRUE):

**Project Scott** *- AI agent prototype:*

**What It Did:**
- **Slack bot** *for questions*
- **RAG-based:** *Vector DB + LLM*
- *If* **found answer** *→ responds*
- *If* **partial/no match** *→ contacts SME with* **specific details** *(not entire question)*
- **SME responds** *→ fills docs →* **answers you**

**Additional:**
- **Ticketing integration** *(suggests docs for tickets)*
- **Code analysis** *(suggests doc updates on code push)*
- **Autonomous agents** *(self-asks to find gaps)*
- **All suggestions** *(human approval, not autonomous changes)*

**Architecture:**
- **LLM agnostic** *(new models every month)*
- **SageMaker, Lambda + API Gateway, DynamoDB**
- **Internal APIs:** *Code, docs, Slack, ticketing*

**Impact (PROJECTED):**
- **Projected 240+ dev-hours/month** *saved*
- **Near 100% doc completion** *(from workshop + suggestions)*

---

## 🔧 TECHNICAL DEEP-DIVE PREP

### Why Step Functions?

**Q: "Why Step Functions over alternatives?"**

**Decision Factors:**
1. **Jobs run days** *(don't want idle EC2)*
2. **Visual workflow** *(easy debug)*
3. **Built-in** *retry, error handling, parallel, wait states*
4. **Native AWS integration** *(Lambda, SageMaker, DynamoDB)*
5. **Automatic state management**

**Alternatives:**
- **Airflow:** *Too heavyweight, manage servers*
- **Glue:** *Data transformation focus, not orchestration*
- **Custom Lambda chain:** *Hard to maintain, no visual*

---

### Lambda Optimization

**Q: "How optimize Lambda?"**

**Approach:**
1. **Profiling** *(CloudWatch Logs Insights)*
2. **Memory tuning:** *128MB → 1GB (optimal for cost/performance)*
3. **Cold start:** *Provisioned Concurrency, lazy loading, connection pooling*
4. **Timeout:** *2 minutes (most complete in 30s, buffer for edges)*
5. **Long-running:** *Offload to SageMaker (not Lambda)*

---

## 🙋 QUESTIONS TO ASK

**1. To All Three:**
*"What does success look like to you for this role?"*

**2. If Same Answer (Change Order):**
*"If you were starting out today in this role, what learnings would you share? X, want to kick us off?"*

**Backup:**
- **Daniel:** *"Madden NFL - most interesting technical challenge?"*
- **Blaze:** *"How coordinate across EA's global studios?"*
- **Rhea:** *"What AWS technologies is team most excited about?"*

---

## ⚠️ FINAL REMINDERS

**From Mehul:**
- **Don't hyperoptimize** - you've done enough
- **Take a break**
- **Read 20 min before**
- **Don't over-practice** - diminishing returns

**Key Points:**
- **BE CONCISE** - watch cues, stop at "Great"
- **Technical artists FIRST** (Tyler's request)
- **40M+ users** - massive scale
- **You know this** - 5 years, you did it

---

## 🎯 YOU'VE GOT THIS!

**The work is done. Now:**
1. **Take break** (clear head)
2. **Eat** (brain fuel)
3. **Read 20 min before** (refresh)
4. **Walk in confident** (you know your stuff)

**These are YOUR accomplishments. Tell YOUR story.**

**GOOD LUCK! 🎮🚀**

