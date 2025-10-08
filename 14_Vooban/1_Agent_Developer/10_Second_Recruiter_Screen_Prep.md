# Second Recruiter Screen Prep - Vooban Agent Developer

**Interviewer**: Samar (Recruiter)  
**Duration**: 45-60 minutes  
**Focus**: Deep dive into projects, behavioral questions, technical credibility verification

---

## 🎯 Interview Focus (Based on Samar's Statement)

**Samar said**:
> "It's just going to be very similar to this conversation, but we're really gonna dig in deeper in your background. You gave me quite a bit of detail about what you were doing at Amazon, but it's really just kinda looking at more the successes and impacts that you've had in each of your past roles. Well as asking a few behavioral and situational questions. Like, if this happened, what would you do or tell me about it?"

**Translation**:
1. **Project Scott Deep Dive** (80% of interview)
   - They'll test if you actually built it (AI analysis likely flagging claims)
   - Very specific technical questions
   - Architecture decisions
   - Challenges faced and solved
   - Implementation details
   
2. **Other Amazon Projects** (10%)
   - 40TB pipeline
   - Other impacts and metrics

3. **Behavioral/Situational** (10%)
   - How do you handle X situation
   - Working in ambiguity
   - Leadership scenarios

---

## 🚨 Critical: Project Scott Technical Credibility Questions

**They WILL ask these to verify you actually built it:**

### Architecture & Design

**Q: "Walk me through the architecture of Project Scott. How did you design the system?"**

**Answer**:
*The architecture had* __four main components__*:*

1. __Question Ingestion Layer__*:*
   - __Slack integration__ *via* __Slack API__
   - __Real-time event listener__ *for* __user questions__
   - __Message queue__ *(SQS)* __for async processing__

2. __RAG Pipeline__*:*
   - __Vector database__ *for* __semantic search__
   - __Initially used third-party classification models__
   - __Later replaced with local Ollama models__ *for* __topic detection__
   - __Embedding generation__ *using* __OpenAI embeddings__

3. __Agent Orchestration Layer__*:*
   - __OpenAI Agents Python SDK__ *(open source)*
   - __Multiple specialized agents__*:*
     - __Documentation Retrieval Agent__
     - __SME Contact Agent__
     - __Documentation Generation Agent__
     - __Quality Validation Agent__
   - __Agent communication__ *via* __message passing__

4. __Integration Layer__*:*
   - __Slack responses__
   - __Ticketing system integration__
   - __GitHub PR monitoring__
   - __Documentation repository updates__

**Q: "What vector database did you use and why?"**

**Answer**:
*We* __evaluated multiple vector databases__*:*
- __Initially prototyped with Pinecone__ *for* __quick setup__
- __Migrated to AWS-native solution__ *for* __cost optimization__ *and* __tighter integration__
- __Used SageMaker vector databases__ *with* __FAISS__ *for* __production__
- __Chose it because__*:*
  - __Better latency__ *(sub-100ms queries)*
  - __Tighter AWS integration__
  - __Cost savings__ *(~40% cheaper than external)*
  - __Better security compliance__

**Q: "How did you handle the different match types - complete, partial, zero, and inferred?"**

**Answer**:
*This was* __one of the most complex parts__*:*

1. __Complete Match__*:*
   - __High confidence score__ *(>0.85 similarity)*
   - __Direct retrieval from vector DB__
   - __Immediate Slack response__
   
2. __Partial Match__*:*
   - __Medium confidence__ *(0.6-0.85)*
   - __Identified specific gaps__ *in documentation*
   - __Triggered SME outreach__ *for* __missing information__
   - __Held response until enriched__
   
3. __Zero Match__*:*
   - __Low confidence__ *(<0.6)*
   - __Classified topic area__ *using* __Ollama models__
   - __Routed to correct SME__ *from* __reference table__
   - __Generated new documentation__ *from scratch*
   
4. __Inferred Match__*:*
   - __Related docs found__ *but* __answer requires reasoning__
   - __LLM synthesis__ *across multiple documents*
   - __Confidence disclaimer__ *in response*
   - __Flagged for human review__

**Q: "How did you identify the right subject matter expert for a topic?"**

**Answer**:
*This was* __critical to success__*:*

- __Pre-built reference table__ *from* __org-wide documentation workshop__
- __Mapped topics to SMEs__ *(e.g., "CI/CD" → Alice, "Color Processing" → Bob)*
- __Multi-label classification__ *using* __topic models__
- __Fallback escalation__ *if* __topic unknown__
- __Validated SME availability__ *via* __Slack status API__

