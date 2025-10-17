# Prioritized Interview Question List
**Sorted by likelihood** (most probable at top)  
**Source weight:** Transcript > Role requirements > Industry standards

---

## TIER 1: EXTREMELY HIGH PROBABILITY (90-100%)
*Daniel explicitly mentioned these topics or they're core to job description*

### 1. **[CODING - DSA] Sorting Algorithm Optimization**
**Why:** Daniel explicitly said "optimize sorting" and "typical questions about sorting a list"  
**Difficulty:** Medium  
**Your angle:** Reference VTO Athena query optimization

### 2. **[CODING - DSA] Invert Binary Tree**
**Why:** Daniel said "inverted binary tree, that kind of thing"  
**Difficulty:** Easy-Medium  
**Your angle:** Classic problem, explain recursive and iterative approaches

### 3. **[OOP] Implement Design Pattern - Factory or Strategy**
**Why:** Daniel said "how can you implement object-oriented thing adapting this to that"  
**Difficulty:** Medium  
**Your angle:** VTO had Strategy pattern for data sources (Athena, streaming, etc.)

### 4. **[ARCHITECTURE] Design Application Architecture (MVC or Microservices)**
**Why:** Daniel explicitly said "how would you design the architecture of an app? Model view controller, maybe"  
**Difficulty:** Medium-Hard  
**Your angle:** Discuss VTO as microservices (Lambda functions, Step Functions orchestration)

### 5. **[ML] Explain ML Parameter Configuration in Production Environment**
**Why:** Daniel said "how parameters are set up in a specific machine learning environment"  
**Difficulty:** Medium  
**Your angle:** SageMaker endpoints (instance type, auto-scaling, hyperparameters)

### 6. **[AWS] Design Lambda + API Gateway Service**
**Why:** Core job requirement (Lambda, API Gateway explicitly listed)  
**Difficulty:** Medium  
**Your angle:** Project Scott - Slack integration via API Gateway + Lambda

### 7. **[SYSTEM DESIGN] Design Content Validation Service**
**Why:** Daniel mentioned "automatically validating renders" as new use case  
**Difficulty:** Hard  
**Your angle:** Similar to VTO - image processing pipeline with ML validation

---

## TIER 2: VERY HIGH PROBABILITY (75-90%)
*Strongly aligned with role, interviewer focus, or your demonstrated experience*

### 8. **[AWS] Design Step Functions Workflow with Error Handling**
**Why:** VTO used Step Functions, job description mentions SAM (serverless), operational readiness theme  
**Difficulty:** Medium-Hard  
**Your angle:** VTO architecture with exponential backoff, X-ray tracing

### 9. **[ML] Batch vs Real-Time Inference - When to Use Each**
**Why:** Common ML deployment question, matches VTO batch processing  
**Difficulty:** Medium  
**Your angle:** VTO used batch (SageMaker batch transform), explain trade-offs

### 10. **[SCALABILITY] How Do You Scale a System 10x?**
**Why:** Rhea's core focus ("that's my thing"), she deeply probed VTO scaling  
**Difficulty:** Hard  
**Your angle:** VTO Athena solution, worldwide expansion, no late-stage failures

### 11. **[CODING - DSA] Two Sum / Array Manipulation**
**Why:** Classic coding interview, Daniel mentioned "general programming"  
**Difficulty:** Easy-Medium  
**Your angle:** Clean Python code with hash table optimization

### 12. **[OOP] Design Class Hierarchy (Inheritance & Polymorphism)**
**Why:** Full-stack role, Daniel mentioned OOP focus  
**Difficulty:** Medium  
**Your angle:** Content asset hierarchy (Image, Video, Cinematic subclasses)

### 13. **[SYSTEM DESIGN] Design Production Tracking System**
**Why:** Daniel mentioned "production tracking" as new tool need, Blaze mentioned Airtable  
**Difficulty:** Medium-Hard  
**Your angle:** Event-driven updates, dashboard integration, timeline tracking

