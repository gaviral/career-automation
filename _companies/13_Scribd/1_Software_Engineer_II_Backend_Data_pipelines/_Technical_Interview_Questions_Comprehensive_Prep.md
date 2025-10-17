# 🎯 TECHNICAL INTERVIEW - COMPREHENSIVE PREP QUESTIONS
## Software Engineer II (Backend + Data Pipelines) - Scribd
## SORTED BY PREPARATION IMPACT

---

## 📊 PREPARATION IMPACT LEGEND

- 🔥 **CRITICAL (95%+ probability)** - Practice until perfect
- ⭐ **HIGH (70-90% probability)** - Must prepare thoroughly  
- ✅ **MEDIUM (40-70% probability)** - Prepare solid examples
- 💡 **BONUS (10-40% probability)** - Nice to have if time permits

---

## 🔥 CRITICAL: DATA PIPELINE ARCHITECTURE (Practice Daily)

### Q1: Design a scalable metadata extraction pipeline for 250M documents
**Preparation Impact:** 🔥 CRITICAL  
**Probability:** 95%+ (This is literally their 2026 roadmap)

**What they're testing:**
- Large-scale distributed systems design
- Understanding of their actual problem
- AWS services knowledge (Lambda, SageMaker, S3, SQS)
- Cost optimization mindset
- LLM integration at scale

**Your answer should cover:**
1. **Ingestion layer:** S3 triggers → SQS → Lambda for fan-out
2. **Processing layer:** Step Functions orchestration, Lambda workers, batch processing
3. **LLM integration:** SageMaker endpoints, batch transform, cost optimization (your 40% approach!)
4. **Storage:** DynamoDB for metadata, S3 for raw/processed docs
5. **Monitoring:** CloudWatch, X-Ray for distributed tracing
6. **Scaling considerations:** 
   - Partition strategy (by document type, size, language)
   - Rate limiting for LLM APIs
   - Caching layer (ElastiCache) for repeated queries
   - Dead letter queues for failed processing
7. **Cost optimization:**
   - Spot instances for non-critical batch jobs
   - Lambda cold start optimization
   - S3 lifecycle policies
   - Your Python-first approach (40% cost reduction)

**Connect to your experience:**
- "At Amazon, I built a similar pipeline for 40TB/day product catalog data..."
- "The challenge of 250M × 27 pages = 6.5B images reminds me of our visual property extraction at scale..."

**Practice:** Draw this architecture 10+ times until you can do it smoothly in 15 minutes

---

### Q2: How would you optimize an expensive LLM pipeline processing millions of documents?
**Preparation Impact:** 🔥 CRITICAL  
**Probability:** 90%+ (Sachin was very interested in your cost optimization approach)

**What they're testing:**
- Practical cost optimization experience
- Understanding of LLM economics
- Engineering creativity
- Production mindset

**Your answer (based on your 40% approach):**

1. **Task decomposition analysis:**
   - Profile which LLM operations are repetitive
   - Identify patterns that can be automated with traditional code
   - Example: "For title generation, 40% of preprocessing (text cleaning, format normalization, language detection) can be done with Python"

2. **Caching strategies:**
   - Vector similarity search for duplicate/similar documents
   - Cache common query patterns
   - Prompt caching (Anthropic/OpenAI support this)
   - Result caching with TTL

3. **Model selection hierarchy:**
   - Use cheapest model that meets quality threshold
   - Route simple tasks to smaller models (Gemini Flash vs. Gemini Pro)
   - Reserve expensive models (GPT-4, Opus) for complex/ambiguous cases
   - A/B test to find quality/cost sweet spot

4. **Batch processing:**
   - Aggregate similar requests to reduce API overhead
   - Use batch APIs where available (SageMaker Batch Transform)
   - Schedule non-urgent jobs during off-peak pricing

5. **Early termination:**
   - Confidence scoring - if Python preprocessing gives high-confidence result, skip LLM
   - Use smaller model first, escalate to larger only if confidence < threshold

6. **Quantifiable results:**
   - "This approach reduced our LLM costs by 40%"
   - "Python preprocessing handles 40% of tasks, LLM only for remaining 60%"
   - "Improved throughput by 35% by reducing API calls"

**Connect to Scribd:**
- "For your 250M document pipeline, this could mean $X savings per month"
- "The self-serving platform you're building could incorporate these optimization rules"

**Practice:** Explain this approach in 5 minutes, then 10 minutes (with examples)

---

## ⭐ HIGH PRIORITY: CODING CHALLENGES (Practice 2-3 Hours Daily)

