# Day-of-Interview Cheat Sheet
**Read 30 minutes before interview** | **Print or have on second screen**

---

## ⚡ TOP 5 TECHNICAL CONCEPTS (5 min review)

### 1. **Sorting Algorithms**
- **Merge Sort:** O(n log n) always, stable, O(n) space → use when stability matters
- **Quick Sort:** O(n log n) avg, O(n²) worst, in-place → use when space limited
- **Python default (Tim Sort):** Best for real-world data (partially sorted)
- **VTO:** Used Athena ORDER BY for 40TB data (external sorting)

### 2. **Factory Pattern**
```python
class Factory:
    _registry = {'sagemaker': SageMakerModel, 'local': LocalModel}
    
    @classmethod
    def create(cls, type, **kwargs):
        return cls._registry[type](**kwargs)
```
- **VTO:** Could have used this for data source switching (Athena, Kinesis, vendor API)

### 3. **Step Functions Error Handling**
- **Retry:** `BackoffRate: 2.0` → 1s, 2s, 4s, 8s (exponential)
- **Catch:** Route errors to specific handlers vs fail entire workflow
- **Parallel:** Isolate failures per branch (format fails ≠ logo fails)
- **VTO:** 3 retries for network, 1 for data quality, X-ray for debugging

### 4. **ML Deployment**
- **Batch (VTO):** SageMaker Batch Transform, S3 I/O, hours, $$ (Spot), catalog updates
- **Real-time:** Endpoint + API, milliseconds, $$$ (provisioned), customer-facing
- **Parameters:** Instance type, auto-scaling, env vars (threshold, batch size)

### 5. **DynamoDB Partition Key**
- High cardinality (many unique values)
- Even access (avoid hot partitions)
- **VTO:** `product_id` (millions) ✅ vs `category` (10) ❌
- Composite: `{marketplace}#{product_id}` for multi-region

---

## 🎯 TOP 3 VTO TALKING POINTS (2 min review)

### 1. **Scale & Impact**
> "Led team of 8 engineers building pipeline processing **40TB/day** serving **40M+ customers** across **15 countries**. Replaced expensive third-party with in-house ML solution achieving **93% success rate** with existing imperfect data."

### 2. **Technical Solution**
> "Designed serverless **Step Functions** architecture with **Lambda, Athena, SageMaker**. Key innovation: **Athena + Parquet** for cost-effective ETL vs expensive Kinesis streaming. Transitioned **human labelers → SageMaker endpoints** without pipeline changes (modular design)."

### 3. **Operational Excellence**
> "Amazon **ORR** (Operational Readiness Review): Exponential backoff, X-ray tracing, comprehensive logging. Worldwide expansion (**US → Japan → Europe → Asia**) with **zero late-stage scaling failures** due to upfront planning."

---

## 🚀 TOP 3 PROJECT SCOTT TALKING POINTS (1 min review)

### 1. **Problem & Solution**
> "Internal documentation gaps. Built **Slack-integrated AI assistant** using **RAG + Pinecone vector DB + LLMs**. When docs incomplete, automatically contacts **SMEs** with specific sub-questions, suggests updates (one-click)."

### 2. **Org Initiative**
> "**3 workshops**, everyone took documentation ownership (100% coverage goal). **Proactive agents** simulate new team members, find gaps before asked."

### 3. **Key Learning**
> "Don't build custom models. Use **OpenAI/Anthropic via Bedrock** or small models (**Ollama**). Focus on **prompt engineering** and **agentic handoff** frameworks."

---

## ❓ TOP 3 QUESTIONS TO ASK INTERVIEWERS (30 sec review)

1. **"What ML/AI projects are other EA teams working on that I might collaborate with?"**
   - Shows: Rhea's collaboration theme, curiosity, strategic thinking

2. **"What's the biggest technical challenge the team is facing right now?"**
   - Shows: Problem-solving orientation, eagerness to contribute

3. **"What does success look like in the first 90 days?"**
   - Shows: Goal-oriented, alignment-seeking, practical focus

---

## ✅ INTERVIEW EXECUTION CHECKLIST (30 sec review)

### For Every Question:
1. **Clarify** (1-2 min): Restate problem, ask constraints
2. **Approach** (2-3 min): Explain strategy before coding
3. **Narrate** (10-15 min): Think out loud, don't code silently
4. **Test** (3-5 min): Walk through examples, fix bugs
5. **Optimize** (2-3 min): Discuss improvements
6. **Connect** (1 min): "This reminds me of VTO when..."