### 14. **[AWS] DynamoDB Table Design (Partition Key Strategy)**
**Why:** Job description lists DynamoDB, common serverless interview question  
**Difficulty:** Medium  
**Your angle:** VTO used DynamoDB for storing extraction results

---

## TIER 3: HIGH PROBABILITY (60-75%)
*Relevant to role, but may not be covered due to time constraints*

### 15. **[ML] Model Versioning and Rollback Strategy**
**Why:** Production ML requirement, operational readiness theme  
**Difficulty:** Medium  
**Your angle:** A/B testing approaches, SageMaker model registry

### 16. **[AWS] Lambda Cold Start Mitigation**
**Why:** Common Lambda interview question, job focuses on performance  
**Difficulty:** Medium  
**Your angle:** Provisioned concurrency, initialization code optimization

### 17. **[CODING - DSA] Tree Traversal (In/Pre/Post-Order)**
**Why:** Daniel mentioned trees ("inverted binary tree"), foundational skill  
**Difficulty:** Easy-Medium  
**Your angle:** Explain all three, discuss use cases

### 18. **[OOP] Observer Pattern Implementation**
**Why:** Design pattern question, event-driven systems (your VTO used SNS/SQS)  
**Difficulty:** Medium  
**Your angle:** VTO pipeline notifications, Project Scott SME alerts

### 19. **[SYSTEM DESIGN] Design AI Documentation Assistant**
**Why:** Blaze said "I have a lot of complaints about documentation internally"  
**Difficulty:** Hard  
**Your angle:** Your Project Scott - RAG, vector DB, agent orchestration

### 20. **[AWS] S3 + Athena Optimization for Large Datasets**
**Why:** Your VTO solution, matches 40TB/day scale mentioned  
**Difficulty:** Medium  
**Your angle:** Parquet format, partitioning strategies, cost optimization

### 21. **[SCALABILITY] Auto-Scaling Strategy (Lambda, SageMaker)**
**Why:** Rhea's focus, production readiness requirement  
**Difficulty:** Medium  
**Your angle:** VTO SageMaker endpoint scaling, Lambda concurrency

### 22. **[ML] What Metrics Track for ML Model in Production?**
**Why:** Operational readiness, Rhea's SRE perspective  
**Difficulty:** Medium  
**Your angle:** Accuracy, latency, throughput, cost, data drift

---

## TIER 4: MODERATE PROBABILITY (40-60%)
*Could be asked if interviewers have specific interests or time allows*

### 23. **[ARCHITECTURE] RESTful API Design Best Practices**
**Why:** Full-stack role, API Gateway integration  
**Difficulty:** Medium  
**Your angle:** VTO served APIs for 3D asset team

### 24. **[CODING - DSA] Find K Largest Elements**
**Why:** Heap/priority queue question, common medium difficulty  
**Difficulty:** Medium  
**Your angle:** Heap approach vs sorting, time complexity trade-offs

### 25. **[AWS] Event-Driven Architecture with EventBridge**
**Why:** Modern serverless pattern, VTO used event-driven design  
**Difficulty:** Medium  
**Your angle:** VTO pipeline stages triggered by events (S3 → Lambda → SNS)

### 26. **[OOP] Singleton Pattern Implementation**
**Why:** Common design pattern question, practical use cases  
**Difficulty:** Easy-Medium  
**Your angle:** Configuration management, connection pooling

### 27. **[SYSTEM DESIGN] Design Document Generation System**
**Why:** Daniel mentioned "document generation for collecting data from brand, legal"  
**Difficulty:** Medium-Hard  
**Your angle:** Template-based generation, ML extraction of requirements

### 28. **[ML] Model Drift Detection Strategy**
**Why:** Production ML best practice, monitoring theme  
**Difficulty:** Medium  
**Your angle:** Statistical tests, retraining triggers, monitoring metrics

### 29. **[AWS] CloudWatch Monitoring & Alarming**
**Why:** Operational readiness, SRE perspective (Rhea)  
**Difficulty:** Medium  
**Your angle:** VTO used CloudWatch for Lambda metrics, X-ray for tracing

