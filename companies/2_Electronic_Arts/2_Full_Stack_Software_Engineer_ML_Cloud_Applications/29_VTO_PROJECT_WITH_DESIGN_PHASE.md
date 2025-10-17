# VTO PROJECT - Complete with Design Phase
**Based on:** All feedback from Mehul + System design details

**Interview Time:** 30 minutes for project
**Structure:** 11 key phases, ~2-3 min each

---

## 📋 11 KEY PHASES (Chronological Order)

### Memory Trigger Words:
1. **WHY** (third-party expensive)
2. **WHAT** (extract RGB, finish, particles)
3. **DESIGN** (3 options, recommended Step Functions)
4. **APPROVAL** (tested internally, iterated, org-wide)
5. **ARCHITECTURE** (event-driven, serverless, modular)
6. **DATA LABELING** (bounding boxes)
7. **INITIAL TESTING** (averaging)
8. **EXPERIMENTS** (double-blind, 4-way)
9. **ML MODELS** (parallel pipelines)
10. **CROSS-TEAM** (6 teams, technical artists)
11. **MARKETPLACE** (15 countries) + **IMPACT** (50%, standards, learning)

---

## PHASE 1: WHY - Problem Statement (2-3 min)

**Memory Trigger:** Third-party expensive, non-extensible, wanted control, reduce cost, expand products, 2 days → 1 day

**Full Explanation:**

*We had a* **third-party tool** *that would create* **3D models of lips with lipstick** *from our product images and render them in the* **AR virtual try-on experience**.

**Why We Needed to Replace It:**

1. **Expensive:** *The third-party service was* **costly**

2. **Non-extensible:** *We wanted to* **expand this to other beauty products**—**foundations, eyeliners, eyeshadows**—*but the third-party tool wasn't designed for that*

3. **Wanted more control:** *We wanted* **control over the extraction process**, *the quality standards, and the turnaround time*

4. **Reduce turnaround time:** *It was taking* **2 days** *for the full pipeline (extraction → 3D model → rendering)*. *We wanted to cut that to* **1 day or less** *(50%+ improvement)*.

5. **Cost reduction:** *Building in-house would* **drastically reduce costs** *at scale*

**The Goal:** *Build an* **in-house visual property extraction pipeline** *that could replace the third-party tool, expand to other beauty products, and reduce turnaround time by at least 50%*.

---

## PHASE 2: WHAT - Project Scope (2-3 min)

**Memory Trigger:** Extract RGB, finish type, particle properties, feed to 3D team, user experience context

**Full Explanation:**

**User Experience Context:**

*On the Amazon app, when you go to a lipstick product and want to see what it would look like on you, you can click* **"virtual try-on"**—*the camera opens,* **face tracking** *happens, and you can try different lipsticks in* **real-time AR** *to see what it looks like on you.*

*For this to work, you need:*
- **Face tracking** *(rendering team)*
- **3D lip models** *(3D asset team)*
- **Accurate color and visual properties** *(my team)*

**What We Needed to Extract from Product Images:**

1. **Color (RGB values):** *Precise RGB values for the lipstick color—not "unicorn red" or "sunset pink", but actual* **standardized RGB values**

2. **Finish Type:** **Matte, shiny, satin, glossy**—*different rendering requirements for each*

3. **Particle Properties:** *For lipsticks with* **glitter or shimmer**:
   - **Particle size** *(how big are the glitter particles)*
   - **Particle density** *(how much glitter)*
   - **Particle color** *(gold, silver, multi-color)*

**The Pipeline Flow:**

*Amazon product catalog* → **My pipeline** *(visual property extraction)* → **3D asset creation team** *(creates 3D lip models)* → **Rendering team** *(technical artists, applied scientists - face tracking + AR rendering)* → **Customer Experience team** *(front-end UX, before/after slider)*

**My Ownership:** *I owned the* **extraction pipeline**—*from product catalog through to sending standardized visual properties to the 3D asset team*.

---

## PHASE 3: DESIGN - System Design Options (2-3 min)

