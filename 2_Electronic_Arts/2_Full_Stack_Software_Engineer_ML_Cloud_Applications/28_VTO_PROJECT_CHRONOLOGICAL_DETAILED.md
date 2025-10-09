# VTO PROJECT - Chronological Detailed Walkthrough
**Based on:** Mehul's structural advice + User's detailed explanation

**Interview Time Allocation:** 30 minutes for project (out of 1-hour interview)
**Structure:** 10 key phases, ~2-3 min each

---

## 🎯 PROJECT OVERVIEW (30 seconds)

**What:** Visual Property Extraction pipeline for AR virtual try-on at Amazon Beauty Tech

**User Experience:** On Amazon app, go to lipstick product → click "virtual try-on" → camera opens → try different lipsticks in real-time AR → see what it looks like on you

**My Role:** Technical lead for extracting color (RGB values), finish type (matte/shiny), particle properties (glitter size, shimmer) → send to 3D modeling team → they create 3D lip models → rendering team does AR

---

## 📋 10 KEY PHASES (Chronological Order)

### Memory Trigger Words:
1. **WHY** (third-party expensive)
2. **WHAT** (extract RGB, finish, particles)
3. **ARCHITECTURE** (event-driven, Step Functions, SageMaker)
4. **DATA LABELING** (bounding boxes, pixel selection)
5. **INITIAL TESTING** (averaging approach)
6. **EXPERIMENTS** (double-blind, real lipsticks, 4-way comparison)
7. **ML MODELS** (data scientists, parallel pipelines)
8. **CROSS-TEAM** (6 teams, technical artists first)
9. **MARKETPLACE EXPANSION** (US → 15 countries)
10. **IMPACT + LEARNING** (50% faster, org standards, work backward)

---

## PHASE 1: WHY - Problem Statement (2-3 min)

**Memory Trigger:** Third-party expensive, non-extensible, wanted control, reduce cost, expand products

**Full Explanation:**

*We had a* **third-party tool** *that would create* **3D models of lips with lipstick** *from our product images and render them in the* **AR virtual try-on experience**.

**Why We Needed to Replace It:**

1. **Expensive:** *The third-party service was* **costly**

2. **Non-extensible:** *We wanted to* **expand this to other beauty products**—**foundations, eyeliners, eyeshadows**—*but the third-party tool wasn't designed for that*

3. **Wanted more control:** *We wanted* **control over the extraction process**, *the quality standards, and the turnaround time*

4. **Reduce turnaround time:** *It was taking* **2 days** *for the full pipeline (extraction → 3D model → rendering)*. *We wanted to cut that significantly.*

5. **Cost reduction:** *Building in-house would* **drastically reduce costs** *at scale*

**The Goal:** *Build an* **in-house visual property extraction pipeline** *that could replace the third-party tool, expand to other beauty products, and reduce turnaround time by at least 50%*.

---

## PHASE 2: WHAT - Project Scope (2-3 min)

**Memory Trigger:** Extract RGB, finish type, particle properties, feed to 3D team

**Full Explanation:**

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

## PHASE 3: ARCHITECTURE - Technical Implementation (2-3 min)

**Memory Trigger:** Event-driven, Step Functions, Lambda, SageMaker, DynamoDB, S3, CDK, 4-stage CI/CD

**Full Explanation:**

**Event-Driven Pipeline:**

- **Product catalog changes** *triggered* **SNS events**
- **Step Functions** *orchestrated* **multi-stage pipeline**
- **Lambda functions** *for:*
  - *Preprocessing and validation*
  - *Image quality checks*
  - *Orchestration between stages*
  - *Invoking SageMaker endpoints*

**ML/Data Processing:**

- **SageMaker Ground Truth** *for* **data labeling** *(bounding boxes)*
- **SageMaker endpoints** *for* **ML model inference** *(bounding box detection, color extraction)*
- **Custom models** *developed by data scientists*

