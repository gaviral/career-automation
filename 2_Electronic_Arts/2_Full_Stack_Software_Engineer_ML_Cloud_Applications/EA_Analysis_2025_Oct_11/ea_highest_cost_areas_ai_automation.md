# EA: Highest Cost Areas for AI Automation

**Date**: October 11, 2025  
**Source**: Interview transcripts analysis + buyout context  
**Goal**: Identify where EA spends MOST money & where AI can cut costs most effectively

---

## Executive Summary: Follow The Money

**Biggest Cost Center**: **Content creation labor** (artists, designers, producers)

**Why**: Marketing org creates ALL content for ENTIRE EA portfolio—every trailer, screenshot, gameplay capture for every franchise (Battlefield, FIFA, Madden, Apex, Need for Speed, etc.)

**Scale**: 
- Blaze leads "craft group" that generates all this content
- Team located primarily in Vancouver + sister studios
- Content types: screenshots, cinematic videos, capture trailers, live action, gameplay shots

**Cost Reality**:
- Senior artists: $100K-150K/year
- Mid-level artists: $70K-100K/year  
- Junior artists: $50K-70K/year
- Tech Designers: $80K-120K/year
- Project Managers: $90K-130K/year

**Team Size Estimate** (Marketing Content Creation Org):
- ~50-100 artists (various levels)
- ~30-40 Tech Designers
- ~20-30 Project Managers/Producers
- **Total headcount: 100-170 people**
- **Annual cost: $10M-$17M**

**Where AI Cuts Deepest**: Content creation acceleration → same output with fewer artists

---

## Part 1: Cost Centers (Ranked by $ Impact)

### 1. Artist Labor ($5M-$10M/year) ★★★★★

**What They Do** (From Interview):
- Create trailers for every EA game launch
- Generate screenshots for marketing campaigns
- Produce cinematic videos
- Create live action promotional content
- Capture gameplay footage
- Make all visual assets for cross-franchise marketing

**Current Process** (Implied from "time to create asset types"):
- Manual composition & editing
- Multiple revision cycles
- Brand/legal approval loops
- Custom work for each franchise
- Repetitive tasks for similar asset types

**AI Automation Opportunity**:

#### **A. Generative AI for Asset Variations** (70% time reduction)
- **Current**: Artist manually creates 5 trailer variations for different platforms (YouTube, Instagram, TikTok, etc.)
- **AI-Automated**: Generate base trailer → AI creates all variations automatically
- **Tech**: Runway, Pika-style video generation + custom Frostbite integration
- **Savings**: 30-40% artist headcount ($2M-$4M/year)

#### **B. Auto-Composition & Editing** (60% time reduction)
- **Current**: Editors manually cut together gameplay footage, add effects, timing
- **AI-Automated**: AI suggests cuts, transitions, pacing based on "exciting moments"
- **Tech**: ML models trained on past successful trailers
- **Savings**: 20-30% editor positions ($1M-$2M/year)

#### **C. Automated Screenshot Generation** (80% time reduction)
- **Current**: Artists manually position camera, lighting, capture, edit screenshots
- **AI-Automated**: AI identifies visually interesting game moments → auto-generates marketing screenshots
- **Tech**: Computer vision + Frostbite camera control automation
- **Savings**: 2-3 dedicated screenshot artists ($150K-$300K/year) + 20% of other artists' time ($800K-$1.5M/year)

**Total Artist Labor Savings: $4M-$8M/year (40-50% reduction)**

---

### 2. Project Management Overhead ($2M-$4M/year) ★★★★☆

