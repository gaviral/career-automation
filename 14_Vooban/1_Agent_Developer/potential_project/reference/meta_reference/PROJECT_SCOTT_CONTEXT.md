# Project Scott - Context & Background

**Source**: Vooban Recruiter Screen Interview (October 7, 2025)

## Project Overview

Project Scott is an AI-powered documentation agent built at Amazon's Beauty Tech organization. It revolutionized team onboarding and knowledge management by providing instant, intelligent answers to documentation questions.

## Core Problem Solved

**The Pain Point**: Lack of comprehensive, up-to-date documentation - a common problem across software organizations that slows onboarding, creates bottlenecks, and wastes developer time.

## How Project Scott Works

### 1. Question Answering Flow
- New team members ask questions directly in Slack
- Scott performs documentation lookup using RAG (Retrieval Augmented Generation)
- Returns relevant documentation instantly

### 2. Intelligent Gap Handling
When documentation is missing or incomplete:
- **Partial Match**: Identifies specific documentation gaps
- **Zero Match**: No relevant documentation found
- **Inferred Match**: Information exists but requires logical reasoning across multiple docs

### 3. Automated Documentation Creation
Instead of just reporting gaps, Scott:
- Contacts subject matter experts for specific topics
- Asks concrete, targeted questions (not generic requests)
- Collects answers
- Auto-generates documentation
- Updates vector database
- Responds to original question with newly created docs

### 4. Ticketing System Integration
- Connected to internal ticketing system
- Monitors new tickets
- Answers questions automatically where possible
- Learns from developer comments and responses
- Continuously improves documentation coverage

### 5. Code Integration (Coding Agents)
- Monitors pull requests
- Reviews code changes for documentation value
- Automatically adds relevant code documentation to repository
- Maintains documentation-code sync

## Technical Stack

- **Framework**: OpenAI Agents Python SDK (open source)
- **Architecture**: Multi-agent system
- **Retrieval**: Vector databases for semantic search
- **Classification**: Topic classification models (initially third-party, later replaced with local Ollama models)
- **Integration**: Slack API, internal ticketing system
- **Infrastructure**: AWS (Amazon)
- **Languages**: Python, LangChain

## Development Approach

### Origin Story
1. Identified documentation as persistent pain point across multiple companies
2. Started as personal experiment with dummy documents
3. Created prototype with vector database
4. Proposed one-pager to manager → gained immediate traction
5. Organization-wide initiative launched

### Pre-Project Foundation
- Led documentation cleanup initiative across Beauty Tech org
- Created reference table mapping topics to subject matter experts (SMEs)
- Established ownership structure for different documentation areas
- Conducted workshops to assign topic owners
- This infrastructure became perfect launchpad for Scott

### Development Process
- Led team of 3 developers + 1 ML engineer
- Worked with cross-functional stakeholders (data scientists, BI engineers)
- Multiple system design iterations
- Team-wide reviews with senior engineers & AI engineers from other teams
- Design proposal + modifications → final implementation
- Extensive red-teaming and experimentation

### Advanced Engineering
- Developed custom prompt engineering techniques to overcome context window limits
- Implemented context caching strategies
- Achieved 8M token conversations in 200K token model
- Built on top of OpenAI API (not just wrapper)

## Impact Metrics

- **82% reduction** in ticket resolution times
- **240+ dev hours saved** per month
- **100% documentation completion** achieved
- Freed developers to focus on coding instead of documentation hunting
- Eliminated bottleneck of onboarding new team members

## Team & Leadership

- **Role**: Led by Aviral (first agent developer at Amazon Beauty Tech)
- **Team Size**: 3 developers, 1 ML engineer
- **Scope**: Organization-wide (entire Beauty Tech org)
- **Ownership**: Full SDLC - requirements engineering → maintenance
- **Stakeholders**: Product managers, developers, data scientists, BI engineers

## Key Innovations

1. **Proactive Gap Filling**: Doesn't just report missing docs, actively creates them
2. **SME Integration**: Intelligent routing to right experts with specific questions
3. **Multi-System Integration**: Slack + ticketing + PR reviews
4. **Self-Improving**: Learns from responses and continuously updates
5. **Context Engineering**: Advanced techniques to exceed standard LLM limitations

## Amazon Beauty Tech Context

**Product**: Virtual makeup try-on feature on Amazon app
- Users can try on lipsticks, foundations, makeup products
- Requires 3D lip models + accurate color/texture properties

**Technical Challenge Solved by Team**:
- Inconsistent color naming (e.g., "unicorn red")
- Non-standard texture descriptions (large/medium/small particles)
- Extracted visual properties from 40+ terabytes of product images daily
- Served 40M+ customers monthly

## Project Scott's Role in Beauty Tech

Enabled seamless knowledge sharing about:
- Visual properties pipeline
- Makeup rendering systems
- Data processing workflows
- Team processes & standards
- Technical architecture decisions

Made it easy for new team members to ramp up on complex, specialized systems without repeatedly bothering SMEs or hunting through incomplete docs.

---

**Note**: This local version of Project Scott will use dummy documentation from a similar domain (Amazon Beauty Tech) to demonstrate the core concepts with realistic examples.