**Storage & State:**

- **S3** *for:*
  - *Raw product images*
  - *Intermediate artifacts*
  - *Extracted visual property data*
  - *Model artifacts*
- **DynamoDB** *for:*
  - *Session state*
  - *Metadata tracking*
  - *Pipeline status*

**API Layer:**

- **API Gateway** *with* **Cognito authentication**
- **Lambda** *for orchestration and business logic*

**Infrastructure:**

- **AWS CDK (TypeScript)** *generating* **CloudFormation**
- **4-staged CI/CD:** dev → gamma → pre-prod → prod
- **CloudWatch** *for metrics, alarming, dashboards*
- **X-Ray** *for distributed tracing*

---

## PHASE 4: DATA LABELING - Bounding Boxes (2-3 min)

**Memory Trigger:** SageMaker Ground Truth, data labelers, bounding boxes, exact pixels, avoid shine

**Full Explanation:**

**The Challenge:** *Product images had* **varying lighting, angles, backgrounds**. *Some had* **shine from studio lights** *that would mess up RGB values if we just extracted from the whole image*.

**Solution: Bounding Boxes**

*We used* **SageMaker Ground Truth** *to set up* **data labeling workflows**:

1. **Sent product images to data labelers**
2. **Data labelers created bounding boxes** *around the exact area of the lipstick product within the packaging*
3. *This helped us identify the* **right pixels** *to extract color from*
4. **Avoided shine/lighting artifacts** *by focusing on specific areas*

**Why This Mattered:**

- *If we just averaged the entire image, we'd include* **packaging colors**, **background colors**, **lighting reflections**
- *Bounding boxes let us focus on the* **actual lipstick product**
- *This created* **training data** *for ML models later*

---

## PHASE 5: INITIAL TESTING - Averaging Approach (2-3 min)

**Memory Trigger:** No ML models yet, averaging pixels, initial experiments, see how it works

**Full Explanation:**

**Starting Point:** *We didn't have ML models trained yet, so we started with a* **simple averaging approach**.

**Process:**

1. *Take the* **bounding box coordinates** *from data labelers*
2. **Extract all pixels** *within the bounding box*
3. **Average the RGB values** *across those pixels*
4. *Use that as our* **initial color estimate**

**Purpose:**

- **Proof of concept:** *Does this approach even work?*
- **Generate initial data** *for early testing*
- **Identify problems early** *(e.g., lighting still affecting results)*
- **Start the realism testing process** *while data scientists worked on ML models in parallel*

---

## PHASE 6: EXPERIMENTS - Double-Blind Realism Testing (2-3 min)

**Memory Trigger:** Bought real lipsticks, double-blind, different ethnicities/skin tones, 4-way comparison, internal app

**Full Explanation:**

**The Realism Challenge:** *How do we know if our extracted color values* **actually look realistic** *when rendered in AR on different skin tones?*

**Solution: Data-Driven Experiments**