### Q3: Write a function to extract metadata from a document pipeline
**Preparation Impact:** ⭐ HIGH  
**Probability:** 85%+ (Core role responsibility)

**Possible variations:**
1. **Extract text from PDF and classify into categories**
2. **Parse structured metadata from unstructured documents**
3. **Implement a data transformation pipeline stage**
4. **Build a simple RAG retrieval function**

**Example problem:**
```python
"""
Given a list of documents with raw text, extract:
1. Title (first non-empty line or first 100 chars)
2. Language (detect from text)
3. Word count
4. Key topics (extract top 5 words by frequency, excluding stop words)

Input: List[Dict] with 'id' and 'text' fields
Output: List[Dict] with id, title, language, word_count, topics

Handle edge cases:
- Empty documents
- Very large documents (>1M chars)
- Non-UTF8 encoding
- Missing fields
"""
```

**What they're testing:**
- Python proficiency
- Data processing patterns
- Error handling
- Efficiency (time/space complexity)
- Production code quality (not just algorithm)

**Your approach:**
1. **Clarify requirements:** Ask about scale, error handling expectations
2. **Design first:** Explain approach before coding
3. **Write clean code:** Type hints, docstrings, meaningful variable names
4. **Handle edge cases:** Empty docs, encoding issues, memory limits
5. **Discuss optimization:** Batch processing, streaming for large docs
6. **Test:** Walk through test cases

**Practice problems:**
- LeetCode: Data processing, string manipulation (Medium level)
- Real-world: PDF parsing, JSON transformation, API data enrichment
- **Specifically practice:** Text processing, data pipeline stages, error handling

**Time target:** Complete in 25-30 minutes (for 45-minute interview)

---

### Q4: Implement a distributed task queue worker
**Preparation Impact:** ⭐ HIGH  
**Probability:** 70%+ (Core distributed systems skill)

**Example problem:**
```python
"""
Implement a worker that:
1. Polls SQS queue for document processing tasks
2. Downloads document from S3
3. Calls metadata extraction API
4. Saves results to DynamoDB
5. Handles failures with exponential backoff
6. Deletes message from queue on success

Include proper error handling, logging, and retry logic.
"""
```

**What they're testing:**
- AWS service integration knowledge
- Distributed systems patterns
- Error handling and resilience
- Production-ready code

**Key concepts to cover:**
- Message visibility timeout
- Idempotency (handling duplicate processing)
- Dead letter queues
- Exponential backoff
- Circuit breaker pattern
- Graceful shutdown
- Monitoring/logging

**Practice:** Build this end-to-end at least once before interview

---

### Q5: Implement rate limiting for LLM API calls
**Preparation Impact:** ⭐ HIGH  
**Probability:** 75%+ (Sachin mentioned hitting OpenAI limits)

**Example problem:**
```python
"""
Implement a rate limiter that:
- Allows max N requests per minute
- Queues excess requests
- Handles burst traffic
- Works across multiple Lambda workers (distributed)

Bonus: Implement token bucket algorithm
Bonus: Handle multiple rate limits (per-second, per-minute, per-day)
"""
```

**What they're testing:**
- Understanding of rate limiting algorithms
- Distributed systems coordination
- Redis/ElastiCache usage
- Production scalability

**Algorithms to know:**
1. **Token bucket:** Most common for API rate limiting
2. **Leaky bucket:** Smooth traffic
3. **Fixed window:** Simple but has edge cases
4. **Sliding window:** More accurate

**Your implementation should:**
- Use Redis/ElastiCache for distributed state
- Handle concurrent requests correctly
- Gracefully queue or reject excess
- Log rate limit events

**Practice:** Implement token bucket in Python, explain trade-offs

---

## ✅ MEDIUM PRIORITY: SYSTEM DESIGN (Breadth Coverage)

### Q6: Design a content moderation system for 250M documents
**Preparation Impact:** ✅ MEDIUM  
**Probability:** 60% (One of two main team domains)

**What they're testing:**
- Understanding of content moderation challenges
- ML pipeline design
- Policy enforcement architecture
- Scalability

**Your design should include:**

1. **Ingestion & Triage:**
   - New document upload → immediate scan
   - Risk scoring (ML model) → prioritize high-risk for human review
   - Fingerprinting for known bad content (hash matching)

2. **Detection Layer:**
   - Google Safe Browsing API integration
   - Custom ML models (NSFW, hate speech, copyright)
   - LLM-based policy violation detection
   - Image/text multi-modal analysis

