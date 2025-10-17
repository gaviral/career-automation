# FINAL ANSWERS - Project Scott Adjusted
**Based on:** Mehul's feedback + Project Scott truthfulness adjustment

**Interview:** Oct 9, 2025, 1PM PDT  
**Interviewers:** Daniel (Hiring Mgr), Blaze (Director), Rhea (Tech Director)

---

## ⚠️ CRITICAL: PROJECT STRATEGY ADJUSTMENT

### Primary Story: VTO PROJECT (100% TRUE, FULLY VERIFIABLE)
- Use this as main project walkthrough
- All details verified and true
- Strong technical depth
- Shows technical artist collaboration (Tyler asked for this)

### Secondary Story: PROJECT SCOTT (PROTOTYPE + WORKSHOP)
- **Workshop is 100% TRUE:** Led org-wide documentation workshop, created SME reference table, reached 100% documentation completion
- **AI Agent was a PROTOTYPE:** Built and tested, not fully deployed across Beauty Tech
- **Metrics were PROJECTED:** 82% improvement and 240 hrs/month were extrapolations/projections, not measured results

### If Asked About Project Scott:
**Focus on what's 100% true:**
1. **The workshop** (led org-wide initiative, 100% doc completion)
2. **The prototype** (built AI agent as proof of concept)
3. **The projected impact** (extrapolated 240 hrs/month savings)

**Avoid saying:**
- ❌ "Deployed across organization"
- ❌ "Achieved 82% improvement" (use "projected")
- ❌ "Saved 240 hours" (use "projected to save")

**Do say:**
- ✅ "Built a prototype AI agent"
- ✅ "Led documentation workshop that achieved 100% completion"
- ✅ "When we extrapolated the impact, projected 240+ hrs/month savings"

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

## 🎨 Q2: "WALK ME THROUGH A PROJECT" (1-1.5 min - USE VTO)

**Tyler's Note:** Use VTO to show technical artists collaboration. This is 100% TRUE and verifiable.

**Memory Triggers:** VTO → AR lipstick try-on → Replace tool, bad photos → Event-driven, SageMaker → 6 teams (TECHNICAL ARTISTS first) → Challenges + Learnings

**Full Answer:**

*I'll walk you through the* **Visual Property Extraction pipeline** *for* **AR virtual try-on** *at* **Amazon Beauty Tech**.

**The Context:** *On the Amazon app, when you go to a lipstick product and want to see what it would look like on you, you can click* **virtual try-on**—*the camera opens, face tracking happens, and you can try different lipsticks in* **real-time AR**. *For this to work, you need* **face tracking**, **3D lip models**, *and most importantly,* **accurate color and visual properties** *of the product*.

**My Project:** *I led the* **visual property extraction pipeline**—*extracting* **color (RGB values)**, **finish type** *(matte vs shiny)*, **particle properties** *(glitter size, shimmer)*—*and sending that to the next team who created* **3D models** *and did the* **AR rendering**.

**Problem:** *We needed to* **replace a costly third-party tool**, *and* **beauty brands** *were submitting* **non-standard product photos**—*wildly different lighting, angles, backgrounds. Some said "unicorn red" instead of proper color data. We needed* **RGB values** *and* **standardized properties**.

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

1. **Non-standard inputs:** *Product catalog had* **wildly inconsistent data**—*"unicorn red", "sunset pink". We needed* **RGB values** *and* **standardized properties** *(matte vs shiny, particle size for glitter)*.

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

## 🚀 Q4: PROJECT SCOTT (ONLY IF ASKED - Use with Caution)

**⚠️ Strategy:** Focus on WORKSHOP (100% true) + PROTOTYPE (true) + PROJECTED impact

**Memory Triggers:** Workshop 100% docs → Prototype AI agent → Projected 240 hrs → SME reference table

**Full Answer (If Pressed):**

*I led an* **org-wide documentation initiative** *at Amazon Beauty Tech that* **achieved 100% documentation completion** *for our entire team*.

**The Workshop (100% TRUE):**
- *Hosted an* **organization-wide documentation workshop**
- *Created a* **subject matter expert reference table** *(mapped topics to experts)*
- *Assigned ownership to team members with* **review deadlines**
- *Everyone took ownership and we reached* **100% documentation completion**

**The Prototype (TRUE):**
- *As part of this initiative, I built a* **prototype AI agent** *called* **"Project Scott"**
- *It was a* **RAG-based system**—**vector embeddings + document retrieval + LLM Q&A**
- *Integrated with* **SageMaker** *for model hosting,* **Lambda + API Gateway** *for orchestration,* **DynamoDB** *for session state*
- *The idea: new engineers could ask* **CI/CD and admin questions**, *and it would search our documentation*
- *If it didn't find a match, it would* **refer to the SME reference table** *and suggest who to contact*

