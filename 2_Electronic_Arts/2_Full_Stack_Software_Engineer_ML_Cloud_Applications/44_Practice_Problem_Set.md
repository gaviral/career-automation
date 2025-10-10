# Practice Problem Set
**Curated LeetCode problems matching EA interview topics**  
**Estimated total time: 10-12 hours** (spread over 3-5 days)

---

## HOW TO USE THIS LIST

### Study Strategy:
1. **Attempt each problem yourself first** (time limit: 30 min)
2. **If stuck after 30 min:** Read hints, try again (15 min)
3. **If still stuck:** See File 41 answer or LeetCode solution
4. **Always:** Write solution from scratch without looking (test understanding)
5. **Track progress:** Check off completed problems

### Priority Levels:
- **P0 (Critical):** Daniel explicitly mentioned or core to job description
- **P1 (High):** Very likely based on role requirements
- **P2 (Medium):** Good to know, time permitting

---

## TIER 1: MUST PRACTICE (P0 - Critical)

### Problem 1: Merge Sort Implementation
**Priority:** P0  
**LeetCode:** N/A (Implement from scratch)  
**Time:** 30 min  
**Why:** Daniel explicitly said "optimize sorting"

**Task:**
```python
def merge_sort(arr):
    """
    Implement merge sort
    Time: O(n log n), Space: O(n)
    """
    # Your implementation here
    pass

# Test cases
assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
assert merge_sort([]) == []
assert merge_sort([1]) == [1]
```

**After solving:** Compare to File 41, Q1. Can you explain time complexity derivation?

---

### Problem 2: 226. Invert Binary Tree
**Priority:** P0  
**LeetCode:** https://leetcode.com/problems/invert-binary-tree/  
**Time:** 15 min  
**Why:** Daniel explicitly mentioned this

**Task:** Implement both recursive and iterative solutions.

**Practice questions to answer:**
- What's the time complexity? Space complexity?
- Which is better: recursive or iterative? Why?
- How would you test this thoroughly?

**After solving:** See File 41, Q2. Practice whiteboarding this.

---

### Problem 3: Design Pattern - Factory
**Priority:** P0  
**LeetCode:** N/A (Design problem)  
**Time:** 45 min  
**Why:** Daniel said "implement object-oriented thing adapting this to that"

**Task:** Implement factory pattern for ML models (SageMaker, Local, Batch). See File 41, Q3 for specification.

**Extension:** Add a new model type (e.g., "LambdaModel" for lightweight inference). How easy was it? (Should be easy if factory well-designed.)

---

### Problem 4: Two Sum
**Priority:** P0  
**LeetCode:** https://leetcode.com/problems/two-sum/  
**Time:** 15 min  
**Why:** Classic problem, Daniel mentioned "general programming"

**Task:** Solve with O(n) time, O(n) space.

**Practice questions:**
- Explain why hash table works here
- What if array is sorted? (Follow-up: Two Sum II)
- What if we want all pairs? (Modification)

---

### Problem 5: System Design - Content Validation Service
**Priority:** P0  
**LeetCode:** N/A (System design)  
**Time:** 60 min  
**Why:** Daniel mentioned "automatically validating renders" as use case

**Task:** Design end-to-end system (API, validators, storage, notification). See File 41, Q4 for details.

**Practice:** Draw architecture on whiteboard, explain to rubber duck, time yourself.

---

## TIER 2: SHOULD PRACTICE (P1 - High Priority)

### Problem 6: 215. Kth Largest Element
**Priority:** P1  
**LeetCode:** https://leetcode.com/problems/kth-largest-element-in-an-array/  
**Time:** 30 min  
**Why:** Heap/sorting optimization question

**Task:** Solve with:
1. Sorting approach (O(n log n))
2. Heap approach (O(n log k))
3. Quickselect approach (O(n) average)

**Compare:** Which is best for k=1? k=n/2? k=n?

---

### Problem 7: 104. Maximum Depth of Binary Tree
**Priority:** P1  
**LeetCode:** https://leetcode.com/problems/maximum-depth-of-binary-tree/  
**Time:** 15 min  
**Why:** Tree traversal, related to invert binary tree

**Task:** Implement both recursive and iterative (BFS).

**Extension:** 111. Minimum Depth of Binary Tree (slightly trickier)

---

### Problem 8: 102. Binary Tree Level Order Traversal
**Priority:** P1  
**LeetCode:** https://leetcode.com/problems/binary-tree-level-order-traversal/  
**Time:** 25 min  
**Why:** BFS pattern, common follow-up to tree problems

**Task:** Use queue, return list of lists.