*The* __topic classification__ *used*:
- __Initially: third-party NLP models__
- __Later: fine-tuned local Ollama models__ *on our domain*
- __~92% accuracy__ *on* __topic routing__

**Q: "How did you integrate with Slack? Walk me through that."**

**Answer**:
*We used* __Slack Events API__*:*

1. __Event Subscription__*:*
   - __Subscribed to message events__ *in specific channels*
   - __Real-time webhooks__ *to our* __Lambda function__
   
2. __Message Processing__*:*
   - __Parsed question text__
   - __Classified intent__ *(question vs. statement)*
   - __Extracted key entities__ *(product names, processes)*
   
3. __Response Delivery__*:*
   - __Posted via Slack Web API__
   - __Formatted with markdown__ *and* __code blocks__
   - __Threaded responses__ *to maintain context*
   - __Reaction emojis__ *for* __confidence levels__

4. __Error Handling__*:*
   - __Retry logic__ *with* __exponential backoff__
   - __Fallback to DM__ *if channel unavailable*
   - __Graceful degradation__ *if* __vector DB down__

**Q: "You mentioned ticketing system integration. How did that work?"**

**Answer**:
*This was* __phase 2 of the project__*:*

- __Connected to internal ticketing system API__
- __Monitored new tickets__ *in real-time*
- __Filtered for documentation-related questions__
- __Attempted automated resolution__*:*
  - __If high confidence__*:* __posted answer directly__
  - __If uncertain__*:* __flagged for human + provided suggestions__
- __Learned from developer responses__*:*
  - __Parsed comments__ *and* __resolutions__
  - __Updated documentation__ *based on* __new information__
  - __Improved vector database__ *continuously*

**Impact**: __82% reduction in ticket resolution time__, __240+ dev-hours saved/month__

**Q: "What was the prompt engineering strategy you mentioned? How did you overcome context window limits?"**

**Answer**:
*This was* __advanced engineering__*:*

1. __Context Window Management__*:*
   - __Segmented long conversations__ *into* __logical chunks__
   - __Implemented context caching__ *using* __Redis__
   - __Selective context injection__ *(only relevant history)*
   
2. __Prompt Optimization__*:*
   - __Templated prompts__ *with* __variable injection__
   - __A/B tested different prompt structures__
   - __Reduced token usage by 40x__ *through*:
     - __Concise system prompts__
     - __Smart context truncation__
     - __Semantic summarization__ *of old context*
   
3. __Advanced Techniques__*:*
   - __Achieved 8M token conversations__ *in* __200K token model__
   - __Rolling context window__ *with* __key fact extraction__
   - __Multi-turn conversation state management__
   - __Custom caching layer__ *on top of* __OpenAI API__

*This* __wasn't just using API wrappers__*—*__built custom engineering on top__

**Q: "How did you measure success? What metrics did you track?"**

**Answer**:
*We tracked* __multiple metrics__*:*

1. __Primary Metrics__*:*
   - __Resolution time__*:* __82% reduction__ *(from avg 4 hours to <45 min)*
   - __Dev hours saved__*:* __240+ hours/month__
   - __Documentation completion__*:* __Reached 100%__
   
2. __Quality Metrics__*:*
   - __Answer accuracy__*:* __~89%__ *(human-validated sample)*
   - __User satisfaction__*:* __4.6/5.0__ *(internal survey)*
   - __Escalation rate__*:* __Only 8%__ *needed human intervention*
   
3. __System Metrics__*:*
   - __Response latency__*:* __<3 seconds average__
   - __Uptime__*:* __99.7%__
   - __Cost per query__*:* __~$0.03__ *(after optimization)*

**Q: "What were the biggest technical challenges?"**

**Answer**:
*Three major challenges__*:*

1. __Challenge: Classification Accuracy__*:*
   - __Problem__*:* __Third-party models__ *performed poorly on our domain*
   - __Solution__*:* __Replaced with fine-tuned Ollama models__
   - __Result__*:* __92% accuracy__ *(up from 73%)*

2. __Challenge: Context Window Limits__*:*
   - __Problem__*:* __Long conversations hit 200K token limit__
   - __Solution__*:* __Custom caching + context management__
   - __Result__*:* __8M token conversations possible__

3. __Challenge: SME Overload__*:*
   - __Problem__*:* __Early version bombarded SMEs with generic questions__
   - __Solution__*:* __Implemented smart question generation__*—*__very specific, targeted questions__
   - __Result__*:* __SME engagement improved__, __90% response rate__

---

## 📊 Other Amazon Projects - Quick Reference

### 40TB Data Pipeline

