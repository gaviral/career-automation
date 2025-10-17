# FINAL ANSWERS - Tyler-Focused Version
**Based on:** Tyler's specific requests + Recruiter call insights + Mehul's tips

**Interview:** Oct 9, 2025, 1PM PDT  
**Interviewers:** Daniel (Hiring Mgr), Blaze (Director), Rhea (Tech Director)

---

## 🎯 WHAT TYLER SPECIFICALLY ASKED FOR (From File 10)

### Tyler's Exact Words:

1. **"Cross-functional collaboration is a BIG PART of this role"**
   - "They need someone who honestly, kind of enjoys that"
   - "Working with folks in other orgs, other parts of the org"

2. **"Talk about working with tech artists and game devs"**
   - "While it's not a requirement, it's certainly a PLUS"
   - "I would encourage you to talk about that"
   - "That would be beneficial"

3. **"Technical background in cloud-based full stack development, AI solutions"**
   - AWS heavily emphasized
   - ML models, web apps
   - Python, JavaScript

4. **"Communication and collaboration"**
   - Emphasized multiple times
   - Standard team questions
   - Examples of working in teams

---

## 💬 Q1: "TELL ME ABOUT YOURSELF" (60-90 sec)

**Memory Triggers:** Amazon 5yrs → 8 engineers → 40TB 40M → Python AWS → Technical artists → FIFA fan → Excited EA

**Full Answer:**

*I'm a* **full-stack software engineer** *with* **5 years at Amazon** *specializing in* **cloud-native ML applications on AWS**.

*At* **Amazon Beauty Tech**, *I* **led a team of 8 engineers** *building* **AI-powered systems** *that processed* **40TB/day**, *serving* **40M+ customers** *across* **15 countries**.

*My technical foundation is* **Python** *and* **AWS serverless architecture**—**Lambda, SageMaker, API Gateway, DynamoDB**—*and* **Infrastructure as Code** *with* **CloudFormation**.

*What I really enjoy is* **cross-functional collaboration**. *I've worked extensively with* **technical artists**, **designers**, **data scientists**, **product managers**. *At UBC, I led a* **game development capstone** *where I was the* **bridge between engineers and creative teams**—*learned early that we speak different languages, and I love translating between technical and creative worlds*.

*I'm excited about EA because:*
- **Perfect technical match**—*exactly the stack I've been building with for 5 years*
- *I genuinely* **enjoy working with technical artists and content creators**
- *As a* **FIFA player and fan myself**, *I resonate with* **creating stellar fan experiences**—*I've been a fan, now I want to help create more fans*

**[STOP. Breathe. Wait for response.]**

---

## 🎨 Q2: "WALK ME THROUGH A PROJECT" (45 sec core)

**Tyler's Note:** He already heard Project Scott and was impressed. **Use VTO to show technical artists collaboration.**

**Memory Triggers:** VTO → Replace tool, bad photos → Event-driven, SageMaker → 6 teams (TECHNICAL ARTISTS first) → 40TB, standards

**Full Answer:**

*I'll walk you through the* **Visual Property Extraction pipeline** *for* **AR virtual try-on** *at* **Amazon Beauty Tech**.

**Problem:** *We needed to* **replace a costly third-party tool**, *and* **beauty brands** *were submitting* **non-standard product photos**—*wildly different lighting, angles, backgrounds*—*causing* **inconsistent data quality** *for our AR try-ons*.

**My Role:** **Technical lead** *for the* **end-to-end pipeline**. *I owned* **architecture, planning, execution**, *consulting a senior engineer for design review*.

**Architecture:** **Event-driven pipeline**—**Step Functions + Lambda** *triggered by product catalog changes*, **SageMaker Ground Truth** *for* **data labeling** *(bounding boxes, color extraction)*, **API Gateway + Lambda** *orchestration*, **DynamoDB** *for state*, **S3** *for artifacts*, **AWS CDK + CloudFormation** *for Infrastructure as Code*, **4-staged CI/CD**, **CloudWatch + X-Ray** *for observability*.