**Connect:** "In VTO, we processed products in batches (levels) through pipeline stages."

---

### Problem 9: 125. Valid Palindrome
**Priority:** P1  
**LeetCode:** https://leetcode.com/problems/valid-palindrome/  
**Time:** 15 min  
**Why:** Two-pointer technique, string manipulation

**Task:** Solve with two pointers, O(n) time, O(1) space.

**Extension:** 680. Valid Palindrome II (delete at most one character)

---

### Problem 10: 242. Valid Anagram
**Priority:** P1  
**LeetCode:** https://leetcode.com/problems/valid-anagram/  
**Time:** 10 min  
**Why:** Hash table usage, sorting

**Task:** Solve two ways:
1. Sorting
2. Hash map

**Compare:** Which is faster for very long strings?

---

### Problem 11: 146. LRU Cache
**Priority:** P1  
**LeetCode:** https://leetcode.com/problems/lru-cache/  
**Time:** 45 min  
**Why:** Design problem combining hash map + doubly linked list

**Task:** Implement with O(1) get and put.

**Connect:** "Similar to caching model inference results in VTO to avoid reprocessing."

---

### Problem 12: Design Pattern - Observer
**Priority:** P1  
**LeetCode:** N/A (Design problem)  
**Time:** 30 min  
**Why:** Event-driven architecture (VTO used SNS/SQS)

**Task:**
```python
class Subject:
    def attach(self, observer): pass
    def detach(self, observer): pass
    def notify(self): pass

class Observer:
    def update(self, subject): pass

# Implement pipeline status notification system
```

**Connect:** "VTO pipeline stages notified downstream services via SNS."

---

### Problem 13: 206. Reverse Linked List
**Priority:** P1  
**LeetCode:** https://leetcode.com/problems/reverse-linked-list/  
**Time:** 20 min  
**Why:** Classic problem, tests pointer manipulation

**Task:** Implement both iterative and recursive.

**Practice questions:**
- What's space complexity of recursive? Why?
- Can you do it with O(1) space?

---

### Problem 14: 56. Merge Intervals
**Priority:** P1  
**LeetCode:** https://leetcode.com/problems/merge-intervals/  
**Time:** 30 min  
**Why:** Sorting + greedy algorithm

**Task:** Sort by start time, merge overlapping.

**Connect:** "In VTO, we merged overlapping processing windows to optimize batch jobs."

---

### Problem 15: Design - Step Functions Error Handling
**Priority:** P1  
**LeetCode:** N/A (AWS design)  
**Time:** 30 min  
**Why:** Core to VTO architecture

**Task:** Design Step Functions state machine with:
- Exponential backoff retry
- Catch blocks for different error types
- Parallel execution with error isolation

**See:** File 41, Q6 for details.

---

## TIER 3: NICE TO HAVE (P2 - Time Permitting)

### Problem 16: 53. Maximum Subarray (Kadane's Algorithm)
**Priority:** P2  
**LeetCode:** https://leetcode.com/problems/maximum-subarray/  
**Time:** 25 min  
**Why:** Dynamic programming introduction

---

### Problem 17: 20. Valid Parentheses
**Priority:** P2  
**LeetCode:** https://leetcode.com/problems/valid-parentheses/  
**Time:** 15 min  
**Why:** Stack usage, common interview problem

---

### Problem 18: 121. Best Time to Buy and Sell Stock
**Priority:** P2  
**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/  
**Time:** 20 min  
**Why:** One-pass algorithm, tracking min/max

---

### Problem 19: 94. Binary Tree Inorder Traversal
**Priority:** P2  
**LeetCode:** https://leetcode.com/problems/binary-tree-inorder-traversal/  
**Time:** 20 min  
**Why:** Tree traversal, iterative with stack

---

### Problem 20: Design - DynamoDB Table for ML Results
**Priority:** P2  
**LeetCode:** N/A (AWS design)  
**Time:** 30 min  
**Why:** Job description mentions DynamoDB

**Task:**
- Design schema for storing VTO color extraction results
- Choose partition key (high cardinality, even access)
- Design GSI for querying by timestamp or status

---

## STUDY SCHEDULE

### Day 1 (3 hours): Core Algorithms
- [ ] Problem 1: Merge Sort (30 min)
- [ ] Problem 2: Invert Binary Tree (15 min)
- [ ] Problem 4: Two Sum (15 min)
- [ ] Problem 6: Kth Largest (30 min)
- [ ] Problem 7: Max Depth (15 min)
- [ ] Problem 9: Valid Palindrome (15 min)
- [ ] Problem 10: Valid Anagram (10 min)
- [ ] Review answers, understand patterns (40 min)