### 30. **[SCALABILITY] Cost Optimization in AWS**
**Why:** VTO discussion touched on cost concerns with different services  
**Difficulty:** Medium  
**Your angle:** Reserved capacity, Spot instances for training, lifecycle policies

---

## TIER 5: POSSIBLE (20-40%)
*Less central to role but still within scope*

### 31. **[CODING - DSA] Maximum Subarray Sum (Kadane's)**
**Why:** Classic DP problem, tests algorithmic thinking  
**Difficulty:** Medium  
**Your angle:** Dynamic programming concept

### 32. **[OOP] Adapter Pattern Implementation**
**Why:** Daniel mentioned "adapting this to that"  
**Difficulty:** Medium  
**Your angle:** Adapting third-party VTO vendor API to internal interface

### 33. **[ARCHITECTURE] Microservices vs Monolith Trade-offs**
**Why:** Architecture discussion, modern development  
**Difficulty:** Medium  
**Your angle:** VTO was microservices (Lambda functions), discuss when not to use

### 34. **[ML] RAG Architecture Explanation**
**Why:** Project Scott used RAG, AI focus of role  
**Difficulty:** Medium-Hard  
**Your angle:** Your Scott project - Pinecone vector DB, LLM integration

### 35. **[AWS] IAM Roles and Policies Best Practices**
**Why:** Security consideration for production systems  
**Difficulty:** Medium  
**Your angle:** Least privilege principle, VTO service roles

### 36. **[CODING - DSA] Merge K Sorted Lists**
**Why:** Advanced problem testing heap/divide-and-conquer  
**Difficulty:** Hard  
**Your angle:** Heap approach, similar to VTO data merging

### 37. **[SYSTEM DESIGN] Design Recommendation Engine for Artists**
**Why:** AI/ML application, content creation focus  
**Difficulty:** Hard  
**Your angle:** Collaborative filtering, content-based, hybrid approaches

### 38. **[ML] Feature Engineering Best Practices**
**Why:** ML development process  
**Difficulty:** Medium  
**Your angle:** VTO feature extraction (RGB, finish, particles)

### 39. **[AWS] VPC Configuration and Security Groups**
**Why:** AWS networking, security concern  
**Difficulty:** Medium  
**Your angle:** Production deployment considerations

### 40. **[SCALABILITY] Load Balancing Strategies**
**Why:** Scalability topic, though Lambda abstracts this  
**Difficulty:** Medium  
**Your angle:** API Gateway throttling, SageMaker endpoint distribution

---

## TIER 6: LOWER PROBABILITY (10-20%)
*Further from core role but potentially asked*

### 41. **[CODING - DSA] Graph Algorithms (BFS/DFS)**
**Why:** Algorithmic foundation, less specific to role  
**Difficulty:** Medium  
**Your angle:** Explain both, discuss use cases

### 42. **[OOP] Decorator Pattern**
**Why:** Python decorators, design pattern  
**Difficulty:** Medium  
**Your angle:** Python @ syntax, function wrapping

### 43. **[ML] Transfer Learning Explanation**
**Why:** Modern ML technique  
**Difficulty:** Medium  
**Your angle:** Fine-tuning pre-trained models

### 44. **[AWS] SQS vs SNS - When to Use Each**
**Why:** VTO used both, messaging patterns  
**Difficulty:** Easy-Medium  
**Your angle:** VTO used SNS for fan-out, SQS for queue buffering

### 45. **[ARCHITECTURE] CQRS Pattern**
**Why:** Advanced architecture pattern  
**Difficulty:** Hard  
**Your angle:** Separation of read/write concerns

### 46. **[SYSTEM DESIGN] Design CI/CD Pipeline for ML Models**
**Why:** MLOps practice, good engineering  
**Difficulty:** Medium-Hard  
**Your angle:** SageMaker Pipeline, testing strategies

### 47. **[ML] Hyperparameter Tuning Strategies**
**Why:** ML training optimization  
**Difficulty:** Medium  
**Your angle:** Grid search, random search, Bayesian optimization