**Collaboration—This is the Key Part:**

*I coordinated across* **6 different teams**:

1. **Technical artists on the rendering team**—*Regular syncs on* **visual calibration** *and* **color accuracy** *for AR. We ran* **double-blind experiments** *with people of different genders and races to validate that our* **RGB values** *looked realistic on different* **skin tones** *in AR*.

2. **Designers**—*UX collaboration, visual property standards*

3. **Data scientists**—*Model training for bounding boxes and color extraction*

4. **Product managers**—*Requirements gathering, working backward from product vision*

5. **External 3D asset creation team**—*Guided overall direction while respecting their expertise*

6. **Beauty brand bridge teams**—*Guided standardization of photo submissions*

**Impact:**
- ✅ **Replaced the third-party tool**
- ✅ **Established org-wide standards** *for future beauty brand partners*
- ✅ **High data quality** *validated through our user experiments*
- ✅ *This fed into the larger* **Beauty Tech data lake** *processing* **40TB/day**

**Key Challenges:**

1. **Non-standard inputs:** *Product catalog had* **wildly inconsistent data**—*some said "unicorn red", others had proper color names. We needed* **RGB values** *and* **standardized properties** *(matte vs shiny, particle size for glitter)*.

2. **Cross-team alignment:** *Six different teams with* **different priorities**—*beauty brands wanted fast onboarding, data scientists needed high-quality training data*.

3. **Scale:** *Had to process the* **entire Amazon Beauty catalog**—*millions of products, varying image quality*.

**How I Solved Them:**

1. **Worked backward from the problem:** *Instead of just building better extraction algorithms, I worked with* **beauty brand bridge teams** *to* **improve photo submission standards** *at the source*. *Created* **standardized forms** *and* **naming conventions**.

2. **Data-driven alignment:** *Brought* **experimental results** *to team meetings—showed that* **low-quality photos = poor AR realism = customer churn**. *This helped teams prioritize quality over speed*.

3. **Phased approach:** **Phase 1** *accepted current submissions with manual review,* **Phase 2** *improved standards,* **Phase 3** *full automation*. *This balanced urgency with quality*.

**Key Learning:**

*The biggest learning was* **don't just solve the immediate technical problem—work backward to address root causes**. *In this case, that meant* **improving the data at the source** *(photo submissions)* *rather than only building better extraction algorithms*. *This approach created* **lasting organizational impact** *(standards adopted for future partners)* *rather than just a one-time technical fix*.

**[STOP. Offer: "I can go deeper into technical architecture, the cross-team collaboration dynamics, or any of these challenges—what would be most useful?"]**

---

## 🎮 Q3: "TELL ME ABOUT WORKING WITH TECHNICAL ARTISTS" (Tyler specifically asked)

**Memory Triggers:** Rendering team → Visual calibration → RGB values, skin tones → Double-blind experiments → Data-driven → UBC game dev

**Full Answer:**

*I have two strong examples.*

**Amazon Beauty Tech—VTO Project:**

*On the VTO project, I worked closely with* **technical artists** *on the* **rendering team**. *Their focus was* **real-time AR rendering** *and* **face tracking**.

**The Challenge:** *Ensuring that the* **color values** *we extracted from product images* **looked realistic** *when rendered on* **different skin tones in AR**.

**My Approach:**
- *Scheduled* **regular syncs** *specifically for* **visual calibration** *discussions*
- *Conducted* **data-driven experiments**—**double-blind tests** *with people of different* **genders and races** *wearing virtual lipsticks in our demo app*
- *This gave us* **real data** *to align on what "realistic" meant* **technically vs artistically**
- *I brought* **experimental results** *to our discussions rather than just talking about RGB values*
- *Respected their* **expertise** *in visual rendering—they understood realism, I ensured our pipeline delivered the right data*

**Result:** *We achieved* **color accuracy standards** *that balanced* **technical precision** *with* **visual realism**, *validated through our user testing*.

**UBC Game Development Capstone:**