### Day 2 (3 hours): Design Patterns
- [ ] Problem 3: Factory Pattern (45 min)
- [ ] Problem 12: Observer Pattern (30 min)
- [ ] Problem 5: System Design - Validation Service (60 min)
- [ ] Review File 41 Q3-Q4 in detail (45 min)

### Day 3 (2.5 hours): Trees & Advanced
- [ ] Problem 8: Level Order Traversal (25 min)
- [ ] Problem 11: LRU Cache (45 min)
- [ ] Problem 13: Reverse Linked List (20 min)
- [ ] Problem 14: Merge Intervals (30 min)
- [ ] Review patterns, practice whiteboarding (30 min)

### Day 4 (2.5 hours): AWS & System Design
- [ ] Problem 15: Step Functions Design (30 min)
- [ ] Problem 20: DynamoDB Design (30 min)
- [ ] Re-draw VTO architecture from memory (30 min)
- [ ] Re-draw Scott architecture from memory (20 min)
- [ ] Practice explaining both out loud (40 min)

### Day 5 (1.5 hours): Review & Mock
- [ ] Redo Problems 1, 2, 4 without looking (45 min)
- [ ] Mock interview: Friend asks Problem 5 (30 min)
- [ ] Review File 43 (Day-of Cheat Sheet) (15 min)

---

## PRACTICE TRACKING

### Completion Checklist:

**P0 (Critical) - Must Complete:**
- [ ] Problem 1: Merge Sort
- [ ] Problem 2: Invert Binary Tree
- [ ] Problem 3: Factory Pattern
- [ ] Problem 4: Two Sum
- [ ] Problem 5: System Design - Validation

**P1 (High) - Should Complete:**
- [ ] Problem 6: Kth Largest
- [ ] Problem 7: Max Depth
- [ ] Problem 8: Level Order Traversal
- [ ] Problem 9: Valid Palindrome
- [ ] Problem 10: Valid Anagram
- [ ] Problem 11: LRU Cache
- [ ] Problem 12: Observer Pattern
- [ ] Problem 13: Reverse Linked List
- [ ] Problem 14: Merge Intervals
- [ ] Problem 15: Step Functions Design

**P2 (Medium) - Time Permitting:**
- [ ] Problem 16: Max Subarray
- [ ] Problem 17: Valid Parentheses
- [ ] Problem 18: Buy/Sell Stock
- [ ] Problem 19: Inorder Traversal
- [ ] Problem 20: DynamoDB Design

### Self-Assessment:

**After Each Problem, Rate Yourself:**
- ✅ **Confident:** Solved in time limit, explained clearly, connected to VTO/Scott
- ⚠️ **Shaky:** Solved but took longer, or needed hints, or explanation unclear
- ❌ **Struggle:** Didn't solve in time, or couldn't explain approach

**If ❌ or ⚠️:** Redo problem next day without looking at solution.

---

## ADDITIONAL RESOURCES

### For More Practice:
- **NeetCode 150:** curated list, video explanations (neetcode.io)
- **Blind 75:** most common interview questions
- **LeetCode Top Interview Questions:** filter by company (EA uses similar questions as FAANG)

### For System Design:
- **System Design Primer:** github.com/donnemartin/system-design-primer
- **AWS Architecture Center:** aws.amazon.com/architecture
- **Your VTO/Scott projects:** Best examples, practice explaining these

### For Design Patterns:
- **Refactoring Guru:** refactoring.guru/design-patterns
- **Python Patterns:** python-patterns.guide
- **Your own implementations:** From File 41, type them out from memory

---

## SUCCESS METRICS

**By End of Practice:**
- [ ] Can solve P0 problems in <20 min without looking
- [ ] Can draw VTO architecture from memory in <5 min
- [ ] Can draw Scott architecture from memory in <5 min
- [ ] Can explain Factory pattern in <3 min
- [ ] Can explain Step Functions error handling in <5 min
- [ ] Can design validation service in <25 min (high-level)

**If you can check all boxes above, you're interview-ready. 🎯**

---

## FINAL NOTE

**Quality > Quantity:** Better to deeply understand 15 problems than superficially solve 50.

**Connect to Projects:** For every problem, ask "How does this relate to VTO or Scott?" Even if tenuous, the practice of making connections helps in interviews.

**Think Out Loud:** Practice explaining your thought process. Record yourself, watch back, identify where explanation unclear.

**You're Ready:** Daniel already said you fit well. These problems solidify technical execution to match your excellent system design thinking.