3. **Action Layer:**
   - Auto-block high-confidence violations
   - Queue medium-confidence for human review
   - Allow low-risk content immediately

4. **Feedback Loop:**
   - Human review results → retrain models
   - False positive/negative tracking
   - Policy updates propagate to models

5. **Scale considerations:**
   - Async processing (don't block upload UX)
   - Batch processing for backlog
   - Incremental updates (only re-scan changed docs)

**Connect to your experience:**
- "At Amazon, we had similar challenges with user-generated content in customer reviews..."
- "My AI agent experience includes classification and risk assessment..."

---

### Q7: Design a document translation system preserving structure
**Preparation Impact:** ✅ MEDIUM  
**Probability:** 50% (Active 2026 project Sachin mentioned)

**Challenges Sachin mentioned:**
- Translate text while keeping fonts, images, structure
- Not just simple translation
- Handle multiple languages
- Scale to millions of documents

**Your design should address:**

1. **Document parsing:**
   - Extract text positions, fonts, styles
   - Preserve layout metadata
   - Handle embedded images, tables, charts

2. **Translation pipeline:**
   - Text extraction → translation API → text replacement
   - Preserve formatting tags
   - Handle text expansion (English → German might be 30% longer)

3. **Layout adjustment:**
   - Reflow text to fit original bounding boxes
   - Adjust font sizes if needed
   - Maintain readability

4. **Quality assurance:**
   - Pre/post comparison checks
   - Human review for high-value docs
   - A/B test quality metrics

5. **Optimization:**
   - Cache common translations
   - Batch similar documents
   - Prioritize by popularity/language demand

---

### Q8: Design a self-serving LLM platform
**Preparation Impact:** ✅ MEDIUM-HIGH  
**Probability:** 65% (Their 2026 vision - Sachin mentioned this)

**Requirements (from Sachin):**
- User submits prompt
- Selects model
- Chooses document sample size (1K to 100M+)
- Runs inference
- Exports results

**Your design should include:**

1. **UI/API Layer:**
   - Prompt builder with templates
   - Model selector (GPT-4, Gemini, Llama, etc.)
   - Sample size selector with cost estimation
   - Job submission and tracking

2. **Orchestration Layer:**
   - Job queue (SQS/Kafka)
   - Worker pool (Lambda/ECS)
   - Dynamic scaling based on job size
   - Priority queue (urgent vs. batch)

3. **Execution Layer:**
   - Document sampling strategy
   - Parallel processing (Step Functions)
   - Model-specific preprocessing
   - Result aggregation

4. **Cost Optimization:**
   - Show cost estimate before running
   - Implement your 40% approach (Python preprocessing)
   - Caching layer for duplicate prompts
   - Budget limits per user/team

5. **Monitoring & Quality:**
   - Real-time progress tracking
   - Quality metrics (if ground truth available)
   - Error handling and retry logic
   - Results export (CSV, JSON, database)

**This is YOUR opportunity to shine:**
- "This aligns perfectly with the cost optimization approach I shared with Sachin..."
- "I've built similar self-serving platforms at Amazon for internal tools..."

---

## 💡 BONUS: TECHNICAL DEPTH QUESTIONS

### Q9: Spark internals and optimization
**Preparation Impact:** 💡 BONUS  
**Probability:** 40% (You don't have direct experience, but showed interest)

**Key concepts to know:**
- **RDD vs DataFrame vs Dataset:** When to use each
- **Lazy evaluation:** Transformations vs actions
- **DAG execution:** How Spark optimizes query plans
- **Partitioning:** Data distribution across nodes
- **Shuffling:** Most expensive operation, how to minimize
- **Caching:** When to cache intermediate results
- **Broadcast variables:** Efficient distribution of lookup tables

**Your approach if asked:**
- Be honest: "I haven't used Spark in production, but I've researched it extensively"
- Connect to Step Functions: "I used similar DAG-based orchestration with Step Functions"
- Show learning: "I understand the key concepts like partitioning, shuffling, and lazy evaluation"
- Express interest: "I'm excited to learn Spark - it's a natural evolution from my Step Functions experience"

**Study resources:**
- Read Spark official docs (RDD programming guide, SQL guide)
- Understand common optimizations (avoid shuffles, use broadcast joins, cache wisely)
- Know when to use Spark vs alternatives (Lambda, Glue, EMR)

---

### Q10: Scala basics (if they ask)
**Preparation Impact:** 💡 BONUS  
**Probability:** 30% (Team uses Scala for Spark, but Sachin said it's not a blocker)

**Minimum you should know:**
- Scala is JVM language, interoperable with Java
- Functional programming features (immutability, higher-order functions)
- Common syntax patterns (val vs var, case classes, pattern matching)
- Used in Spark because it's Spark's native language

**Your approach if asked:**
- "I haven't written production Scala, but I have exposure from reviewing Spark code"
- "I learned Kotlin at Amazon which has similar functional programming concepts"
- "I'm a fast learner - I picked up Kotlin in 2 weeks when I joined Prime Pantry"
- "My focus has been Python for data engineering, but I'm excited to learn Scala"

**Don't:**
- Pretend you know Scala deeply
- Say "I don't know Scala" without context
- Show resistance to learning it

**Do:**
- Acknowledge gap honestly
- Show related experience (Kotlin, functional programming)
- Express genuine interest in learning
- Demonstrate fast learning ability with examples

---

## 🎯 BEHAVIORAL QUESTIONS (Technical Context)

### Q11: Tell me about a time you optimized a system for cost or performance
**Preparation Impact:** ⭐ HIGH  
**Probability:** 85%+

**Your stories (ranked by relevance):**

1. **🔥 BEST: LLM cost optimization (40% reduction)**
   - Context: LLM tasks were expensive at scale
   - Action: Analyzed repetitive patterns, automated 40% with Python
   - Result: 40% cost reduction, maintained quality
   - Why it's best: Directly addresses their 2026 challenge

2. **⭐ GREAT: $30K AWS savings (Prime Pantry)**
   - Context: Rising AWS costs for CI/CD pipelines
   - Action: Systematic audit, rightsized resources, implemented policies
   - Result: $30K annual savings, 95% reduction in deployment errors
   - Why it's great: Shows cost-consciousness, AWS expertise

3. **✅ GOOD: 50% efficiency improvement (Beauty Tech data lake)**
   - Context: Data pipeline was slow, couldn't keep up with growth
   - Action: Serverless architecture, auto-scaling, parallel processing
   - Result: 50% efficiency gain, handles 40TB/day
   - Why it's good: Shows large-scale optimization

**Use STAR format:**
- **Situation:** Context and scale
- **Task:** Your responsibility
- **Action:** Specific steps you took (use "I", not "we")
- **Result:** Quantifiable impact

---

### Q12: Tell me about a time you handled ambiguity in a technical project
**Preparation Impact:** ⭐ HIGH  
**Probability:** 75%

**Your best story: Project Scott (AI Documentation Agent)**

**STAR format:**
- **Situation:** Team documentation was a mess, new hires struggling, complaints escalating
- **Task:** No clear solution, had to figure out how to solve this systematically
- **Action:** 
  - Started as side project to explore AI-powered solution
  - Built RAG pipeline with FAISS vector database
  - Integrated with Slack for easy access
  - Prototyped multi-agent architecture with dynamic agent creation
  - Showed working demo to leadership
  - Got buy-in to make it official project
- **Result:**
  - 82% resolution time improvement
  - 240+ dev-hours saved per month
  - Became model for other teams
  - Led org-wide documentation workshop

**Why this story works:**
- Shows initiative (started as side project)
- Shows technical depth (RAG, vector DB, multi-agent)
- Shows handling ambiguity (no clear path, figured it out)
- Shows impact (quantifiable results)
- Shows leadership (influenced org-wide change)

---

### Q13: Tell me about a time you disagreed with a technical decision
**Preparation Impact:** ✅ MEDIUM  
**Probability:** 60%

**Possible story: Spark vs Step Functions decision**

**STAR format:**
- **Situation:** Team was considering Spark for Beauty Tech data pipeline
- **Task:** Evaluate best architecture for our use case
- **Action:**
  - Researched Spark thoroughly (pros/cons)
  - Considered team experience (junior devs, timeline)
  - Analyzed our specific needs (modularity, SageMaker integration)
  - Proposed Step Functions + Lambda as alternative
  - Showed we could get Spark-like patterns without learning curve
  - Presented trade-off analysis to leadership
- **Result:**
  - Team agreed with Step Functions approach
  - Delivered project on time
  - 50% efficiency improvement
  - Maintained flexibility for future Spark migration if needed

**Why this story works:**
- Shows technical judgment (evaluated trade-offs)
- Shows data-driven decision making (not just opinion)
- Shows respect for team constraints (junior devs, timeline)
- Shows you can advocate for your position professionally
- Shows you're open to learning (mentioned Spark is still valuable)

**Note:** Frame this as "different perspectives" not "conflict"

---

## 🛠️ TECHNICAL SKILLS - QUICK REFERENCE

### Python (You're an expert - be ready to code)
**Topics to review:**
- List comprehensions, generators
- Decorators and context managers
- Async/await (asyncio)
- Error handling (try/except, custom exceptions)
- Type hints
- Common libraries: requests, boto3, pandas (basics)

### AWS Services (Deep knowledge - explain architectures)
**Must know cold:**
- Lambda: Triggers, layers, cold starts, concurrency
- Step Functions: State machines, error handling, retries
- SageMaker: Endpoints, batch transform, model deployment
- DynamoDB: Partition keys, GSIs, transactions, TTL
- S3: Buckets, policies, lifecycle, event notifications
- SQS: Standard vs FIFO, visibility timeout, DLQ
- CloudWatch: Metrics, alarms, logs, X-Ray tracing

### Distributed Systems (Concepts - discuss trade-offs)
**Core concepts:**
- CAP theorem (Consistency, Availability, Partition tolerance)
- Eventual consistency vs strong consistency
- Sharding and partitioning strategies
- Load balancing (round-robin, least-connections, consistent hashing)
- Caching strategies (write-through, write-back, cache-aside)
- Message queues and event-driven architecture
- Idempotency and exactly-once delivery
- Circuit breaker pattern
- Rate limiting algorithms

### Data Engineering (Patterns - design pipelines)
**Core patterns:**
- ETL vs ELT
- Batch vs streaming processing
- Data validation and quality checks
- Schema evolution
- Data versioning
- Partitioning strategies (by date, by type, by hash)
- Slowly changing dimensions
- Data lineage and observability

---

## 📚 STUDY PLAN (By Day)

### Day 1-2: Coding Practice
- **Focus:** Python data processing problems
- **Goal:** Solve 5-10 LeetCode Medium problems (data structures, string manipulation)
- **Specifically:** Write clean, production-ready code with error handling
- **Time:** 3-4 hours/day

### Day 3-4: System Design
- **Focus:** Draw architecture diagrams
- **Goal:** Practice Q1 (metadata pipeline) 10+ times
- **Specifically:** Time yourself - aim for 15 minutes to draw + explain
- **Time:** 3-4 hours/day

### Day 5-6: Cost Optimization Deep Dive
- **Focus:** Your 40% approach
- **Goal:** Explain clearly in 5 min, 10 min, and 20 min formats
- **Specifically:** Prepare concrete examples with numbers
- **Time:** 2-3 hours/day

### Day 7: Mock Interview
- **Focus:** Full simulation
- **Goal:** Practice coding + system design back-to-back
- **Specifically:** Record yourself, identify areas to tighten up
- **Time:** 3-4 hours

---

## 🎯 FINAL PRE-INTERVIEW CHECKLIST

**24 hours before:**
- ✅ Review this document (30 min)
- ✅ Practice Q1 (metadata pipeline) one more time (30 min)
- ✅ Practice Q2 (cost optimization) explanation (30 min)
- ✅ Review your resume - be ready to explain any project (30 min)
- ✅ Test your setup (camera, mic, internet, whiteboarding tool) (15 min)

**Morning of interview:**
- ✅ Light review (don't cram - you're prepared!)
- ✅ Review this "Final Checklist" section
- ✅ Deep breath - you've got this!

---

## 💪 CONFIDENCE BOOSTERS

**Remember:**
- ✅ You built 40TB/day pipelines at Amazon
- ✅ You have LLM production experience (rare!)
- ✅ Your cost optimization approach impressed Sachin
- ✅ You're an AWS expert (perfect for their new stack)
- ✅ You've led teams and driven org-wide initiatives
- ✅ Sachin said "your experience will come handy for us"

**You're not hoping to pass - you're demonstrating why you're the right hire.** 🚀

---

## 🎤 INTERVIEW DAY MINDSET

1. **Clarify before coding:** Ask questions, confirm requirements
2. **Think out loud:** Explain your reasoning as you go
3. **Start simple:** Get a working solution first, optimize later
4. **Test your code:** Walk through examples, edge cases
5. **Discuss trade-offs:** There's rarely one "right" answer
6. **Show production mindset:** Error handling, logging, monitoring
7. **Connect to your experience:** "At Amazon, I handled similar challenges..."
8. **Express enthusiasm:** "This is exciting!" "I love this type of problem!"
9. **Ask clarifying questions:** Shows you think before acting
10. **Stay calm:** If you get stuck, talk through your thought process

---

**You've got this! This is YOUR role - show them why.** 🔥