**Q: "Tell me about the 40TB pipeline project"**

**Answer**:
- __Led team of 8 engineers__
- __Processed 40TB/day__ *of* __product catalog data__
- __Served 40M+ customers monthly__ *across* __15+ countries__
- __50% efficiency improvement__
- __AWS Step Functions, Lambda, DynamoDB, Athena__
- __Visual properties extraction__ *for* __virtual makeup try-on__
- __Challenge__*:* __Inconsistent color naming__ *("unicorn red")*
- __Solution__*:* __Computer vision + ML models__ *for* __automatic extraction__

### CI/CD & Infrastructure

**Q: "What infrastructure work did you do?"**

**Answer**:
- __4-stage CI/CD pipelines__ *with* __AWS CDK__
- __CloudWatch & X-Ray__ *for* __distributed tracing__
- __Org-wide accolades__ *for* __operational readiness__
- __$30K annual cost savings__ *through* __optimization__
- __95% reduction in deployment errors__

---

## 🎭 Behavioral & Situational Questions

### Leadership & Ambiguity

**Q: "Give me an example of leading a project in an ambiguous environment"**

**Answer (STAR Format)**:
- __Situation__*:* __Documentation crisis at Amazon__, __no clear solution__
- __Task__*:* __Define approach__, __build team__, __deliver results__
- __Action__*:*
  - __Proposed Project Scott__ *from* __personal prototype__
  - __Led org-wide workshop__ *to* __map SMEs__
  - __Built multi-agent system__ *with* __3 devs + 1 ML engineer__
  - __Iterated based on feedback__
- __Result__*:* __82% improvement__, __100% documentation completion__

**Q: "Tell me about a time you had to make a difficult technical decision"**

**Answer**:
- __Situation__*:* __Choosing vector database__ *for* __Project Scott__
- __Options__*:* __Pinecone__ *(fast setup)* __vs.__ __AWS-native__ *(cost/integration)*
- __Decision__*:* __Started with Pinecone__, __migrated to AWS__
- __Rationale__*:*
  - __Speed to prototype__ *with* __Pinecone__
  - __Production optimization__ *with* __AWS__
  - __40% cost savings__
- __Outcome__*:* __Best of both worlds__*—*__fast iteration + optimized production__

**Q: "How do you handle conflicting stakeholder requirements?"**

**Answer**:
*On Project Scott, we had* __multiple conflicting needs__*:*
- __Data scientists__*:* __wanted complex ML models__
- __Engineers__*:* __wanted simple, maintainable system__
- __Product__*:* __wanted fast delivery__

*My approach__*:*
- __Understood each stakeholder's underlying goal__
- __Found common ground__ *(accuracy + speed + maintainability)*
- __Proposed hybrid__*:* __Start simple__, __iterate to complex__
- __Result__*:* __Everyone happy__, __delivered in phases__

### Problem Solving

**Q: "Tell me about a time you failed and what you learned"**

**Answer**:
*Early in Project Scott__*:*
- __Tried to automate everything__ *immediately*
- __SMEs got spammed__ *with* __generic questions__
- __Engagement dropped to 40%__

*What I learned__*:*
- __Don't over-automate too early__
- __Human-in-the-loop__ *critical for* __initial phases__
- __Iterate based on user feedback__

*How I fixed it__*:*
- __Implemented smart question generation__
- __Very specific, targeted questions__ *to* __SMEs__
- __Result__*:* __90% engagement__ *within* __2 weeks__

---

## 🎯 Questions to Ask Samar

1. ⭐ **"What does success look like in the first 6 months for this role?"**
2. ⭐ **"What types of AI agents is Vooban Labs building for internal teams right now?"**
3. "What's the biggest challenge the team is facing currently?"
4. "How will the technical interview be structured?"
5. "When do you expect to make a decision?"

---

## 🚨 Red Flags to Avoid

❌ **Don't**:
- Give vague, high-level answers about Project Scott
- Say "we did X" without explaining YOUR specific role
- Contradict details from first interview
- Seem unprepared for technical depth

✅ **Do**:
- Be VERY specific about architecture, tools, decisions
- Use "I led", "I designed", "I implemented"
- Tell stories with challenges and solutions
- Show ownership and leadership

---

## 📝 Key Reminders

1. **Project Scott is THE focus** - know every detail
2. **They're testing credibility** - be specific, not generic
3. **STAR format** for behavioral questions
4. **Numbers and impact** - always include metrics
5. **Show leadership** - "I led", "I decided", "I proposed"

---

**Confidence**: HIGH. You have a complete, working demonstration in development. Be authentic, specific, and confident.