1. **Bought the actual lipsticks** *from beauty brands (L'Oréal, Maybelline, etc.)*

2. **Recruited people of different ethnicities and skin tones:**
   - *Different genders*
   - *Different skin pigmentation*
   - *Diverse demographics*

3. **Had them wear the real lipsticks** *and took* **reference photos**

4. **4-Way Comparison:**
   - **Real lipstick photo** *(ground truth)*
   - **Third-party tool rendering**
   - **Our averaging approach rendering**
   - **Our ML model rendering** *(once available)*

5. **Built an internal app** *to automate this process:*
   - *People could quickly* **create screenshots**
   - **Submit to realism testing platform**
   - **Score how close each rendering was** *to the real lipstick*
   - *Automated the entire* **realism test workflow**

**Why This Was Powerful:**

- **Data-driven decisions:** *Not just subjective opinions—actual user data*
- **Cross-team alignment:** *Brought these results to meetings with PMs, data scientists, technical artists to show* **"low-quality data = poor AR realism = customer churn"**
- **Validated improvements:** *Could prove our ML models were better than averaging, better than third-party*

**Collaboration with Technical Artists:**

*This is where I worked most closely with the* **technical artists on the rendering team**. *We had* **regular syncs on visual calibration**:
- *What RGB values look realistic on different skin tones?*
- *How does lighting affect perception?*
- *What about glossy vs matte rendering?*

*I brought* **experimental data** *to these discussions, not just technical specs. This helped us align on what "realistic" meant* **technically vs artistically**.

---

## PHASE 7: ML MODELS - Parallel Pipelines (2-3 min)

**Memory Trigger:** Data scientists, applied scientists, custom models, parallel pipelines, labelers + ML

**Full Explanation:**

**Working with Data Scientists / Applied Scientists:**

*In parallel with the averaging approach, I worked with* **data scientists and applied scientists** *to develop* **custom ML models** *using the labeled data*.

**Their Process (I guided, they executed):**

1. **Took the labeled data** *(bounding boxes from SageMaker Ground Truth)*
2. **Trained models for:**
   - **Bounding box detection** *(automatically find the lipstick in product images)*
   - **Color extraction** *(more sophisticated than averaging—account for lighting, texture)*
   - **Finish type classification** *(matte, shiny, satin, glossy)*
   - **Particle detection** *(identify glitter, quantify size and density)*

**Parallel Pipelines:**

*Once ML models were trained, we ran* **two pipelines in parallel**:

1. **Data labeling pipeline** *for new products* **(SageMaker Ground Truth → human labelers → training data)**
2. **ML inference pipeline** *for products* **(SageMaker endpoints → automated extraction)**

**Why Parallel:**

- **New data kept improving models** *(continuous learning loop)*
- **ML handled most products automatically** *(faster, cheaper)*
- **Human labelers validated edge cases** *(unusual products, low-quality images)*

**My Role:**

- *I* **didn't create the ML models myself** *(data scientists did)*
- *But I:*
  - **Architected the pipelines** *(how data flows, how models are invoked)*
  - **Integrated SageMaker endpoints** *(Lambda functions calling inference endpoints)*
  - **Set up the continuous learning loop** *(feedback from realism tests → retrain models)*
  - **Worked with them on feature engineering** *(what features matter for color extraction?)*

---

## PHASE 8: CROSS-TEAM COLLABORATION - 6 Teams (2-3 min)

**Memory Trigger:** 6 teams - technical artists FIRST, designers, data scientists, PMs, 3D team, beauty brands

**Full Explanation:**

**This project required coordinating across 6 different teams:**

**1. Technical Artists (Rendering Team) - CLOSEST COLLABORATION:**

- *These were* **applied scientists and technical artists** *focused on* **real-time AR rendering** *and* **face tracking**
- **Regular syncs on visual calibration**
- *Key question:* **"What RGB values look realistic across different skin tones in AR?"**
- *I brought* **experimental data from double-blind tests** *to our discussions*
- *We aligned on* **color accuracy standards** *that balanced* **technical precision with visual realism**
- *They understood* **visual realism** *(artistic side)*, *I ensured our pipeline* **delivered the right data** *(technical side)*

**2. Designers (Customer Experience Team):**

- *Sister team owned* **front-end UX** *including* **before/after slider feature**
- **Collaborated on visual property standards**
- *Example challenge:* **Balancing design goals** *(immediate visual feedback)* **with technical constraints** *(processing time)*
- *Prototyped solutions, showed trade-offs with real data*
- *Agreed on* **asynchronous processing with progress indicators**

**3. Data Scientists / Applied Scientists:**

- **Created and trained ML models** *for bounding boxes and color extraction*
- **Collaboration:** *Model training, validation experiments, feature engineering*
- *Example challenge:* **Insufficient labeled training data initially**
- *My solution:* *Established* **SageMaker Ground Truth pipeline**, *recruited data labelers*
- *Result:* **High-quality training dataset**, *improved model accuracy*

**4. Product Managers:**

- **Defined requirements** *for what visual properties to extract*
- **Collaboration:** *Requirements gathering, working backward from product vision*
- *Example challenge:* *Initial requirements were vague ("make AR try-on realistic")*
- *My approach:* **Multiple iteration cycles**, *prototyped early to clarify disconnects*
- *Result:* **Concrete requirements:** *RGB values, product dimensions, texture data*

**5. 3D Asset Creation Team (External to Beauty Tech):**

- *Specialized team that* **created 3D lip models** *from our extracted properties*
- **Collaboration:** *Defined data format handoffs, API contracts*
- *Example challenge:* *Coordinate system context was misunderstood*
- *My approach:* *Scheduled meeting to clarify, documented assumptions*
- **Leadership decision:** *Respected their expertise (they're 3D modeling experts), guided overall direction without micromanaging*
- *Result:* **Smooth handoff pipeline**, *they handled 3D generation autonomously*

**6. Beauty Brand Bridge Teams:**

- *Teams interfacing with beauty brand clients* **(L'Oréal, Maybelline, etc.)**
- **Collaboration:** *Improved product photo submission platform*
- *Example challenge:* **Non-standard photo submissions** *(lighting, angles, backgrounds varied wildly—"unicorn red" instead of RGB values)*
- *My approach:* **Worked backward**—*"Why are photos bad quality?"—guided* **standardization of submission forms**
- *Result:* **Internal standards** *for color values, naming conventions, photo quality* **(lighting, resolution, angles)** *adopted* **organization-wide**

---

## PHASE 9: MARKETPLACE EXPANSION - 15 Countries (2-3 min)

**Memory Trigger:** Phased rollout, US → Japan → Europe → Asia → Mexico, A/B testing, 15 countries

**Full Explanation:**

**Scaling Globally:**

*Once the pipeline was working, we* **rolled it out to 15 countries** *in a* **phased approach**:

**Phase 1: United States**
- *Started with* **US marketplace** *(largest, most data)*
- *Validated the pipeline at scale*
- *Monitored for issues*

**Phase 2: Japan**
- *Expanded to* **Japan** *(different beauty product preferences, different skin tones)*
- **A/B testing** *to compare our in-house extraction vs third-party*

**Phase 3: Europe**
- *Rolled out to* **European marketplaces** *(UK, Germany, France, Italy, Spain)*
- *Continued monitoring and optimization*

**Phase 4: Asia & Mexico**
- **Asia:** *China, India, other Asian markets*
- **Mexico** *and* **Latin American markets**
- *Total:* **15 countries**

**Why Phased Rollout:**

- **Risk mitigation:** *If something broke, it only affected one marketplace*
- **Localization:** *Different countries had different beauty product catalogs*
- **A/B testing:** *Could compare our in-house tool vs third-party per marketplace*
- **Gradual load increase:** *Ensured our pipeline scaled properly*

**My Role:**

- **Monitored rollouts** *(CloudWatch dashboards, alarms)*
- **Coordinated with regional teams** *(different time zones, different requirements)*
- **Handled escalations** *(when issues arose in specific marketplaces)*
- **Optimized for scale** *(as load increased from 1 country to 15)*

---

## PHASE 10: IMPACT + LEARNING - Results & Takeaways (2-3 min)

**Memory Trigger:** 50% faster turnaround, org standards, work backward from root causes, lasting impact

**Full Explanation:**

**Measured Impact:**

1. **Turnaround Time:** *Reduced from* **2 days to 1 day** **(50% improvement)** *for the full pipeline (extraction → 3D model → rendering)*

2. **Cost Savings:** **Replaced third-party tool** *entirely, drastically reduced costs at scale*

3. **Quality Improvement:** **High data quality** *validated through our double-blind user experiments*

4. **Scalability:** *Successfully processed the* **entire Amazon Beauty catalog** *(millions of products)* *across* **15 countries**

5. **Extensibility:** *Created foundation to* **expand to other beauty products** *(foundations, eyeliners, eyeshadows)*

**Organizational Impact:**

1. **Established org-wide standards:**
   - **Photo submission standards** *(lighting, resolution, angles)*
   - **Naming conventions** *(adopted across Beauty Tech organization)*
   - **Color value standards** *(RGB values, finish types)*
   - *These standards were adopted for* **future beauty brand partnerships**

2. **Created standardized onboarding process** *for new beauty brands*

3. **Fed into larger Beauty Tech data lake:** *This pipeline was part of the larger data lake processing* **40TB/day**, *serving* **40M+ monthly customers**

**Key Challenges (Summary):**

1. **Non-standard inputs** *(solved by working backward to improve photo submissions at source)*
2. **Cross-team alignment** *(solved with data-driven discussions showing quality matters)*
3. **Scale** *(solved with event-driven architecture, parallel processing, optimization)*

**Key Learning:**

*The biggest learning was* **don't just solve the immediate technical problem—work backward to address root causes**.

*In this case, I could have just built better and better extraction algorithms to handle bad photos. But instead, I worked with* **beauty brand bridge teams** *to* **improve the data at the source** *(photo submissions)*.

*This approach created* **lasting organizational impact** *(standards adopted for future partners)* *rather than just a one-time technical fix*.

*I took this learning into my next projects:* **"What's the root cause? How do we fix it upstream?"**

---

## 🎯 USAGE GUIDE

### Full 30-Minute Walkthrough:
Go through all 10 phases chronologically (2-3 min each)

### Shorter Versions (If They Interrupt/Redirect):

**5-Minute Version:**
- Phase 1 (Why)
- Phase 2 (What)
- Phase 3 (Architecture - high level)
- Phase 8 (Cross-team - emphasize technical artists)
- Phase 10 (Impact + Learning)

**10-Minute Version:**
- Phase 1 (Why)
- Phase 2 (What)
- Phase 3 (Architecture)
- Phase 6 (Experiments - double-blind testing)
- Phase 8 (Cross-team - all 6 teams)
- Phase 10 (Impact + Learning)

**15-Minute Version:**
- All phases except Phase 9 (Marketplace Expansion)

### Key Points to Emphasize:

✅ **Technical Artists FIRST** in cross-team collaboration (Tyler asked for this)
✅ **Data-driven experiments** (double-blind testing shows rigor)
✅ **Working backward from root causes** (shows maturity)
✅ **Lasting organizational impact** (standards for future partners)
✅ **50% turnaround time improvement** (concrete metric)

### Flexibility:

**Watch for interviewer cues:**
- If they seem engaged → keep going chronologically
- If they interrupt with specific questions → answer, then offer to continue
- If they say "Great" or "Perfect" → offer to go deeper or move to their questions

**Offer choices:**
- "I can go deeper into [technical architecture / cross-team dynamics / challenges / ML models]—what would be most useful?"

---

## 🚀 YOU'VE GOT THIS!

**This is your strongest story. It's 100% true, fully verifiable, and demonstrates everything they're looking for:**

✅ **Cross-functional collaboration** (6 teams, especially technical artists)
✅ **AWS serverless architecture** (exactly their stack)
✅ **ML/AI in production** (SageMaker, custom models, inference endpoints)
✅ **Leadership** (led 8 engineers, coordinated across 6 teams, 15 countries)
✅ **Challenges + Solutions** (shows problem-solving)
✅ **Lasting impact** (org-wide standards)
✅ **Data-driven decision making** (experiments, metrics)

**30 minutes is actually the RIGHT amount of time for this story. There's so much depth here.**

**Go get it! 🎮🚀**