*At University of British Columbia, I led a* **game development capstone** *where I was* **technical lead** *and* **bridge** *between* **engineers and game designers/artists**.

**Key Learning:** *We speak* **different languages**—*designers care about* **player experience** *and* **aesthetics**, *engineers care about* **frame rates** *and* **memory**. *I became the* **translator**, *ensuring* **design visions** *were technically feasible and technical constraints were understood creatively*.

**Why This Matters for EA:**

*I genuinely* **enjoy** *this type of collaboration*. *It's challenging but rewarding to* **bridge technical and creative worlds**, *and I know from Tyler that this is a* **big part of this role**.

**[STOP. Wait for follow-up.]**

---

## 🚀 Q4: PROJECT SCOTT (If They Ask for Different Example)

**Memory Triggers:** AI agent → Documentation Q&A → Talk to Project Scott → SME escalation → 82%, 240 hrs, 100% docs

**Full Answer:**

*Another strong example is* **Project Scott**, *an* **AI agent system** *I built for answering team questions from* **internal documentation**.

**Problem:** **New engineers** *had tons of technical questions about* **CI/CD, admin, infrastructure**. **Documentation was scattered**, **SMEs kept answering the same questions**.

**Solution:** *Built a* **RAG-based AI agent**:
- **Vector embeddings + document retrieval + LLM-powered Q&A**
- *Named it* **"Project Scott"** *to anthropomorphize it and encourage adoption*
- *If the AI couldn't find an answer, it* **automatically escalated to subject matter experts**, *then* **fed their responses back into the documentation**
- **Integrated with internal ticketing system**

**Architecture:** **API Gateway + Lambda**, **SageMaker** *for model hosting*, **DynamoDB** *for session state*, **S3** *for documents*, **CloudWatch/X-Ray** *for observability*, **AWS CDK + CloudFormation**.

**Impact:**
- ✅ **82% improvement** *in resolution time*
- ✅ **240+ dev-hours/month saved** *across the organization*
- ✅ **100% documentation coverage**—*I led an org-wide documentation workshop*
- ✅ **High adoption rate**—*became the go-to resource*

**Why I'm Mentioning This:** *Shows a different angle of my* **full-stack ML experience**, *and demonstrates* **leadership** *(drove org-wide adoption, led workshops)*.

**[Use this if asked: "Tell me about another ML project" or "AI agents/LLMs experience"]**

---

## 💼 BEHAVIORAL QUESTIONS

### "Describe receiving difficult feedback"

**Memory Triggers:** VTO architecture review → Senior engineer → Won't scale → Felt defensive → Redesigned → 40TB scale → Now proactive

**Answer:**

**Situation:** *Early in the VTO project, I proposed my initial architecture to a* **senior engineer** *for review*.

**Feedback:** *He said,* **"This won't scale beyond small volume. Your Step Functions orchestration will timeout with large batches. You need to rethink data partitioning and parallel processing."**

**Initial Reaction:** *I felt defensive—I'd spent* **3 days** *on that design*. *But I took a step back.*

**Action:**
- *Scheduled a* **follow-up meeting** *to understand his concerns deeply*
- *Asked clarifying questions about* **expected scale**—*turned out it was* **10x** *what I'd designed for*
- *Acknowledged the gaps in my assumptions*
- **Redesigned** *with* **parallel processing**, *optimized* **Lambda memory allocation**, *implemented* **DynamoDB caching**

**Result:**
- *The final architecture* **scaled to 40TB/day** *serving* **40M+ users**
- **Strengthened my relationship** *with the senior engineer*
- *Now I* **proactively seek architecture reviews** *before full implementation*

**Learning:** **Feedback is a gift**. *Senior engineers have* **context I don't**. *Now I always ask upfront:* **"What scale should this handle?"**

---

### "Handling competing priorities from different teams"

**Memory Triggers:** Beauty brands vs data scientists → Fast onboarding vs quality data → Brought data showing impact → Phased approach → Both bought in

**Answer:**