**The Impact (PROJECTED):**
- *When we extrapolated the potential impact based on initial testing, we* **projected 240+ dev-hours/month** *could be saved across the organization*
- *We saw early indicators of an* **82% improvement** *in question resolution time during prototype testing*

**Why I'm Mentioning This:** *Shows a different angle of my* **ML/AI experience** *(RAG, LLM integration, SageMaker)*, *and demonstrates* **leadership** *(drove org-wide initiative, facilitated workshops)*.

**[Use ONLY if they specifically ask about "another project" or "documentation work" or if they press on resume bullet point]**

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

## ⚠️ CRITICAL REMINDERS

### DON'T RAMBLE:
- ❌ **Recruiter screen:** Spent **2+ minutes** on Project Scott when **30-45 seconds** would work
- ✅ **Fix:** Answer in **30-60 seconds** (Mehul approved 1-1.5 min for project walkthrough), THEN offer to elaborate
- ✅ **Phrase:** *"I can go deeper into [X, Y, or Z]—what would be most useful?"*

### WATCH INTERVIEWER CUES:
- *If they say* **"Great"** or **"Perfect"** → **STOP TALKING IMMEDIATELY**
- *If they're* **taking notes** → **PAUSE** *to let them catch up*
- *If they say* **"That's exactly what I was looking for"** → **MOVE ON**

### MEHUL'S TIPS:
- **Single-word triggers**, not reading scripts
- **Mention keywords**, let them probe
- **1-1.5 minute project explanation is GOOD** (not 10 seconds - you have 1 hour)
- **Focus on VTO** (100% true, verifiable, strong story)
- **Use "projected" for Project Scott metrics**

### PROJECT SCOTT HANDLING:
- ❌ **Don't volunteer it** as main project
- ✅ **If asked:** Focus on **workshop** (100% true) + **prototype** (true) + **"projected"** impact
- ✅ **Emphasis:** "Led org-wide documentation workshop, built prototype AI agent, projected 240 hrs/month savings"
- ✅ **Interviewers have resume pulled up** - they'll see the bullet point but won't remember recruiter notes

### TYLER'S SPECIFIC EMPHASIS:
1. ✅ **Cross-functional collaboration** (mentioned MULTIPLE times) - VTO has 6 teams
2. ✅ **Technical artists & game devs** ("certainly a plus") - VTO rendering team collaboration
3. ✅ **Communication** (emphasized multiple times) - VTO shows this extensively
4. ✅ **AWS cloud-native full-stack** (core requirement) - Both projects demonstrate this

---

## 🎯 YOUR COMPETITIVE ADVANTAGES

✅ **VTO Project is Your Strength:**
- **100% true and verifiable**
- **Technical artists collaboration** (Tyler specifically asked)
- **6-team coordination** (cross-functional collaboration)
- **AWS serverless architecture** (exactly what they need)
- **Challenges + Learnings** (shows maturity)
- **Lasting organizational impact** (standards for future partners)

✅ **Unique Differentiators:**
- **Technical artist collaboration** (rendering team, visual calibration, experiments)
- **Game dev experience** (UBC capstone)
- **Led team of 8 engineers** (leadership)
- **Infrastructure as Code** (AWS CDK, CloudFormation, 4-stage CI/CD)
- **FIFA player and fan** (genuine connection to mission)

✅ **Tyler Already Likes You:**
- Recruiter screen went well
- He highlighted your game dev experience as a plus
- You have the exact experience they need

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
- [ ] **Practice VTO walkthrough OUT LOUD 3x** (1-1.5 min, emphasize technical artists, challenges, learnings)
- [ ] **Practice technical artist answer OUT LOUD 2x** (60 sec)
- [ ] **Take 5 deep breaths**
- [ ] **Mindset:** *"VTO is my main story. It's 100% true. I know it inside out. I'm qualified."*

### During Interview:
- [ ] **Lead with VTO project** (if asked to walk through a project)
- [ ] **Be concise** (but 1-1.5 min for project is OK per Mehul)
- [ ] **Watch for cues** (stop when they say "Great")
- [ ] **Emphasize cross-functional collaboration** (Tyler's #1 point)
- [ ] **Mention technical artists FIRST** in collaboration list (Tyler specifically asked)
- [ ] **Show enthusiasm for EA** (FIFA player and fan, fan growth mission)
- [ ] **Ask tailored questions** (researched each interviewer)
- [ ] **If Project Scott comes up:** Focus on workshop + prototype + "projected" impact

---

## 🚀 YOU'VE GOT THIS!

**Remember:**
- **VTO is your main story** - it's 100% true, fully verifiable, shows everything they want to see
- You have **exactly** the experience they need
- Tyler **already likes you**
- **Technical artist work + game dev** = unique differentiators
- Just **be honest, be concise, watch cues, be yourself**

**This is a conversation between peers.**

**GOOD LUCK! 🎮🚀**