**What They Do** (From Daniel's Description):
- "Production tracking"
- "Document generation for collecting data from brand, legal, making brief of production"
- Coordinate between artists, brand, legal, game studios
- Track timelines in Airtable
- Manage approval workflows

**Current Process**:
- Manual data gathering from stakeholders
- Document creation for each project
- Status tracking & updates
- Meeting coordination
- Approval routing

**AI Automation Opportunity**:

#### **A. Automated Production Brief Generation** (70% time reduction)
- **Current**: PM spends 2-3 days gathering requirements from brand, legal, game teams → creates production brief
- **AI-Automated**: RAG system scrapes inputs from email/Slack/docs → LLM generates draft brief
- **Tech**: Your Project Scott approach (RAG + LLMs)
- **Savings**: 60-70% of PM time on briefs → repurpose to higher-value work OR reduce 5-8 PMs ($500K-$1M/year)

#### **B. Automated Production Tracking** (50% time reduction)
- **Current**: PMs manually update Airtable with project status, artists manually report progress
- **AI-Automated**: Auto-detection of project milestones, asset completion, bottlenecks from tool usage data
- **Tech**: Event-driven tracking integrated with asset creation tools
- **Savings**: 3-5 PMs ($300K-$650K/year)

#### **C. Auto-Routing & Approval Workflows** (60% time reduction)
- **Current**: PMs manually route assets to brand/legal for approval, chase down feedback
- **AI-Automated**: Smart routing based on asset type, auto-reminders, status aggregation
- **Tech**: Workflow automation + NLP for feedback parsing
- **Savings**: 30-40% of coordination time ($600K-$1.2M/year across team)

**Total PM Savings: $1.4M-$2.8M/year (30-40% headcount reduction)**

---

### 3. Tech Designer Support ($2M-$3M/year) ★★★★☆

**What They Do** (From Interview):
- Day-to-day artist technical support
- Pipeline troubleshooting
- First responders to tool issues
- Handle recurring technical problems

**Team Size**: ~30-40 Tech Designers @ $80K-$120K avg = $2.4M-$4.8M/year

**Current Process**:
- Artists hit technical issue → Slack message or ticket
- Tech Designer investigates & resolves
- Recurring issues escalated to Software Engineering
- Documentation often outdated or missing

**AI Automation Opportunity**:

#### **A. AI Support Chatbot (70% issue resolution)** 
- **Current**: Tech Designer manually answers same questions repeatedly
- **AI-Automated**: RAG-based chatbot handles Tier 1 issues (70% of volume)
- **Tech**: Your Project Scott architecture
- **Savings**: 10-15 Tech Designers ($800K-$1.8M/year)

#### **B. Self-Service Troubleshooting** (40% issue prevention)
- **Current**: Artists wait for Tech Designer to fix issue
- **AI-Automated**: AI detects issue patterns → suggests fixes proactively
- **Tech**: Agentic system monitoring tool logs
- **Savings**: 4-6 Tech Designers ($320K-$720K/year)

#### **C. Automated Documentation Updates** (50% doc maintenance time)
- **Current**: Tech Designers manually write/update documentation
- **AI-Automated**: AI watches tool changes → suggests doc updates → SME approves
- **Tech**: Project Scott's gap detection feature
- **Savings**: 20% of remaining Tech Designer time ($200K-$400K/year)

**Total Tech Support Savings: $1.3M-$2.9M/year (35-45% headcount reduction)**

---

### 4. QA & Validation ($1M-$2M/year) ★★★☆☆

**What They Do** (From Daniel):
- "Automatic validation of renders, like content visuals being generated"
- "Correct size logos, proportions, colors"
- Manual asset review before approval
- Brand guideline compliance checking

**Team Size**: ~15-20 QA artists @ $50K-$80K = $750K-$1.6M/year

**Current Process**:
- Human review of every asset
- Check logos, proportions, colors against brand guidelines
- Flag errors for revision
- Re-check after fixes

**AI Automation Opportunity**:

#### **A. Automated Render Validation** (80% of checks)
- **Current**: Human checks every asset manually
- **AI-Automated**: Computer vision validates logos, sizes, proportions, colors automatically
- **Tech**: Your VTO project approach (color detection, visual properties)
- **Savings**: 10-12 QA positions ($500K-$960K/year)

#### **B. Brand Guideline Compliance Checking** (90% automation)
- **Current**: QA artist references brand guidelines document
- **AI-Automated**: AI knows brand guidelines → auto-flags violations
- **Tech**: Vision models + rule engine
- **Savings**: 2-3 specialized brand QA roles ($100K-$240K/year)

**Total QA Savings: $600K-$1.2M/year (60-70% headcount reduction)**

---

### 5. Game Capture & Replay Systems ($800K-$1.5M/year) ★★★☆☆

**What They Do** (From Daniel):
- "Heavy on game capture, gameplay capture"
- "Specific tools for making cooler shots when capturing from the game"
- Create gameplay footage for trailers

**Team Size**: ~10-15 capture specialists @ $60K-$100K = $600K-$1.5M/year

**Current Process**:
- Manual camera control during gameplay
- Multiple capture attempts to get "perfect" shot
- Manual identification of interesting moments
- Time-consuming replay scrubbing

**AI Automation Opportunity**:

#### **A. AI-Driven Camera Pathing** (60% time reduction)
- **Current**: Human operator controls camera during gameplay capture
- **AI-Automated**: AI identifies interesting moments → optimal camera angles automatically
- **Tech**: ML trained on past successful captures + game state analysis
- **Savings**: 3-5 capture specialists ($180K-$500K/year)

#### **B. Automated Highlight Reel Generation** (70% editing time)
- **Current**: Editor scrubs through hours of footage finding best moments
- **AI-Automated**: AI watches gameplay → flags exciting moments → auto-generates highlight reel
- **Tech**: Event detection ML + auto-editing
- **Savings**: 2-3 editors ($120K-$300K/year)

**Total Capture Savings: $300K-$800K/year (30-40% headcount reduction)**

---

## Part 2: ROI Analysis (Year 1 Impact)

### Immediate Wins (Month 1-6)

**1. Production Brief Automation**
- **Investment**: 3 months dev time = $50K (1/4 your annual salary)
- **Savings**: 5-8 PMs × 60% time = $500K-$1M annually
- **ROI**: 10:1 to 20:1
- **Timeline**: 3 months to production

**2. Render Validation**
- **Investment**: 4 months dev time = $67K
- **Savings**: 10-12 QA positions = $500K-$960K annually
- **ROI**: 7:1 to 14:1
- **Timeline**: 4 months to production

**Total 6-Month Impact**: $1M-$2M annual recurring savings from $117K investment

### Mid-Term Wins (Month 7-12)

**3. Tech Support Automation**
- **Investment**: 4 months dev time = $67K
- **Savings**: 10-15 Tech Designers = $800K-$1.8M annually
- **ROI**: 12:1 to 27:1
- **Timeline**: 4 months to production (after Month 6)

**4. Asset Variation Generation (Pilot)**
- **Investment**: 3 months dev time = $50K
- **Savings**: Pilot phase, 2-3 artists = $150K-$300K annually
- **ROI**: 3:1 to 6:1
- **Timeline**: 3 months pilot

**Total Year 1 Impact**: $2M-$4M annual recurring savings from $234K investment

### Long-Term (Year 2+)

**5. Full Content Generation Pipeline**
- **Investment**: 6-12 months = $100K-$200K
- **Savings**: 30-40% of artist team = $2M-$4M annually
- **ROI**: 10:1 to 40:1
- **Timeline**: 12-18 months

**6. End-to-End Production Automation**
- **Investment**: 6-12 months = $100K-$200K
- **Savings**: Additional PM reduction = $800K-$1.5M annually
- **ROI**: 4:1 to 15:1
- **Timeline**: 12-18 months

**Total Year 2 Impact**: Additional $3M-$6M annual savings

---

## Part 3: Strategic Prioritization

### Tier 1: Build FIRST (Highest ROI, Fastest)

**1. Production Brief Automation** ★★★★★
- **Why First**: Daniel specifically mentioned, clear metrics, fast win
- **Investment**: $50K (3 months)
- **Return**: $500K-$1M/year
- **ROI**: 10:1 to 20:1
- **Political Risk**: LOW (improves PM work, doesn't eliminate immediately)

**2. Render Validation** ★★★★★
- **Why First**: Daniel mentioned, your expertise match, measurable success
- **Investment**: $67K (4 months)
- **Return**: $500K-$960K/year
- **ROI**: 7:1 to 14:1
- **Political Risk**: MEDIUM (reduces QA team but positions as "quality improvement")

### Tier 2: Build NEXT (High ROI, Strategic)

**3. Tech Support Automation** ★★★★☆
- **Why**: Project Scott parallel, builds cross-team collaboration (Rhea's ask)
- **Investment**: $67K (4 months)
- **Return**: $800K-$1.8M/year
- **ROI**: 12:1 to 27:1
- **Political Risk**: HIGH (directly threatens Tech Designer jobs)
- **Mitigation**: Position as "handles boring Tier 1, you do interesting Tier 2/3 work"

**4. Asset Variation Generation (Pilot)** ★★★☆☆
- **Why**: Tests generative AI viability, smaller scope reduces risk
- **Investment**: $50K (3 months pilot)
- **Return**: $150K-$300K/year (pilot scale)
- **ROI**: 3:1 to 6:1
- **Political Risk**: HIGH (threatens creative roles)
- **Mitigation**: Start with tedious variations, not hero assets

### Tier 3: Build LATER (High Impact, Complex)

**5. Full Content Generation Pipeline** ★★★★☆
- **Why**: Highest total savings but needs Tier 2 learnings first
- **Investment**: $100K-$200K (12-18 months)
- **Return**: $2M-$4M/year
- **ROI**: 10:1 to 40:1
- **Political Risk**: VERY HIGH (major artist headcount reduction)
- **Approach**: Build incrementally, pilot extensively, get artist buy-in

**6. Game Capture Automation** ★★☆☆☆
- **Why**: Solid ROI but requires deep Frostbite integration
- **Investment**: $80K-$120K (6-9 months)
- **Return**: $300K-$800K/year
- **ROI**: 4:1 to 10:1
- **Political Risk**: MEDIUM (specialized team, less visible)

---

## Part 4: Where EA is Currently Wasting Money

### Problem Areas (From Interview Analysis)

**1. Duplicated AI/ML Work** (Rhea's Point)
- **Quote**: "Different teams doing different things or the same thing without knowing other teams exist"
- **Cost**: Multiple teams building same tools independently
- **Waste Estimate**: $500K-$1M/year in redundant development
- **Solution**: Your role as bridge-builder + central AI/ML community

**2. Manual Production Tracking** (Airtable Mentioned)
- **Current**: Manual Airtable updates by PMs and artists
- **Waste**: 20-30% of PM time = $600K-$1.2M/year
- **Solution**: Automated tracking from tool usage data

**3. Outdated Documentation** (Implied from Project Scott Discussion)
- **Problem**: Tech Designers answering same questions repeatedly
- **Waste**: 30-40% of Tech Designer time on preventable issues = $700K-$1.4M/year
- **Solution**: Automated documentation + self-service support

**4. Revision Cycles** (Implied from QA Discussion)
- **Problem**: Manual QA catches errors late → expensive revisions
- **Waste**: 10-15% of artist time redoing work = $500K-$1M/year
- **Solution**: Automated validation catches issues earlier

**5. Tool Exploration Without Strategy** (Daniel: "EA paying for many AI products")
- **Problem**: Multiple teams trying different AI tools without coordination
- **Waste**: $200K-$500K/year in unused/redundant tools
- **Solution**: Centralized AI tool evaluation & procurement

**Total Waste: $2.5M-$5M/year** (addressable through better coordination & automation)

---

## Part 5: The Pressure You'll Face

### From Interview Context

**Blaze**: "Battlefield 6 launching tomorrow" (said day before launch)
- **Translation**: High-pressure launch cycles, need tools that work under deadline stress

**Daniel**: "Growing team, hiring multiple roles, org developing"
- **Translation**: Expansion happening NOW, need results to justify continued hiring

**Rhea**: "Multiple AI/ML teams, avoiding silos"
- **Translation**: Company knows it's wasting money on duplication, you're expected to fix this

**All Three**: "Autonomy, no experts on team, figure it out yourself"
- **Translation**: High expectations with limited support

### From Buyout Context

**$20B Debt**: Requires ~$1.5B-$2B annual debt service (assuming 7-8% interest)

**Investor Expectations**: 
- Double-digit EBITDA improvement within 2-3 years
- Marketing spend reduction is low-hanging fruit
- Your role = instrument of that reduction

**Timeline Pressure**:
- Year 1: Prove concept (small wins)
- Year 2: Scale automation (major savings)
- Year 3: Deliver full ROI (justify buyout)

**If You Don't Deliver**: Role eliminated, outside consultants brought in, harsher cuts imposed

---

## Part 6: Recommended Focus

### Your First 90 Days

**Month 1: Research & Quick Win**

Week 1-2: **Cost Center Mapping**
- Interview 30+ people (artists, PMs, Tech Designers)
- Map where time is actually spent (not just what they say)
- Identify the 3-5 most painful, time-consuming tasks
- Calculate current cost of these tasks

Week 3-4: **Production Brief POC**
- Build minimal viable brief generator
- Test on 5-10 past projects
- Demo to Daniel/Blaze with time savings data
- **Goal**: Prove you can deliver fast wins

**Month 2-3: Brief Tool Production + Validation Prototype**

Brief Tool:
- Production deployment
- Integration with Airtable
- Training for PMs
- Track usage & savings

Validation:
- Computer vision model for logo/proportion/color checking
- Test on 100 past assets
- Calculate accuracy vs human QA
- **Goal**: Second production system deployed

**Metrics to Track** (Report Weekly to Daniel/Blaze):
- Time savings per project (their Airtable metric)
- Cost savings (extrapolated annually)
- User adoption rate
- Error/accuracy rates
- Number of headcount-hours saved

### Your Communication Strategy

**To Leadership** (Daniel, Blaze):
- Frame as "accelerate timelines" not "reduce headcount"
- Use their language: "time to create assets" from Airtable
- Show quarterly wins, not just long-term vision
- Emphasize "enables team to do more with current resources"

**To Artists**:
- "These tools handle the tedious parts—you focus on creative work"
- Get their input on what they WANT automated
- Never say "2x productivity" (they hear "half the people needed")
- Build trust before tools that threaten jobs

**To Tech Designers**:
- "AI handles Tier 1 support, you do the interesting Tier 2/3 work"
- Make them co-creators, not victims
- Position as tool managers, not tool users
- Start with documentation, not their replacement

**To Executives** (If Asked):
- "Projected $2M-$4M annual savings within 12 months"
- "3 production systems deployed, 4 more in pipeline"
- "Cross-team collaboration reducing tool duplication waste"
- "Scalable architecture for worldwide franchise rollout"

---

## Part 7: The Honest Answer to Your Question

### Where is EA Spending the MOST Money?

**Answer**: **Artist & Content Creator Labor** ($5M-$10M/year in Marketing Org alone)

**Why This Matters**:
- Every trailer, screenshot, video requires human labor
- EA has DOZENS of franchises launching annually
- Marketing content created for EVERY launch
- Repetitive work across similar asset types
- Manual processes dominate

**Where AI Can Cut Deepest**:
1. **Content generation automation** → 40-50% artist reduction = $2M-$5M/year
2. **Production management automation** → 30-40% PM reduction = $1.4M-$2.8M/year
3. **Tech support automation** → 35-45% Tech Designer reduction = $1.3M-$2.9M/year

**Total Addressable Savings**: $5M-$11M/year from Marketing Org alone

**Scaling Across EA**: If this is just ONE org, and EA has similar structures for:
- Game development studio support
- IT operations
- Customer support
- QA across all games
- **Multiply by 5-10x for company-wide impact**

**Company-Wide AI Savings Potential**: $25M-$100M/year

### Where Will Pressure Fall on YOU?

**Answer**: Production brief automation & render validation FIRST (Tier 1), then content generation pilots (Tier 2)

**Why**:
- Daniel SPECIFICALLY mentioned these as needs
- They're measurable (Airtable metrics)
- Fast ROI (3-6 months)
- Prove your value before tackling harder problems

**Timeline You're On**:
- **Month 6**: Need to show $1M-$2M annual savings potential
- **Month 12**: Need to have $2M-$4M annual savings in production
- **Month 18**: Either promoted for success OR replaced for insufficient ROI

**Reality**: You'll be pushed toward content generation (highest savings) even if you start with production tools. Be ready for that conversation.

---

## Final Answer: Start Here

**Immediate Focus** (Week 1): 
- Map exact breakdown of where Marketing Org spends time (from interviews)
- Quantify current cost of production briefs, render validation, tech support
- Build business case showing ROI for each

**Quick Win** (Month 1):
- Production brief automation POC
- Demonstrate 50-70% time reduction
- Calculate annual savings: $500K-$1M

**Scale** (Month 2-6):
- Brief tool production + render validation
- Both systems deployed & tracked
- Combined savings: $1M-$2M/year

**Prove Value** (Month 6-12):
- Tech support automation
- Asset variation generation pilot
- Total savings: $2M-$4M/year
- Justify role & expansion

**You Asked**: "Where could most money be saved?"

**Answer**: Content creator labor ($5M-$10M/year in your org alone)

**You'll Start With**: Production tools ($1M-$2M/year savings) to prove yourself

**You'll Be Pushed Toward**: Content automation ($2M-$5M/year savings) once you've proven you can deliver

**Be Ready**: This is the pressure you signed up for when you saw "$55B buyout with $20B debt."

Good luck. The math is clear, the path is straightforward, the human cost is real.