**Situation:** *On the VTO project,* **beauty brand bridge teams** *wanted* **faster onboarding** *(pressure from executives)*, *but* **data scientists** *needed* **higher quality training data** *(couldn't train good models without it)*.

**Conflict:**
- *Bridge teams wanted to* **accept any photo submissions** *to speed onboarding*
- *Data scientists wanted* **strict photo standards** *to ensure model accuracy*

**My Approach:**
- *Facilitated a meeting with both teams to* **align on priorities**
- *Brought* **data**: *Showed experimental results proving* **low-quality photos = poor AR realism = bad customer experience = churn**
- *Proposed a* **phased approach**:
  - **Phase 1:** *Accept current submissions, manual review bottleneck*
  - **Phase 2:** *Work with beauty brands to improve submission standards*
  - **Phase 3:** *Automated pipeline with high-quality inputs*

**Communication:**
- **Regular status updates** *to both teams*
- **Documented decisions** *and trade-offs*
- **Managed expectations** *on timelines*

**Result:**
- *Both teams bought in*
- **Photo standards** *established that beauty brands adopted*
- **Data quality improved** *over time*
- *No compromise on* **customer experience**

---

### "Effective communication with non-technical stakeholders"

**Memory Triggers:** PMs asking "speed it up" → Visual demos → User impact framing → Analogies → Trade-offs → Bi-weekly dashboards

**Answer:**

**Challenge:** **Product managers** *didn't understand why* **color extraction** *took "so long"*. *They kept asking,* **"Can't you just speed it up?"**

**My Approach:**

1. **Visual Demonstrations:** *Showed* **side-by-side examples** *of* **"fast but inaccurate"** *vs* **"slower but accurate"** *color extraction in AR try-on*

2. **User Impact Framing:** *Explained in terms they cared about:* **"Fast but wrong colors = customers buy wrong shade = returns = bad reviews"**

3. **Analogies:** *"It's like photo editing—you can apply a filter in 1 second, but* **professional color grading** *takes time for realism."*

4. **Trade-off Transparency:** *Gave* **options** *with* **clear trade-offs** *(speed vs accuracy vs cost)*

5. **Regular Updates:** **Bi-weekly syncs** *with* **dashboards** *showing progress, not just technical jargon*

**Result:**
- *PMs* **understood the trade-offs**
- *Stopped pushing for* **speed over quality**
- **Advocated for realistic timelines** *with leadership*

**Learning:** *Non-technical stakeholders care about* **user impact** *and* **business outcomes**. **Translate technical constraints** *into their language*.

---

## 🙋 QUESTIONS TO ASK (Tailored to Each Interviewer)

### For Daniel (Hiring Manager - Madden NFL veteran):
1. *"Can you tell me more about the* **day-to-day responsibilities** *in the first 90 days? Tyler mentioned learning the* **Frostbite codebase**—*what does that ramp-up look like?"*

2. *"What does* **success look like** *for this role in the* **first 6 months**?"*

3. *"You've worked on* **Madden NFL** *for many years—are there any* **technical challenges** *from game development infrastructure that you've found particularly interesting?"* *(Shows you researched him, genuine curiosity)*

### For Blaze (Director - Global Operations):
1. *"You oversee* **Production Operations & Technology** *across EA's global studios—what are the* **biggest operational challenges** *in coordinating across so many teams?"*

2. *"How do you see* **AI/ML evolving** *in EA's content production workflows over the next few years?"*

3. *"Tyler mentioned* **cross-functional collaboration** *is a big part of this role—what does* **effective collaboration** *look like on your team? Any recent examples?"*

### For Rhea (Technical Director - Online Development):
1. *"What's the* **technical architecture** *for EA's online services? Are there specific* **scalability challenges** *you're tackling at EA's scale?"*

2. *"How does the team balance* **rapid experimentation** *with maintaining* **production stability**?"*

3. *"What* **AWS services or cloud technologies** *is the team most excited about adopting or expanding use of?"*

### General (If Time):
1. *"What do you* **enjoy most** *about working at EA?"*
2. *"How does the team* **stay current** *with rapidly evolving* **AI/ML technologies**?"*

---

## ⚠️ CRITICAL REMINDERS (From File 11 - Learning Points)

### DON'T RAMBLE:
- ❌ **Recruiter screen:** Spent **2+ minutes** on Project Scott when **30-45 seconds** would work
- ✅ **Fix:** Answer in **30-60 seconds**, THEN offer to elaborate
- ✅ **Phrase:** *"I can go deeper into [X, Y, or Z]—what would be most useful?"*

### WATCH INTERVIEWER CUES:
- *If they say* **"Great"** or **"Perfect"** → **STOP TALKING IMMEDIATELY**
- *If they're* **taking notes** → **PAUSE** *to let them catch up*
- *If they say* **"That's exactly what I was looking for"** → **MOVE ON**

### MEHUL'S TIPS (From File 25):
- **Single-word triggers**, not reading scripts
- **Mention keywords**, let them probe
- **Don't force it** if you forget something—smart interviewers will infer, or bring it up in next answer
- **Sound conversational**, not rehearsed

### TYLER'S SPECIFIC EMPHASIS (From File 10):
1. ✅ **Cross-functional collaboration** (mentioned MULTIPLE times)
2. ✅ **Technical artists & game devs** ("certainly a plus", "encourage you to talk about")
3. ✅ **Communication** (emphasized multiple times)
4. ✅ **AWS cloud-native full-stack** (core technical requirement)

---

## 🎯 YOUR COMPETITIVE ADVANTAGES

✅ **Exactly what Tyler asked for:**
- **Cross-functional collaboration:** 6 teams on VTO, including technical artists
- **Game dev experience:** UBC capstone, natural fit
- **AWS/ML cloud-native:** 5 years, extensive experience
- **Communication skills:** Proven across technical and creative teams

✅ **Unique differentiators:**
- **Technical artist collaboration** (rendering team, visual calibration, experiments)
- **Led team of 8 engineers** (leadership)
- **Impressive metrics:** 82%, 240 hrs, 100% docs, 40TB, 40M users
- **Infrastructure as Code** (AWS CDK, CloudFormation, 4-stage CI/CD)
- **FIFA player** (genuine fan, understand customer perspective)

✅ **Tyler already likes you:**
- Recruiter screen went well
- He specifically highlighted your game dev experience as a plus
- He emphasized cross-functional work, which is your strength

---

## 📋 FINAL PRE-INTERVIEW CHECKLIST

### 30 Minutes Before:
- [ ] **Test video/audio setup**
- [ ] **Good lighting** (face clearly visible)
- [ ] **Quiet space** (phone on silent)
- [ ] **Water nearby**
- [ ] **This file open** (for quick glances at memory triggers)
- [ ] **Resume open**
- [ ] **Job description open**

### Mental Prep:
- [ ] **Practice "Tell me about yourself" OUT LOUD 3x** (60-90 sec, time it)
- [ ] **Practice VTO walkthrough OUT LOUD 2x** (45 sec, emphasize technical artists FIRST)
- [ ] **Practice technical artist answer OUT LOUD 1x** (60 sec)
- [ ] **Take 5 deep breaths**
- [ ] **Mindset:** *"I'm qualified. I've done this exact work. This is a conversation between peers."*

### During Interview:
- [ ] **Be concise** (30-60 sec answers)
- [ ] **Watch for cues** (stop when they say "Great")
- [ ] **Emphasize cross-functional collaboration** (Tyler's #1 point)
- [ ] **Mention technical artists naturally** (Tyler specifically asked)
- [ ] **Show enthusiasm for EA** (FIFA player, fan growth mission)
- [ ] **Ask tailored questions** (researched each interviewer)

---

## 🚀 YOU'VE GOT THIS!

**Remember:**
- You've built **exactly** what they need
- Tyler **already likes you**
- You have **unique differentiators** (technical artist work, game dev)
- Just **be concise, watch cues, be yourself**

**This is a conversation, not an interrogation.**

**GOOD LUCK! 🎮🚀**