**Memory Trigger:** 3 designs, ML Pigeon (bad), AWS native (deprecation), Step Functions (recommended)

**Full Explanation:**

**My Approach to System Design:**

*I came up with* **three different design options** *and created* **full end-to-end designs** *for each*.

**Option 1: ML Pigeon (Internal Color Extraction Framework)**

- **ML Pigeon** *was an internal Amazon framework for color extraction*
- **Pros:** *Already exists, familiar to some teams*
- **Cons:**
  - **Had bottlenecks** *(performance issues)*
  - **Bad reviews from other teams** *who had used it*
  - **Poor response time** *from the customer support team*
  - **Not enough control** *over the extraction process*
  - *Used* **internal tools on path to deprecation**

**Decision:** ❌ **Not recommended**

**Option 2: Entirely AWS Native Services**

- *Use AWS services end-to-end*
- **Pros:** *Fully cloud-native, AWS-supported*
- **Cons:**
  - **Data pipelines service** *we'd use was* **on path to deprecation**
  - **Costs were too high** *for the volume we'd process*

**Decision:** ❌ **Not recommended**

**Option 3: AWS Services with Step Functions Orchestration (RECOMMENDED)**

- **Step Functions** *for* **orchestration** *of multi-stage pipeline*
- **Serverless architecture** *(because jobs could take days—don't want servers sitting idle)*
- **Event-driven** *with* **SNS, SQS** *(product catalog changes trigger pipeline)*
- **AWS Glue components** *for* **data transformation** *(but orchestrated by Step Functions)*
- **Modular/plug-and-play design** *(could swap out components easily)*
- **Lambda functions** *for* **compute** *(preprocessing, orchestration, validation)*
- **SageMaker** *for* **ML model hosting and inference**
- **DynamoDB + S3** *for* **state and storage**

**Why This Design:**
- **Cost-effective** *(serverless, pay-per-use)*
- **Scalable** *(event-driven, parallel processing)*
- **Flexible** *(modular design, swap components)*
- **Future-proof** *(not dependent on deprecated services)*
- **Supports both data labeling AND ML inference** *(plug-and-play)*

**Decision:** ✅ **Recommended this design**

---

## PHASE 4: APPROVAL - Internal Review & Org-Wide Presentation (2-3 min)

**Memory Trigger:** Tested internally, incorporated feedback, iterated, org-wide presentation, approved, assigned team

**Full Explanation:**

**Step 1: Internal Team Review**

*First, I* **tested the design internally within my team**:
- *Presented all three options to* **senior engineers** *and* **team members**
- *Got their feedback on trade-offs, risks, technical feasibility*
- **Incorporated their feedback** *into the design*
- **Iterated on the design** *based on their input (minor modifications)*

**Why Internal First:**
- **Validate technical assumptions** *before going org-wide*
- **Get buy-in from senior engineers** *(credibility)*
- **Refine the design** *with technical experts*
- **Identify blind spots** *early*

**Step 2: Organizational-Wide Presentation**

*Once the design was solid, I* **led an organizational-wide meeting**:
- **Presented all three design options**
- **Explained trade-offs** *for each*
- **Recommended Option 3** *(Step Functions + serverless)*
- *Got* **approval to move forward** *with implementation*

**Team Assignment:**

*After approval, I was assigned:*
- **3 developers** *to work with*
- **2 machine learning engineers**

*Total team:* **Me (technical lead) + 5 engineers**

**Why This Mattered:**

- **Cross-functional buy-in** *early on*
- **Clear decision-making process** *(transparent, data-driven)*
- **Team was aligned** *on the chosen design before we wrote any code*
- **Reduced risk** *of pivoting mid-project*

---

## PHASE 5: ARCHITECTURE IMPLEMENTATION - Building It Out (2-3 min)

**Memory Trigger:** Event-driven, Step Functions, Lambda, SageMaker, DynamoDB, S3, CDK, 4-stage CI/CD, modular

**Full Explanation:**

**Event-Driven Pipeline:**

- **Product catalog changes** *triggered* **SNS events**
- **Step Functions** *orchestrated* **multi-stage pipeline**
  - *Each stage was a* **separate Lambda function** *or* **SageMaker job**
  - *Could run stages* **in parallel** *where possible*
  - *Built in* **retry logic** *and* **error handling**

**Lambda Functions (Orchestration & Compute):**

- **Preprocessing:** *Image quality checks, validation*
- **Filtering:** *Extract only beauty products (lipsticks initially)*
- **Orchestration:** *Call SageMaker endpoints, manage state*
- **Post-processing:** *Format extracted properties, send to next team*

**SageMaker (ML Platform):**

- **SageMaker Ground Truth** *for* **data labeling workflows**
- **SageMaker Training Jobs** *for* **model training** *(data scientists' models)*
- **SageMaker Endpoints** *for* **real-time inference** *(color extraction, bounding boxes)*

**Storage & State:**

- **S3** *for:*
  - *Raw product images*
  - *Intermediate artifacts*
  - *Extracted visual property data*
  - *Model artifacts*
- **DynamoDB** *for:*
  - *Pipeline state tracking*
  - *Metadata (which products processed, when)*
  - *Session state*

**API Layer:**

- **API Gateway** *with* **Cognito authentication**
- **Lambda** *for API orchestration and business logic*

**Infrastructure as Code:**

- **AWS CDK (TypeScript)** *generating* **CloudFormation templates**
- **4-staged CI/CD pipeline:**
  - **Dev:** *Deploy on every commit (automated)*
  - **Gamma:** *Deploy on merge to main (automated tests, manual approval)*
  - **Pre-Prod:** *Canary deployment (10% traffic)*
  - **Prod:** *Full rollout after validation*

**Monitoring & Observability:**

- **CloudWatch** *for:*
  - *Metrics (pipeline throughput, error rates)*
  - *Logs (Lambda execution, SageMaker jobs)*
  - *Alarms (notify on failures)*
  - *Dashboards (real-time pipeline health)*
- **X-Ray** *for* **distributed tracing** *(track requests across services)*

**Why Modular Design:**

*This is key:* **The pipeline was designed to be plug-and-play**:
- *Initially, we sent images to* **data labelers** *(human annotation)*
- *Later, we could* **swap in ML models** *(automated inference)*
- **Same pipeline, different component** *(just change which Lambda/SageMaker endpoint to call)*
- *This let us* **iterate quickly** *and* **experiment** *without rebuilding the whole system*

---

## PHASE 6: DATA LABELING - Bounding Boxes (2-3 min)

**Memory Trigger:** SageMaker Ground Truth, data labelers, bounding boxes, exact pixels, avoid shine

**Full Explanation:**

**The Challenge:** *Product images had* **varying lighting, angles, backgrounds**. *Some had* **shine from studio lights** *that would mess up RGB values if we just extracted from the whole image*.

**Solution: Bounding Boxes via SageMaker Ground Truth**

*We used* **SageMaker Ground Truth** *to set up* **data labeling workflows**:

1. **Product images sent to data labelers** *(human annotators)*
2. **Data labelers created bounding boxes** *around the exact area of the lipstick product (not packaging, not background)*
3. *This identified the* **right pixels** *to extract color from*
4. **Avoided shine/lighting artifacts** *by focusing on specific areas*

**Why This Mattered:**

- *If we averaged the entire image:* **Packaging colors, background, lighting reflections** *would skew results*
- *Bounding boxes:* **Focus on actual lipstick product**
- *Created* **training data** *for ML models later*

**Workflow:**

- **Images → S3**
- **S3 triggers Lambda** *via SNS*
- **Lambda creates SageMaker Ground Truth labeling job**
- **Data labelers annotate** *(bounding boxes)*
- **Results stored in S3** *(bounding box coordinates)*
- **Used for immediate extraction AND ML training**

---

## PHASE 7: INITIAL TESTING - Averaging Approach (2-3 min)

**Memory Trigger:** No ML yet, averaging pixels, proof of concept, parallel to ML development

**Full Explanation:**

**Starting Point:** *We didn't have ML models trained yet, so we started with a* **simple averaging approach** *while data scientists worked on models in parallel*.

**Process:**

1. *Take* **bounding box coordinates** *from data labelers*
2. **Extract all pixels** *within the bounding box*
3. **Average the RGB values** *across those pixels*
4. *Use that as* **initial color estimate**
5. *For finish type:* **Simple heuristics** *(high variance in pixel values → shiny, low variance → matte)*

**Purpose:**

- **Proof of concept:** *Does this approach even work?*
- **Generate initial data** *for early testing and experiments*
- **Identify problems early** *(e.g., lighting still affecting results)*
- **Start the realism testing pipeline** *while ML models were being developed*
- **Don't block on ML:** *Make progress while data scientists train models*

---

## PHASE 8: EXPERIMENTS - Double-Blind Realism Testing (2-3 min)

**Memory Trigger:** Bought real lipsticks, double-blind, diverse demographics, 4-way comparison, internal app automates testing

**Full Explanation:**

**The Realism Challenge:** *How do we know if our extracted color values* **actually look realistic** *when rendered in AR on different skin tones?*

**Solution: Data-Driven Experiments**

1. **Bought the actual lipsticks** *from beauty brands (L'Oréal, Maybelline, Revlon, etc.)*

2. **Recruited people of different ethnicities and skin tones:**
   - *Different genders*
   - *Different skin pigmentation*
   - *Diverse demographics (Asian, Black, White, Hispanic, etc.)*

3. **Had them wear the real lipsticks** *and took* **reference photos** *(ground truth)*

4. **4-Way Comparison:**
   - **Real lipstick photo** *(ground truth - what it actually looks like)*
   - **Third-party tool rendering** *(baseline to beat)*
   - **Our averaging approach rendering**
   - **Our ML model rendering** *(once models were trained)*

5. **Built an internal app** *to automate this entire workflow:*
   - *People could quickly* **upload screenshots** *of each rendering*
   - **Submit to realism testing platform**
   - **Score how close each rendering was** *to the real lipstick (1-10 scale)*
   - **Aggregate scores across demographics**
   - *Automated the entire* **realism test workflow**

**Why This Was Powerful:**

- **Data-driven decisions:** *Not subjective opinions—actual user data*
- **Cross-team alignment:** *Brought experimental results to meetings with PMs, data scientists, technical artists*
  - *Showed* **"low-quality data = poor AR realism = bad customer experience = returns/churn"**
- **Validated improvements:** *Could prove our ML models > averaging > third-party*
- **Informed model development:** *Data scientists used scores to improve models*

**Collaboration with Technical Artists (CRITICAL):**

*This is where I worked most closely with* **technical artists on the rendering team**:

- **Regular syncs on visual calibration**
- *Key questions they cared about:*
  - **"What RGB values look realistic on different skin tones in AR?"**
  - **"How does lighting affect perception?"**
  - **"What about glossy vs matte rendering?"**
- *I brought* **experimental data** *to these discussions, not just technical specs*
- *This helped us align on what "realistic" meant* **technically (accurate RGB) vs artistically (looks good)**

**Result:** *We achieved* **color accuracy standards** *that balanced* **technical precision with visual realism**, *validated through user testing*.

---

## PHASE 9: ML MODELS - Parallel Pipelines (2-3 min)

**Memory Trigger:** Data scientists, applied scientists, custom models, parallel pipelines (labelers + ML), continuous learning

**Full Explanation:**

**Working with Data Scientists / Applied Scientists:**

*In parallel with the averaging approach, I worked with* **2 machine learning engineers** *and collaborated with* **data scientists / applied scientists** *to develop* **custom ML models** *using the labeled data*.

**Their Process (I guided architecture, they built models):**

1. **Took the labeled data** *(bounding boxes from SageMaker Ground Truth)*
2. **Trained models for:**
   - **Bounding box detection** *(automatically find the lipstick in product images)*
   - **Color extraction** *(more sophisticated than averaging—account for lighting, texture, reflections)*
   - **Finish type classification** *(matte, shiny, satin, glossy)*
   - **Particle detection** *(identify glitter, quantify size and density)*

**My Role:**

- *I* **didn't create the ML models myself** *(data scientists did)*
- *But I:*
  - **Architected the pipelines** *(how data flows, how models are invoked, how results are stored)*
  - **Integrated SageMaker endpoints** *(Lambda functions calling inference endpoints)*
  - **Set up the continuous learning loop** *(feedback from realism tests → retrain models)*
  - **Worked with them on feature engineering** *(what features matter for color extraction? Pixel variance? Edge detection?)*
  - **Provided infrastructure** *(SageMaker training jobs, endpoint configuration, auto-scaling)*

**Parallel Pipelines (Key Innovation):**

*Once ML models were trained, we ran* **two pipelines in parallel**:

1. **Data labeling pipeline** *for new/edge-case products:*
   - **SageMaker Ground Truth → human labelers → training data**
   - *Fed back into model retraining*

2. **ML inference pipeline** *for most products:*
   - **SageMaker endpoints → automated extraction → fast turnaround**

**Why Parallel:**

- **New data kept improving models** *(continuous learning loop)*
- **ML handled 90%+ of products automatically** *(faster, cheaper)*
- **Human labelers validated edge cases** *(unusual products, low-quality images, new product types)*
- **Modular design made this easy** *(just route to different component based on product type)*

---

## PHASE 10: CROSS-TEAM COLLABORATION - 6 Teams (3-4 min)

**Memory Trigger:** 6 teams - technical artists FIRST, designers, data scientists, PMs, 3D team, beauty brands

**Full Explanation:**

*This project required coordinating across* **6 different teams**:

**1. Technical Artists (Rendering Team) - CLOSEST COLLABORATION:**

- *These were* **applied scientists and technical artists** *focused on* **real-time AR rendering** *and* **face tracking**
- **Regular syncs on visual calibration** *(weekly meetings)*
- *Key question:* **"What RGB values look realistic across different skin tones in AR?"**
- *I brought* **experimental data from double-blind tests** *to our discussions*
- *We aligned on* **color accuracy standards** *that balanced* **technical precision (accurate RGB)** *with* **visual realism (looks good in AR)**
- *They understood* **visual realism** *(artistic side: what looks good)*, *I ensured our pipeline* **delivered the right data** *(technical side: accurate extraction)*
- **Example collaboration:** *When rendering glossy lipstick, they needed not just color but also* **reflectance values**. *I added that to our extraction pipeline based on their feedback.*

**2. Designers (Customer Experience Team):**

- *Sister team owned* **front-end UX** *including* **before/after slider feature** *(swipe to see with/without lipstick)*
- **Collaborated on visual property standards**
- *Example challenge:* **Balancing design goals** *(immediate visual feedback—users don't want to wait)* **with technical constraints** *(processing takes time)*
- *Prototyped solutions, showed trade-offs with real data*
- *Agreed on* **asynchronous processing with progress indicators** *(spinner while processing, then show result)*

**3. Data Scientists / Applied Scientists:**

- **Created and trained ML models** *for bounding boxes and color extraction*
- *I provided:*
  - **Infrastructure** *(SageMaker training jobs, endpoint hosting)*
  - **Data pipelines** *(labeled data from Ground Truth)*
  - **Feedback loop** *(realism test scores to improve models)*
- *They provided:*
  - **Model development** *(architecture, training, tuning)*
  - **Expertise** *(what features matter, how to handle edge cases)*
- *Example challenge:* **Insufficient labeled training data initially** *(only had 500 images)*
- *My solution:* *Scaled up* **SageMaker Ground Truth pipeline**, *recruited more data labelers*, *got to 10,000+ labeled images*
- *Result:* **Model accuracy improved from 65% to 92%**

**4. Product Managers:**

- **Defined requirements** *for what visual properties to extract*
- **Prioritized product rollout** *(lipsticks first, then foundations, etc.)*
- *Example challenge:* *Initial requirements were vague ("make AR try-on realistic")*
- *My approach:* **Multiple iteration cycles**, *prototyped early to clarify what "realistic" means*, *showed them 4-way comparison results*
- *Result:* **Concrete requirements:** *RGB values, finish type, particle properties, reflectance values*

**5. 3D Asset Creation Team (External to Beauty Tech):**

- *Specialized team that* **created 3D lip models** *from our extracted properties*
- **Defined data format handoffs and API contracts** *(what format do they need? JSON? What fields?)*
- *Example challenge:* *One time, coordinate system context was misunderstood (they thought origin was top-left, we sent bottom-left)*
- *My approach:* *Scheduled meeting to clarify, created detailed API documentation, added validation*
- **Leadership decision:** *Respected their expertise (they're 3D modeling experts), guided overall direction without micromanaging, let them handle 3D generation autonomously*
- *Result:* **Smooth handoff pipeline** *(< 5% error rate on handoffs)*

**6. Beauty Brand Bridge Teams:**

- *Teams interfacing with beauty brand clients* **(L'Oréal, Maybelline, Revlon, MAC, etc.)**
- **Problem they brought to me:** *Beauty brands were submitting* **wildly inconsistent product photos**:
  - *Different lighting (studio vs natural)*
  - *Different angles (straight-on vs 45°)*
  - *Different backgrounds (white vs textured)*
  - *Text descriptions like "unicorn red" instead of RGB values*
- *My approach:* **Worked backward**—*"Why are photos bad quality? Let's fix it at the source."*
  - *Worked with bridge teams to* **improve photo submission forms** *(requirements: white background, natural lighting, straight-on angle)*
  - *Created* **naming conventions** *for color descriptions*
  - *Established* **best practices for RGB value submission** *(use color picker tools)*
- *Result:* **Standards adopted organization-wide** *(now all beauty brand partners follow these guidelines)*

---

## PHASE 11: MARKETPLACE EXPANSION + IMPACT (3-4 min)

**Memory Trigger:** Phased rollout, US → 15 countries, A/B testing, 50% turnaround, org standards, work backward learning

**Full Explanation:**

### Marketplace Expansion (15 Countries)

**Phased Rollout Approach:**

**Phase 1: United States**
- *Started with* **US marketplace** *(largest, most data, easiest to monitor)*
- *Validated the pipeline at scale*
- **A/B testing:** *50% traffic to our in-house tool, 50% to third-party*
- *Monitored closely for issues*

**Phase 2: Japan**
- *Expanded to* **Japan** *(different beauty product preferences, different average skin tones)*
- **Continued A/B testing**
- *Found some edge cases (Japanese beauty brands had different packaging styles)*

**Phase 3: Europe**
- *Rolled out to* **European marketplaces** *(UK, Germany, France, Italy, Spain)*
- *By now, confident in the system—moved to 80/20 traffic split*

**Phase 4: Asia & Latin America**
- **Asia:** *China, India, Singapore, other Asian markets*
- **Latin America:** *Mexico, Brazil*
- *Total:* **15 countries**

**Why Phased:**

- **Risk mitigation:** *If something broke, only affected one marketplace*
- **Localization:** *Different countries had different beauty product catalogs*
- **A/B testing validation:** *Could compare our in-house vs third-party per marketplace*
- **Gradual load increase:** *Ensured pipeline scaled properly (from 100K products/day to millions)*

**My Role:**

- **Monitored rollouts** *(CloudWatch dashboards, real-time alarms)*
- **Coordinated with regional teams** *(different time zones, different holidays, different on-call schedules)*
- **Handled escalations** *(when issues arose, debugged quickly)*
- **Optimized for scale** *(tuned Lambda memory, SageMaker auto-scaling policies)*

---

### Measured Impact

**1. Turnaround Time:**
- *Reduced from* **2 days → 1 day** **(50% improvement)**
- *For the full pipeline: extraction → 3D model → rendering*

**2. Cost Savings:**
- **Replaced third-party tool** *entirely*
- **Drastically reduced costs** *at scale (processing millions of products)*

**3. Quality Improvement:**
- **High data quality** *validated through double-blind user experiments*
- **92% model accuracy** *(vs 65% with initial averaging approach)*

**4. Scalability:**
- *Successfully processed* **entire Amazon Beauty catalog** *(millions of products)* *across* **15 countries**

**5. Extensibility:**
- *Created foundation to* **expand to other beauty products**:
  - **Foundations** *(already started)*
  - **Eyeliners, eyeshadows** *(on roadmap)*
  - **Nail polish** *(future)*

---

### Organizational Impact (Lasting)

**1. Established Org-Wide Standards:**
- **Photo submission standards** *(lighting, resolution, angles, background)*
- **Naming conventions** *(adopted across entire Beauty Tech organization)*
- **Color value standards** *(RGB values, finish types)*
- *These standards were* **adopted for all future beauty brand partnerships**

**2. Standardized Onboarding Process:**
- *New beauty brands now follow* **our guidelines** *from day one*
- **Faster onboarding** *(don't have to fix photos after submission)*
- **Higher quality data** *from the start*

**3. Fed into Larger Data Lake:**
- *This pipeline was part of the* **larger Beauty Tech data lake**
- *Processing* **40TB/day**
- *Serving* **40M+ monthly customers** *globally*

---

### Key Challenges (Summary)

**1. Non-standard inputs:**
- *Solved by* **working backward to improve photo submissions at source**

**2. Cross-team alignment:**
- *Solved with* **data-driven discussions** *(showed experimental results proving quality matters)*

**3. Scale:**
- *Solved with* **event-driven architecture, parallel processing, optimization** *(Step Functions, Lambda, SageMaker auto-scaling)*

---

### Key Learning (Critical Takeaway)

*The biggest learning was:* **Don't just solve the immediate technical problem—work backward to address root causes.**

*In this case, I could have just built better and better extraction algorithms to handle bad photos. But instead, I worked with* **beauty brand bridge teams** *to* **improve the data at the source** *(photo submissions)*.

*This approach created* **lasting organizational impact** *(standards adopted for future partners)* *rather than just a one-time technical fix*.

*I took this learning into all my next projects:* **"What's the root cause? How do we fix it upstream?"**

---

## 🎯 USAGE GUIDE

### Full Walkthrough (30 min):
Go through all 11 phases chronologically (~2-3 min each)

### Key Emphasis Points:

✅ **Technical Artists FIRST** in cross-team (Tyler asked)
✅ **Data-driven experiments** (double-blind, 4-way comparison)
✅ **System design process** (3 options, internal review, org-wide approval)
✅ **Working backward from root causes** (photo submission standards)
✅ **Lasting organizational impact** (standards for future partners)
✅ **Modular/plug-and-play architecture** (swap components easily)
✅ **50% turnaround improvement** (concrete metric)

### Flexibility:

**Watch interviewer cues:**
- Engaged → keep going chronologically
- Interrupt with questions → answer, then offer to continue
- Say "Great" → offer to go deeper or move on

**Offer choices:**
- *"I can go deeper into [technical architecture / cross-team dynamics / ML models / experiments]—what would be most useful?"*

---

## 🚀 YOU'VE GOT THIS!

**This is your strongest story. 100% true, fully verifiable, demonstrates everything they want:**

✅ **Cross-functional (6 teams, especially technical artists)**
✅ **AWS serverless architecture (their exact stack)**
✅ **ML/AI in production (SageMaker, custom models)**
✅ **Leadership (led team, coordinated 6 teams, 15 countries)**
✅ **System design (3 options, justified recommendation)**
✅ **Challenges + Solutions (problem-solving)**
✅ **Lasting impact (org-wide standards)**
✅ **Data-driven (experiments, metrics)**

**30 minutes is perfect for this depth. Go get it! 🎮🚀**

