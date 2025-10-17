# FINAL INTERVIEW PREP - All Feedback Incorporated
**Interview:** Oct 9, 2025, 1PM PDT (1 hour)
**Interviewers:** Daniel (Hiring Mgr), Blaze (Director), Rhea (Tech Director)

---

## ⚠️ CRITICAL STRATEGY

**PRIMARY PROJECT:** VTO (Visual Property Extraction for AR Try-On)
- 100% true, fully verifiable
- Shows technical artists collaboration (Tyler's #1 request)
- 30 minutes of depth available

**SECONDARY PROJECT:** Project Scott (Documentation Workshop + AI Prototype)
- Workshop 100% true
- Prototype true
- Metrics were "projected"
- Use ONLY if asked

---

## 📋 VTO PROJECT - Complete Walkthrough

### PHASE 1: WHY (2 min)

**Trigger:** Third-party expensive, non-extensible, control, 2 days→1 day

*We had a* **third-party tool** *creating* **3D lip models** *for* **AR virtual try-on**. *We needed to replace it because:*

1. **Expensive** at scale
2. **Non-extensible** *(wanted to expand to foundations, eyeliners, eyeshadows)*
3. **Wanted control** *(extraction quality, turnaround time)*
4. **Reduce turnaround:** **2 days → 1 day (50%+)**
5. **Cost reduction** *(in-house cheaper at millions of products)*

---

### PHASE 2: WHAT (2 min)

**Trigger:** AR lipstick UX, extract RGB/finish/particles, pipeline flow

**User Experience:**
*Amazon app → lipstick product → "virtual try-on" → camera opens → face tracking → try different lipsticks in real-time AR*

**My Part:**
*Extract from product images:*
- **RGB color values** *(not "unicorn red")*
- **Finish type** *(matte, shiny, satin, glossy)*
- **Particle properties** *(glitter size, density, color)*

**Pipeline:** *Product catalog → My pipeline → 3D asset team → Rendering team (technical artists) → Customer Experience*

---

### PHASE 3: DESIGN (2-3 min)

**Trigger:** 3 options, ML Pigeon bad, AWS native deprecation, Step Functions recommended

**3 Design Options:**

**Option 1: ML Pigeon (Internal Framework)**
- ❌ Bottlenecks, bad reviews, tools on path to deprecation

**Option 2: AWS Native Services**
- ❌ Data pipelines deprecating, costs too high

**Option 3: Step Functions + Serverless (RECOMMENDED)**
- ✅ Cost-effective (pay-per-use)
- ✅ Scalable (event-driven, parallel)
- ✅ Modular (plug-and-play components)
- ✅ Future-proof

**Why Step Functions:**
- *Jobs could take* **days** *(don't want servers idle)*
- **Event-driven** *(SNS/SQS triggers)*
- **Parallel processing** *(multiple stages at once)*
- **Built-in retry logic**
- **Modular:** *Swap data labelers → ML models easily*

---

### PHASE 4: APPROVAL (2 min)

**Trigger:** Tested internally (4 senior engineers), incorporated feedback, iterated, org-wide, approved, assigned team

**Process:**

**Step 1: Internal Review**
- *Tested design internally with my team*
- *Presented to* **4 senior engineers** *from different teams/organizations*
- **Incorporated their feedback**
- **Iterated on design** *(minor modifications)*

**Step 2: Org-Wide Presentation**
- *Led* **organizational-wide meeting** *with all technical stakeholders + PM*
- *Presented all 3 options, recommended Step Functions*
- **Got approval** *to move forward*

**Team Assigned:**
- **Me (technical lead) + 3 developers + 2 ML engineers = 6 total**

---

### PHASE 5: ARCHITECTURE (2-3 min)

**Trigger:** Event-driven, Step Functions orchestrate, Lambda/SageMaker, DynamoDB/S3, CDK 4-stage, CloudWatch/X-Ray

**Event-Driven Pipeline:**
- **Product catalog changes → SNS → Step Functions**
- **Step Functions orchestrate** multi-stage pipeline
- **Each stage:** Lambda or SageMaker job
- **Parallel processing** where possible

**Services:**
- **Lambda:** Preprocessing, orchestration, validation
- **SageMaker Ground Truth:** Data labeling
- **SageMaker Endpoints:** ML inference
- **DynamoDB:** Pipeline state, metadata
- **S3:** Images, artifacts, model files
- **API Gateway + Cognito:** API layer
- **CloudWatch + X-Ray:** Monitoring, tracing
- **AWS CDK (TypeScript) → CloudFormation**

**CI/CD: 4 Stages**
1. **Dev** (auto on commit)
2. **Gamma** (merge to main, tests, manual approval)
3. **Pre-Prod** (canary 10%)
4. **Prod** (full rollout)

**Why Modular:**
- *Initially:* **Data labelers** *(humans)*
- *Later:* **Swap in ML models** *(automated)*
- *Same pipeline, different component*
- *Quick iteration, experimentation*

---

### PHASE 6: DATA LABELING (2 min)

**Trigger:** SageMaker Ground Truth, bounding boxes, avoid shine, exact pixels

*Product images had* **varying lighting, angles, shine from studio lights**.

**Solution: Bounding Boxes**
- **SageMaker Ground Truth** *workflows*
- **Data labelers** *create bounding boxes around lipstick (not packaging)*
- *Identifies* **right pixels** *to extract from*
- **Avoids shine/reflection artifacts**
- *Creates* **training data** *for ML models*

---

### PHASE 7: INITIAL TESTING (2 min)

**Trigger:** No ML yet, averaging pixels, proof of concept, parallel to ML

*While data scientists trained models, we started with* **simple averaging**:
- *Take* **bounding box pixels**
- **Average RGB values**
- *Initial color estimate*
- **Proof of concept** *(does this work?)*
- **Generate data** *for experiments*
- *Don't block on ML*

---

### PHASE 8: EXPERIMENTS - Double-Blind Testing (3-4 min)

**Trigger:** 40→80 people, bought real lipsticks, diverse demographics, 4-way comparison, 23%→93%, internal app

**The Challenge:** *How do we know extracted colors* **look realistic in AR on different skin tones**?

**Experiment Setup:**

**Round 1:**
- **Bought actual lipsticks** *(L'Oréal, Maybelline, Revlon, MAC)*
- **40 participants:**
  - *Different genders*
  - *Different ethnicities*
  - *Different skin tones (Asian, Black, White, Hispanic, etc.)*
- **Wore real lipsticks** *→ reference photos (ground truth)*
- **9 lipsticks each** *of different colors*

**Round 2 (After ML Models):**
- **80 participants** *(higher adoption)*
- *People from* **Japan, Mexico, France, US**
- *Everyone loved free lipsticks!*
- *Even I wore lipstick for experiments* *(ensuring every gender represented)*

**4-Way Comparison:**
1. **Real lipstick photo** (ground truth)
2. **Third-party tool** rendering (baseline)
3. **Our averaging** rendering
4. **Our ML model** rendering

**Scoring:** 1-10 scale, *how close to real?*

**Results:**
- **First experiment (averaging):** **23% success rate** *(23% preferred ours over third-party)*
- **Second experiment (first ML models):** **60-70% success rate**
- **Continued iteration:** Eventually **93% success rate**

**Built Internal App:**
- *People upload screenshots*
- **Submit to realism platform**
- **Automated scoring aggregation**
- **Fed back to data scientists** *for model improvement*

**Collaboration with Technical Artists:**

*This is where I worked closest with* **technical artists on rendering team**:
- **Weekly syncs on visual calibration**
- *Key question:* **"What RGB values look realistic on different skin tones in AR?"**
- *I brought* **experimental data** *(not just specs)*
- *Aligned on* **technical precision vs artistic realism**
- **Example:** *For glossy lipstick, they needed* **reflectance values** *→ I added to pipeline*

**Inclusivity Focus:**

*Machine learning models depend on data—data is usually* **non-inclusive** *(lots for majority, little for minority)*.

*We made sure:*
- **Equity and equality** *in training data*
- *People from* **every gender, face type, skin tone**
- **Diverse demographics** *well-represented*
- *This became* **foundational principle** *throughout project*

---

### PHASE 9: ML MODELS - Parallel Pipelines (2-3 min)

**Trigger:** Data scientists built models, I architected pipelines, parallel (labelers + ML), continuous learning, 65%→92% accuracy

**Collaboration with Data Scientists:**

*I worked with* **2 ML engineers** *on my team +* **data scientists/applied scientists**:
- *They* **trained models** *(bounding boxes, color extraction, finish classification, particle detection)*
- *I* **architected pipelines** *(data flow, SageMaker integration, continuous learning loop)*

**Models Trained:**
1. **Bounding box detection** (auto-find lipstick in image)
2. **Color extraction** (sophisticated - accounts for lighting, texture)
3. **Finish type** (matte/shiny/satin/glossy classifier)
4. **Particle detection** (glitter quantification)

**Parallel Pipelines:**
- **Data labeling:** *New/edge-case products → human labelers → training data*
- **ML inference:** *Most products → SageMaker endpoints → automated*

**Continuous Learning:**
- *Realism test scores* → **feedback to data scientists**
- **Model retraining** *with new data*
- **Accuracy: 65% → 92%** *over iterations*

**Funny Edge Case:**
- **Honeybee detection bug:** *Yellow lipstick image had a honeybee in background → model detected it as product*
- *Fixed with better bounding boxes + training data*

---

### PHASE 10: WORKING BACKWARD - Photo Submission Standards (2-3 min)

**Trigger:** Contact beauty brands, standardize submissions, white background circle, add RGB field to catalog

**Out-of-the-Box Thinking:**

*Instead of just building better extraction algorithms, I asked:* **"Why constrain ourselves to bad photos? Can we improve data at source?"**

**Solution:**

**Step 1: Contacted Beauty Brand Bridge Teams**
- *Teams interfacing with* **L'Oréal, Maybelline, Revlon, MAC**
- *Asked them to work with brands on* **photo submission standards**

**Step 2: Standardized Photo Submission**
- **White background**
- **Natural lighting** *(not studio lights with shine)*
- **Straight-on angle** *(not 45°)*
- **High resolution**
- **Circle format** *(lipstick in center)*

**Step 3: Worked with Technical Artists**
- *Collaborated to define* **one standard way** *to photograph products*
- *Ensured it worked for* **rendering requirements**

**Step 4: Added RGB Field to Amazon Catalog**
- *Not just relying on images*
- **Added field** *for brands to input* **RGB values directly** *(using color picker tools)*
- **Standardized naming** *(no more "unicorn red")*

**Impact:**
- **Higher quality data from day one** *(new brand partners)*
- **Standards adopted organization-wide**
- **Faster onboarding** *(don't fix photos after submission)*
- *This approach created* **lasting organizational impact** *(not just technical fix)*

---

### PHASE 11: CROSS-TEAM (3 min)

**Trigger:** 6 teams - technical artists FIRST, all others

*Coordinated across* **6 teams**:

**1. Technical Artists (Rendering) - CLOSEST:**
- **Weekly visual calibration syncs**
- *Data-driven discussions with* **experimental results**
- **Example:** *Added reflectance values for glossy lipsticks based on their feedback*

**2. Designers (Customer Experience):**
- **Before/after slider UX**
- *Balanced* **design goals** *(immediate feedback)* **vs technical constraints** *(processing time)*
- **Solution:** *Asynchronous processing with progress indicators*

**3. Data Scientists / Applied Scientists:**
- *I provided:* **Infrastructure** *(SageMaker)*, **data** *(labeled)*, **feedback** *(scores)*
- *They provided:* **Models** *(architecture, training)*
- **10,000+ labeled images** *(scaled from 500)*

**4. Product Managers:**
- *Vague requirements ("realistic") →* **Concrete** *(RGB, finish, particles, reflectance)*
- **Multiple iterations** *with prototypes*

**5. 3D Asset Team (External):**
- **Defined API contracts** *(data format handoffs)*
- **Respected their expertise** *(guided direction, didn't micromanage)*
- **<5% error rate** *on handoffs*

**6. Beauty Brand Bridge Teams:**
- **Standardized photo submissions** *(working backward)*
- **Org-wide standards** *adopted for future partners*

---

### PHASE 12: AB TESTING & ROLLOUT (2-3 min)

**Trigger:** AB testing, 60% usage increase, exponential backoff, web labs monitoring

**AB Testing in US:**

**Phase 1:**
- **50/50 traffic split** *(our in-house vs third-party)*
- **Monitored closely** *with Web Labs (Amazon's testing tool)*
- **Collaborated with web engineers** *to track metrics*

**Results:**
- **60% increase** *in virtual try-on* **feature usage and rating**
- *Customers preferred our rendering*

**Safety Mechanisms:**
- **Exponential backoff** *to A version (third-party) on any issues*
- **Don't lose customer trust**
- **Quick rollback** *if problems detected*

**Interesting Edge Cases:**
- **Japan had different product photos** *(different packaging styles)*
- *Initially saw issues in smoke testing*
- **Stopped rollout**, *improved models*
- **Created unified models** *for Japan + US*
- **Modular design made this easy** *(quick adaptation)*

---

### PHASE 13: MARKETPLACE EXPANSION (2 min)

**Trigger:** US→15 countries, phased (Japan/Europe/Asia/Mexico), A/B per marketplace, scoped US first then scale

**Phased Rollout:**

**We scoped project to US first:**
- **Figure out all kinks**
- **Validate at scale**
- *Then* **scale to other countries**

**Expansion:**
1. **US** (largest, easiest monitoring)
2. **Japan** (different products, skin tones)
3. **Europe** (UK, Germany, France, Italy, Spain)
4. **Asia** (China, India, Singapore)
5. **Latin America** (Mexico, Brazil)
- **Total: 15 countries**

**Why Phased:**
- **Risk mitigation** *(issues contained to one marketplace)*
- **Localization** *(different catalogs)*
- **A/B testing per marketplace**
- **Scale gradually** *(100K → millions products/day)*

**Learning:**
- **Different markets behave differently** *(not just volume, but* **different kinds** *of products)*
- **Forecasting this was important** *(thought about it from design)*
- **Modular architecture helped** *(adapted quickly to Japan edge cases)*

---

### PHASE 14: IMPACT & LEARNING (3 min)

**Trigger:** 50% turnaround, 93% accuracy, cost savings (projected), foundation reuse, org standards, work backward

**Measured Impact:**

**1. Turnaround Time:**
- **2 days → 1 day (50% improvement)**

**2. Cost Savings:**
- **Replaced third-party tool**
- **Projected savings:** *(need to calculate - significant at millions of products)*
- *Additional projected savings when* **foundation** *reused pipeline*

**3. Quality:**
- **93% success rate** *(vs 23% with averaging, vs third-party baseline)*
- **92% ML model accuracy** *(up from 65% initial)*
- **60% increase in feature usage/rating**

**4. Scalability:**
- **Millions of products** *across* **15 countries**
- **40TB/day** *in larger Beauty Tech data lake*
- **40M+ monthly customers**

**5. Extensibility - Foundation Reused Pipeline:**
- *Initially expected this would* **only work for lipsticks**
- *After success, expanded to* **foundations**
- **Entire pipeline reused** *(not rebuilt)*
- *Other team* **implemented their features into existing pipeline**
- **Additional projected savings** *from foundation reuse*
- *Roadmap:* **Eyeliners, eyeshadows, nail polish**

**Organizational Impact:**

**1. Standards Adopted Org-Wide:**
- **Photo submission** *(white background, lighting, angle)*
- **Naming conventions** *(no more "unicorn red")*
- **RGB value standards**
- *Applied to* **all future beauty brand partnerships**

**2. Standardized Onboarding:**
- **New brands follow guidelines from day one**
- **Faster onboarding**
- **Higher quality data immediately**

**Key Learning:**

**Don't just solve immediate technical problem—work backward to address root causes.**

*I could have built increasingly sophisticated extraction algorithms for bad photos. Instead, I worked with* **beauty brand bridge teams** *to* **improve data at source**.

*This created* **lasting organizational impact** *(standards for future)* **vs one-time technical fix**.

*Took this into all future projects:* **"What's the root cause? How do we fix it upstream?"**

---

## 🚀 PROJECT SCOTT (Only If Asked)

**Trigger:** Workshop 100% docs, prototype AI agent, projected 240 hrs, LLM agnostic

### Tightened Opening (No Repetition):

*We had a recurring issue:* **Documentation was incomplete**, **new hires spent too much time asking questions**, *and* **subject matter experts answered the same questions repeatedly**.

*I took it upon myself to improve* **operational excellence** *for our team.*

### The Workshop (100% TRUE):

*Led* **organization-wide documentation workshop**:
- **Assigned subject matter experts** *to topics (CI/CD, front-end, back-end, etc.)*
- **Created SME reference table** *(topic → go-to people)*
- **Assigned ownership** *(everyone responsible for their docs)*
- **Review deadlines**
- **Result: 100% documentation completion**

### The Prototype (TRUE):

*Then I built* **Project Scott**, *an AI agent prototype:*

**What It Did:**
- **Slack bot** *you could ask questions*
- **RAG-based:** *Vector database + LLM (retrieval augmented generation)*
- *If* **found answer** *in docs → responds immediately*
- *If* **partial/no match** *→ contacts SME from reference table with* **specific missing details** *(not entire question)*
- **SME responds** *→ fills documentation →* **answers you**

**Additional Features:**
- **Ticketing system integration** *(suggests relevant docs for tickets)*
- **Code analysis** *(when code pushed, suggests documentation updates)*
- **Autonomous agents** *(self-asks questions to find doc gaps)*
- **All suggestions** *(not autonomous changes - human approval)*

**Architecture:**
- **LLM agnostic** *(didn't train our own - new models every month)*
- **SageMaker** *for model hosting*
- **Lambda + API Gateway**
- **DynamoDB** *for state*
- **Used internal APIs:** *Code platform, docs platform, Slack, ticketing*

**Impact (PROJECTED):**
- *When we did* **quick napkin calculations** *and* **projected** *impact:*
- **240+ dev-hours/month** *could be saved*
- **Near 100% doc completion** *(from workshop + suggestions)*

**Why Prototype:**
- **Proof of concept**
- **Validated approach** *before full deployment*
- **Got organizational buy-in**

---

## 🔧 TECHNICAL DEEP-DIVE PREP

### Why Step Functions Over Alternatives?

**Q: "Why did you choose Step Functions for orchestration?"**

**Decision Factors:**

1. **Jobs could run for days:**
   - *Don't want* **EC2 instances idle** *waiting*
   - **Serverless** *= pay only when running*

2. **Visual workflow:**
   - **Easy to debug** *(see which stage failed)*
   - **Non-engineers can understand** *pipeline*

3. **Built-in features:**
   - **Retry logic** *(exponential backoff)*
   - **Error handling** *(catch, fallback)*
   - **Parallel execution** *(speed up stages)*
   - **Wait states** *(delay between stages if needed)*

4. **Integrates natively with AWS:**
   - **Lambda, SageMaker, DynamoDB, SNS/SQS**
   - *No custom glue code*

5. **State management:**
   - *Maintains* **pipeline state automatically**
   - *Can* **pause/resume**

**Alternatives Considered:**
- **Airflow:** *Too heavyweight, need to manage servers*
- **AWS Glue:** *Data transformation focus, not general orchestration*
- **Custom Lambda chain:** *Hard to maintain, no visual workflow*

---

### Lambda Memory/Timeout Optimization

**Q: "How did you optimize Lambda functions?"**

**Approach:**

1. **Profiling:**
   - *Used* **CloudWatch Logs Insights**
   - *Analyzed* **execution time vs memory**

2. **Memory tuning:**
   - *Default:* **128MB** *(too slow)*
   - *Tested:* **512MB, 1GB, 2GB**
   - **Optimal: 1GB** *(sweet spot for cost/performance)*
   - *More memory =* **more CPU** *(faster execution)*

3. **Cold start reduction:**
   - **Provisioned Concurrency** *for critical paths*
   - **Lazy loading** *(load model on first invocation, cache in global)*
   - **Connection pooling** *(reuse DB connections)*

4. **Timeout optimization:**
   - *Initially:* **3 minutes** *(sometimes timed out)*
   - *Analyzed:* **Most complete in 30 seconds**
   - *Set timeout:* **2 minutes** *(buffer for edge cases)*
   - *For long-running:* **Offload to SageMaker** *(not Lambda)*

---

## 💡 MEHUL'S KEY TIPS SUMMARY

1. **Single-word triggers** (not reading scripts)
2. **30 minutes for VTO is perfect** (you have 1 hour total)
3. **Mention keywords, let them probe**
4. **Details show authenticity** (40→80 people, 23%→93%, honeybee bug)
5. **Scoped to US first, then scaled** (good project management)
6. **Testing internally, then org-wide** (better phrasing)
7. **Impact metrics matter** (60% usage increase, projected cost savings)
8. **Foundation reuse shows extensibility**

---

## 📋 FINAL CHECKLIST

### 30 Min Before:
- [ ] Test video/audio
- [ ] Water nearby
- [ ] Phone silent
- [ ] This file open (scan key sections)

### Mental Prep:
- [ ] **VTO is main story** (100% true, 30 min depth)
- [ ] **Project Scott secondary** (workshop true, prototype true, "projected" metrics)
- [ ] **Technical deep-dives ready** (Step Functions why, Lambda optimization)
- [ ] **5 deep breaths**

### During:
- [ ] **Lead with VTO** (technical artists emphasis)
- [ ] **Watch cues** (stop at "Great")
- [ ] **Offer to elaborate** (don't info-dump)
- [ ] **Use memory triggers** (not reading)
- [ ] **Be authentic** (details show you did it)

---

## 🎯 YOU'VE GOT THIS!

**VTO Project:**
- ✅ 100% true, fully verifiable
- ✅ 30 minutes of authentic depth
- ✅ Shows everything they want (technical artists, cross-functional, AWS, ML, leadership)
- ✅ Impressive metrics (50%, 93%, 60% increase, 15 countries)
- ✅ Lasting impact (org standards, foundation reuse)

**You're prepared. Be confident. Be yourself. Good luck! 🎮🚀**