### Red Flags to Avoid:
❌ Code immediately without clarifying  
❌ Silent coding (always narrate)  
❌ Give up on bugs  
❌ Ignore interviewer hints

### Green Flags to Show:
✅ Ask clarifying questions  
✅ Multiple approaches  
✅ Discuss trade-offs  
✅ Handle edge cases  
✅ Reference real experience  

---

## 💪 CONFIDENCE REMINDERS (1 min review)

### What Daniel Said:
> "I think that **you fit very well** on what we're looking for. We appreciate your time and your **clear and friendly way of explaining things**. Hope we see you again in **not a long time**."

### What Rhea Said:
> "That is a **very good answer**." (about your ORR explanation)

### What Blaze Said:
> "I have a lot of complaints about documentation internally." (Your Scott project solves this!)

### Your Advantages:
✅ **Exact stack match:** AWS serverless, ML pipelines, IaC  
✅ **Scale experience:** 40TB/day, 40M users, 15 countries  
✅ **Leadership:** Led 8 engineers, coordinated 6 teams  
✅ **Operational readiness:** ORR, X-ray, no failures  
✅ **Cutting-edge AI:** RAG, agentic frameworks, prompt engineering  
✅ **Game dev bonus:** Unity projects (Tyler said this helps)

### Remember:
🎮 **They already like you.** This is validation, not elimination.  
🎮 **Daniel coordinating difficulty** to ensure it's appropriate.  
🎮 **"Don't be shy"** - they said this 3+ times.  
🎮 **You're interviewing them too** (cultural fit).

---

## 🧠 ANSWER FRAMEWORKS (3 min review)

### Algorithm Question Framework:
1. **Clarify:** "What's the input size range? Space constraints?"
2. **Approach:** "I'll use X because Y. Time O(n log n), space O(n)."
3. **Code:** Write clean Python, explain variable names
4. **Test:** "Input [1,2,3] → Output [3,2,1]"
5. **Optimize:** "Could improve to O(n) by using hash table"
6. **Connect:** "In VTO, similar optimization with Athena queries..."

### Design Pattern Framework:
1. **Clarify:** "What model types? How is config provided?"
2. **Interface:** Abstract base class with common methods
3. **Implementations:** Concrete classes for each type
4. **Factory:** Registry + create method
5. **Benefits:** Open/closed, testability, flexibility
6. **Connect:** "VTO had similar pattern for data sources..."

### System Design Framework:
1. **Requirements (3-5 min):** Functional, scale, latency, constraints
2. **High-level (5-7 min):** Components, data flow, tech choices
3. **Deep Dive (10-15 min):** Focus on 1-2 components they're interested in
4. **Trade-offs (3-5 min):** Alternatives, scaling strategies, cost
5. **Connect:** "Similar to VTO architecture where..."

### ML Deployment Framework:
1. **Context:** "What model type? What scale?"
2. **Architecture:** Data → Training → Inference
3. **Deployment:** SageMaker endpoints, batch vs real-time
4. **Monitoring:** Accuracy, latency, drift detection
5. **Connect:** "VTO used batch for catalog, real-time for..."

---

## 🎬 FINAL PRE-INTERVIEW RITUAL (2 min)

### Physical:
1. Deep breath (4 sec in, 7 sec hold, 8 sec out) × 3
2. Power pose for 2 minutes (hands on hips, stand tall)
3. Hydrate (water ready, bathroom break done)
4. Tech check (camera, mic, internet, backup phone)

### Mental:
1. Visualize: See yourself confidently explaining VTO architecture
2. Affirmation: "I fit very well. I have the exact experience they need."
3. Excitement: Remember the Battlefield 6 launch energy from Rhea
4. Mission: Help EA build amazing content creation tools with AI

### Environment:
- Second screen with this cheat sheet
- Notebook + pen for diagrams/notes
- No distractions (phone silent, door closed)

---

## 🔥 ONE-SENTENCE MANTRAS

**Before interview:** "Daniel already said I fit very well. Now I show them why."

**During tough question:** "Clarify first. Think out loud. Reference VTO/Scott."

**After interview:** "I prepared thoroughly. I showed up authentically. I trust the process."

---

**YOU'VE GOT THIS. GO GET THAT OFFER. 🎮🚀**