### 48. **[CODING - DSA] Dynamic Programming - Longest Common Subsequence**
**Why:** Classic DP problem  
**Difficulty:** Medium-Hard  
**Your angle:** Bottom-up approach, memoization

### 49. **[AWS] CloudFormation vs Terraform**
**Why:** IaC comparison, job mentions CloudFormation  
**Difficulty:** Medium  
**Your angle:** VTO used CloudFormation via CDK, state management differences

### 50. **[SCALABILITY] Database Sharding Strategy**
**Why:** Scalability technique, less relevant with DynamoDB  
**Difficulty:** Hard  
**Your angle:** Partition key strategy analogous to sharding

---

## QUESTION SELECTION STRATEGY

### If Interview is 60 Minutes:
**Expect:**
- 2-3 coding questions (20-30 min total)
- 1-2 OOP/design questions (10-15 min)
- 1 system design question (20-25 min)
- 5-10 min for your questions

**Focus Tiers:** 1-2 (questions 1-14)

### If Interview is 90 Minutes:
**Expect:**
- 3-4 coding questions (30-40 min)
- 2-3 OOP/design questions (15-20 min)
- 1-2 system design questions (25-35 min)
- 5-10 min for your questions

**Focus Tiers:** 1-3 (questions 1-22)

### If Multiple Interview Panels:
Different panels may split focus:
- **Panel A:** Pure coding (Tier 1-2 coding questions)
- **Panel B:** System design + ML (Tier 1-2 system design/ML)
- **Panel C:** Behavioral + architecture (Leadership + design patterns)

---

## PREPARATION ALLOCATION

### 50% of Prep Time → Tier 1 (Questions 1-7)
These are near-certain. Must be confident.

### 30% of Prep Time → Tier 2 (Questions 8-14)
High likelihood. Should be comfortable.

### 15% of Prep Time → Tier 3 (Questions 15-22)
Good to know. Review but don't stress.

### 5% of Prep Time → Tiers 4-6 (Questions 23-50)
Skim for awareness. Don't memorize.

---

## CONTEXT-SPECIFIC INSIGHTS

### From Transcript:
- **Daniel cares about:** Thought process > syntax perfection
- **Rhea cares about:** Scalability, operational readiness, upfront planning
- **Blaze cares about:** Collaboration, practical tool design, artist empathy

### Interview Philosophy (Daniel's Words):
> "It's not about if you know the syntax, it's more about your general way of thinking, like designing a solution, exactly."

### Your Advantage:
Every question can tie back to VTO or Scott. Practice weaving project stories into technical answers.

**Example:**
- Q: "How do you handle Lambda cold starts?"
- A: "In my VTO project, we initially faced cold start issues when processing 40TB daily. We solved it by [technical solution], but first let me explain the context of why cold starts were critical for us..."

**This demonstrates:**
✅ Real experience (not textbook knowledge)  
✅ Problem-solving approach (not just memorization)  
✅ Production scale awareness (40TB/day)  
✅ Clear communication (context first)

---

## FINAL NOTES

### High-Confidence Areas (Leverage These):
1. AWS serverless (Lambda, Step Functions, API Gateway)
2. ML pipelines (data → train → deploy)
3. Scalability (VTO worldwide expansion, no failures)
4. Operational readiness (ORR, X-ray, CloudWatch)
5. Design patterns (Strategy, Observer from your projects)

### Lower-Confidence Areas (Study These):
1. Pure algorithm questions (practice LeetCode Medium)
2. OOP implementation details (practice coding patterns)
3. ML-specific questions (model deployment nuances)

### Red Flags to Avoid:
❌ Saying "I don't know" without thought process  
❌ Jumping to code without clarifying requirements  
❌ Over-engineering simple problems  
❌ Ignoring edge cases  
❌ Not asking questions back

### Green Flags to Demonstrate:
✅ Clarify before solving  
✅ Explain trade-offs explicitly  
✅ Reference real experience (VTO/Scott)  
✅ Think out loud  
✅ Handle hints gracefully  
✅ Show excitement about EA's mission

---

**Remember: Daniel already said "you fit very well." This is validation, not elimination.**


