# FINAL PREP - Chronologically Optimized
**Interview:** Oct 9, 2025, 1PM PDT
**Time:** 1 hour total, ~30 min for VTO project

---

## 📋 VTO PROJECT - 12 Phases (Chronological)

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

### PHASE 6: WORKING BACKWARD - Fix Root Cause (2-3 min)

**Trigger:** Contact beauty brands, standardize photos, white circle, add RGB field

**Out-of-the-Box Thinking:**

*Instead of just better algorithms, I asked:* **"Can we improve data at source?"**

**Actions:**

**1. Contacted Beauty Brand Bridge Teams**
- *Teams with* **L'Oréal, Maybelline, Revlon, MAC**
- *Work with brands on* **photo standards**

**2. Standardized Photo Submission:**
- **White background, natural lighting, straight angle, high res, circle format**

**3. Collaborated with Technical Artists:**
- *Defined* **one standard way** *to photograph*
- *Works for* **rendering requirements**

**4. Added RGB Field to Amazon Catalog:**
- **Brands input RGB directly** *(color picker)*
- **Standardized naming** *(no more "unicorn red")*

**Impact:**
- **Higher quality data** *from day one*
- **Standards adopted org-wide**
- **Lasting impact** *(not just technical fix)*

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
- **Standardized photo submissions**, **org-wide standards**

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

**1. Standards Org-Wide:**
- **Photo submission, naming, RGB** *standards*
- *Applied to* **all future beauty brand partnerships**

**2. Standardized Onboarding:**
- **New brands follow guidelines** *from day one*
- **Faster, higher quality**

**Key Learning:**

**Don't just solve immediate technical problem—work backward to address root causes.**

*Could have built better algorithms. Instead:* **Improved data at source** *(beauty brand photos)*.

**Lasting organizational impact** *(standards for future)* **vs one-time fix**.

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

## 🔧 TECHNICAL DEEP-DIVE

### Why Step Functions?
1. **Jobs run days** *(no idle servers)*
2. **Visual workflow**
3. **Built-in** *retry, error handling, parallel*
4. **Native AWS integration**
5. **Automatic state management**

### Lambda Optimization:
1. **Memory: 128MB → 1GB** *(optimal)*
2. **Cold start:** *Provisioned Concurrency, lazy loading*
3. **Timeout: 2 min** *(most complete in 30s)*

---

## 🙋 QUESTIONS FOR THEM

**1.** *"What does success look like to you for this role?"* **(To all three)**

**2.** *"If starting today, what learnings would you share? X, kick us off?"* **(If same answer, change order)**

---

## ⚠️ FINAL REMINDERS

**Strategy:**
- **30 min for VTO** (let them guide with questions)
- **Watch cues** (stop at "Great")
- **Technical artists FIRST** (Tyler's ask)
- **Be flexible** (follow their lead)

**Confidence:**
- **40M+ users** - massive scale
- **You did this** - 5 years, fully verifiable
- **Unique differentiators** - technical artists, game dev
- **This is a conversation** - not interrogation

---

## 🎯 YOU'VE GOT THIS!

**Take break → Read 20 min before → Walk in confident**

**GOOD LUCK! 🎮🚀**

