# Job Applications Subproject Instructions

## 0. Strategic Mission & Vision

### 0.1 Subproject Definition & Context
This document contains instructions for executing the **Job Applications Subproject** - a strategic career acceleration initiative that transforms candidates into optimal job applicants through systematic AI-powered enhancement and strategic positioning.

### 0.2 Core Mission Statement
Maximize hireability through strategic personal project development. Create compelling resume content demonstrating technical mastery. All tasks work backwards from: **maximum hireability through impressive technical demonstration**.

### 0.3 Available AI Resources & Capabilities
- **Ultra-Deep Thinking Mode** - Rigorous multi-angle analysis with triple verification for complex strategic decisions

### 0.4 Candidate Context & Development Profile

#### High-Achievement Baseline
Candidate demonstrates strong technical capabilities:
- **Proven Achievement Pattern**: High achievement baseline with measurable impact
- **Enterprise Experience**: Production experience with large-scale systems
- **Technical Foundation**: Strong background in AI/ML, full-stack development, cloud architecture, and production deployment

#### Personal Project Impact Framework
- **Technical Capability**: Project complexity driven by hiring manager impact and relevant expertise demonstration
- **Practical Constraints**: Avoid impractical claims (multi-terabyte processing, 40x improvements)
- **Quantification Realism**: Use impressive but achievable metrics appropriate for personal projects
- **Project Clarity**: Resume points must clearly communicate project purpose and functionality
- **Scope Realism**: Maintain realistic adoption/visibility metrics for personal project scope

#### Development Philosophy & Standards
- **Ultra-Deep Thinking Mode**: Strategic tasks require rigorous multi-angle analysis with triple verification
- **High Achievement Standards**: Maintain ambitious technical goals that impress hiring managers
- **Innovation Leadership**: Focus on cutting-edge technologies and competitive differentiation
- **Quantified Excellence**: Emphasis on measurable technical improvements and performance optimizations
- **Technical Performance Focus**: Prioritize technical capability metrics over user adoption metrics

#### Instruction Development Context
- **Generic Instructions, Job-Specific Execution**: Instructions remain universally applicable while execution tailors to specific requirements
- **Context Preservation Priority**: Preserve critical contextual information for strategic alignment
- **Hiring Manager Psychology**: Prioritize immediate hiring appeal and psychological impact
- **Success Pattern Replication**: Follow proven achievement patterns (quantified impact + business value + differentiation)
- **Practical Quantification Standards**: Technical achievements impressive but grounded - avoid impractical claims
- **Project Purpose Clarity**: Resume points must clearly communicate project purpose, not just technical details
- **Comparative Context Requirements**: Metrics need clear baseline comparison - avoid vague claims
- **Personal Project Scope Realism**: Acknowledge individual development constraints
- **End Goal Focus**: All tasks work backwards from maximum hireability


### 0.5 Claude-4-Sonnet Prompting Best Practices

**Effective Instruction Techniques for Claude-4-Sonnet:**
1. **Concise Clarity**: Remove verbose language while preserving essential information
2. **Action-Oriented Directives**: Use imperative verbs (Read, Create, Apply, Analyze) 
3. **Structured Organization**: Headers, bullets, numbered lists for easy parsing
4. **Explicit Constraints**: State character limits, formatting requirements clearly
5. **Priority Indicators**: Mark critical requirements with **HIGH PRIORITY**
6. **Sequential Processing**: Break complex tasks into ordered steps
7. **Specific Deliverables**: Define exact file names and output formats
8. **Context Preservation**: Maintain strategic context while eliminating redundancy
9. **Verification Requirements**: Include quality check steps
10. **Iterative Optimization**: Allow step-by-step refinement

**This Section 0 serves as the central repository for all strategic thinking, future enhancements, and evolutionary development of the Job Applications Subproject. Additional tasks will be incrementally added to implement these comprehensive capabilities.**

## Task_1: Job Description Placement Task

### 1.1 Task
This task involves placing the job description content into the `raw_jd.txt` file inside a newly created temp folder. 

### 1.2 Implementation Notes
- This task is handled by a Python script automatically
- The script assumes the user has already copied the job description from a website to their clipboard
- The script creates a new temporary folder inside `data/job_applications_subproject/` folder
- The script creates a `Task_1_raw_jd.txt` file and puts the clipboard content into this raw file
- These instructions are for reference purposes only

## Task_2: Job Description Formatting Instructions

### 2.1 Task
Take the content from `data/job_applications_subproject/temp/Task_1_raw_jd.txt` and create a formatted markdown version called `Task_2_formatted_jd.md` in the same directory.

### 2.2 HIGH PRIORITY Requirements
1. **Preserve all information** - Every detail from raw file must be maintained
2. **No content modification** - Keep original text exactly as written
3. **No additions** - Only reorganize and format existing content
4. **No summarization** - Pure formatting exercise, not content modification

### 2.3 Step-by-Step Instructions
1. **Read** the raw job description from `data/job_applications_subproject/temp/Task_1_raw_jd.txt`

2. **Identify all headings** in the raw text and convert them to proper markdown headers:
   - Use `#` for the main job title
   - Use `##` for major sections
      - Use `###` for subsections when needed

3. **Organize content logically** by grouping related information together while maintaining the original text exactly

4. **Apply basic markdown formatting**:
   - Convert lists to bullet points or numbered lists
   - Use **bold** for important labels and keywords
   - Maintain proper spacing and structure
   - Use tables if appropriate for structured data

5. **Create** the formatted file at `data/job_applications_subproject/temp/Task_2_formatted_jd.md`

6. **Preserve exact original wording** - maintain readability while keeping all text identical to source

### 2.4 Output Format
Well-structured markdown document with:
- Clear section hierarchy
- Every original detail preserved
- Professional readability
- Standard markdown formatting

## Task_3: Company and Job Title Extraction with Folder Organization

### 3.1 Task
Extract the company name and job title from the formatted job description, then organize the temp folder appropriately within the company structure using proper numbering.

### 3.2 Step-by-Step Instructions

#### 3.2.1 Extract Information
1. **Read** the formatted job description from `data/job_applications/temp/Task_2_formatted_jd.md`
2. **Extract** the company name (look for company field, EA Sports, Electronic Arts, etc.)
3. **Extract** the job title/role name (e.g., "Machine Learning Engineer")

#### 3.2.2 Company Matching and Verification
1. **List** all existing company folders in `data/job_applications_subproject/` directory
2. **Compare** extracted company name with existing folder names using fuzzy matching logic:
   - "ABC Company" and "ABC Company Limited" = same company
   - "ABC" and "ABC Limited" = same company
      - "ABC Company" and "XYZ Company" = different companies
3. **Verify online** only if there is a potential conflict between company names with existing folders
4. **Decision**: 
   - If match found: Use existing company folder
   - If no match: Create new company folder following naming conventions

#### 3.2.3 Job Application Numbering
1. **Navigate** to the company folder (existing or newly created)
2. **List** all existing job application folders with their numeric prefixes (1_, 2_, 3_, etc.)
3. **Determine** the next available number in sequence
4. **Rename** temp folder to: `{next_number}_{job_title}`
   - Example: `2_Machine Learning Engineer`

#### 3.2.4 Folder Organization
1. **Move** the renamed folder from `data/job_applications_subproject/temp/` to `data/job_applications_subproject/{company_name}/`
2. **Verify** the folder structure is correct
3. **Confirm** all files (Task_1_raw_jd.txt and Task_2_formatted_jd.md) are preserved in the moved folder


### 3.4 Company Folder Naming Conventions
1. **Company Numbering**: All company folders must have numeric prefixes (1_, 2_, 3_, etc.)
2. **Spaces**: Replace all spaces with underscores in company and job role names
3. **Name Simplification**: For new company folders, use commonly referred names:
   - Remove suffixes like "Limited", "Inc", "Corporation", "LLC", etc.
   - Search online for most commonly used name if uncertain
   - If no common name found, use extracted name from job description
4. **Existing Folders**: Apply numbering based on creation order

### 3.5 Important Notes
- Use fuzzy matching for company names (handle variations like "Inc", "Ltd", "Limited", "Company")
- Maintain chronological numbering for job applications to same company
- Preserve all files during folder moves
- Create company folders if they don't exist
- Verify company name accuracy through web search only when conflicts exist
- All folder names should use underscores instead of spaces

## Task_4: Streamline Job Description

**Objective:** Create streamlined version removing verbose language while preserving critical context for project ideation.

**HIGH PRIORITY Requirements:**
- Preserve team/company context, technical environments, all requirements/frameworks
- Remove redundant phrases, filler words, generic corporate language
- Maintain technical accuracy and strategic alignment information

**Process:**
1. Read `Task_2_formatted_jd.md`
2. Preserve: Team context, company/industry context, technical environments, all requirements
3. Remove: Redundant phrases, verbose descriptions, generic qualifiers
4. Create `Task_4_formatted_jd.md`

## Task_5: Structure Information Extraction

**Objective:** Extract streamlined job description into key-value format maintaining reading sequence.

**HIGH PRIORITY Requirements:**
- Maintain reading sequence, allow repeated keys, capture every sentence
- Categories: Role, Team, Company Context, Skills (repeated), Core Technology Stack (repeated)

**Process:**
1. Read `Task_4_formatted_jd.md`
2. Process sequentially by sentence/section
3. Categorize using key-value format with repeated keys allowed
4. Create `Task_5_structured_requirements.md`

**Output Format:**
```
- Role: [Job Title]
- Team: [Team/Department]
- Company Context: [Industry/Company Type]
- Skills: [Responsibility/Skill 1]
- Skills: [Responsibility/Skill 2]
```

## Task_6: Group Key-Value Pairs

**Objective:** Group repeated keys into indented bullet lists maintaining sequence.

**HIGH PRIORITY Requirements:**
- Maintain sequence, group by keys, use indented bullets
- Include Company Context, Hiring Team Context, Role Context (empty if needed)
- No content changes, only structural reorganization

**Process:**
1. Read `Task_5_structured_requirements.md`
2. Group repeated keys maintaining original sequence
3. Convert to indented bullet format
4. Create `Task_6_grouped_requirements.md`

**Output Format:**
```
- Role: [Job Title]
- Company Context:
  - [Company/Industry Info]
- Skills:
  - [Skill/Responsibility 1]
  - [Skill/Responsibility 2]
```

## Task_7: Expand Technology Lists

**Objective:** Expand technology mentions into nested bullet structure for clarity.

**HIGH PRIORITY Requirements:**
- Identify technology lists in Skills, preserve original context
- Use nested bullets for technology arrays, no content loss

**Process:**
1. Read `Task_6_grouped_requirements.md`
2. Find phrases like "using X, Y, Z" or "with A, B, C" 
3. Restructure: keep main description, add colon, nest technologies
4. Create `Task_7_technology_expanded.md`

**Format Example:**
```
- Skills:
  - Design workflows using:
    - [Technology 1]
    - [Technology 2]
```

## Task_8: Convert to Table Format

**Objective:** Convert all content to two-column table structure.

**HIGH PRIORITY Requirements:**
- Complete table conversion, preserve all content exactly
- Include Company Context, Hiring Team Context, Role Context, Skills
- One row per bullet point, preserve indentation with &nbsp; spaces

**Process:**
1. Read `Task_7_technology_expanded.md`
2. Extract all sections into table format
3. Column 1: Requirements with indentation, Column 2: Empty
4. Create `Task_8_skills_table.md`

**Format:**
```
| Requirement | Notes |
|---|---|
| **Skills** | |
| Design workflows using: | |
| &nbsp;&nbsp;&nbsp;&nbsp;Technology 1 | |
```

## Task_9: Map Project Ideas

**Objective:** Fill table's second column with unified project strategy demonstrating all requirements.

**HIGH PRIORITY Requirements:**
- **Ultra-Deep Thinking Mode**: Comprehensive analysis required
- Cohesive strategy, one-to-one mapping, demonstrable projects
- Practical implementation, strategic alignment with hiring appeal

**Process:**
1. Read `Task_8_skills_table.md`
2. **Ultra-Deep Analysis**: Analyze holistically, identify themes/clusters, plan cohesive ecosystem
3. Change header "Notes" to "Project Idea" 
4. Create unified project strategy aligned with company context
5. Fill systematically with interconnected project components
6. Create `Task_9_project_ideas.md`

**Include Strategic Analysis Summary** explaining unified approach.

## Task_10: Synthesize Detailed Project

**Objective:** Combine all project ideas into comprehensive detailed project description.

**HIGH PRIORITY Requirements:**
- **Ultra-Deep Thinking Mode**: Apply rigorous analysis
- Comprehensive integration, technical depth, business value
- Strategic alignment with all job requirements and company context

**Process:**
1. Read `Task_9_project_ideas.md`
2. Apply Ultra-Deep Thinking Mode for synthesis
3. Copy `Task_9_project_ideas.md` to `pipeline_report.md` as starting point
4. Add comprehensive detailed project description section below existing table
5. Include technical implementation approach, architecture, and business value
6. Continue working with `pipeline_report.md` for all subsequent tasks

## Task_11: Create 6-Point Summary

**Objective:** Create concise 6 bullet point project summary highlighting key accomplishments.

**HIGH PRIORITY Requirements:**
- **Ultra-Deep Thinking Mode**: Apply rigorous analysis
- Maximum 6 points, comprehensive coverage, strategic focus
- Clear communication, immediately understandable points
- **Proper Punctuation**: End each bullet point with a full stop (period)

**Process:**
1. Continue working with `pipeline_report.md`
2. Apply Ultra-Deep Thinking Mode for strategic summarization
3. Identify 6 most impactful accomplishments
4. Add concise 6-point summary section at document bottom
5. **Ensure proper punctuation**: Each bullet point must end with a full stop
6. Update file continues as `pipeline_report.md`

## Task_12: Optimize Character Count (<715)

**Objective:** Optimize 6 points to under 715 total characters while maintaining technical impact.

**HIGH PRIORITY Requirements:**
- **Ultra-Deep Thinking Mode**: Apply rigorous analysis
- Under 715 characters total, no bullet symbols
- Remove bold formatting and business metrics, maintain technical focus
- **Proper Punctuation**: Each line must end with a full stop (period)
- **Pipeline Report Formatting**: Plain text format without bullets or bold formatting
- **Accurate Character Counting**: Count only actual content without formatting overhead

**Process:**
1. Continue working with `pipeline_report.md`
2. Apply Ultra-Deep Thinking Mode for optimization
3. Create optimized version of 6-point summary in plain text format
4. **Character counting optimization**: Count only plain text content without formatting characters
5. Remove formatting, bullets, bold text, business metrics
6. Optimize language preserving technical impact
7. **Iterative optimization**: If over 715 characters, remove least critical content one element at a time
8. **Add full stops**: Ensure each line ends with a period
9. **Verify under 715 characters**: Count plain text content including punctuation
10. Add optimized summary as new section in same file with plain text formatting
11. **Resume transfer later**: Task 16 will transfer optimized project to resume with proper formatting

## Task_13: Resume Integration

### 13.1 Task
Copy the resume file to current working folder and integrate skills section with project summary.

### 13.2 HIGH PRIORITY Requirements
1. **Resume Copy**: Copy `Aviral_Garg_Resume.md` from job_applications_subproject to current working folder
2. **Skills Integration**: Extract skills section from copied resume and add to `pipeline_report.md`
3. **Two-File Approach**: Work with both project file and resume file going forward
4. **Pipeline Report Formatting**: In `pipeline_report.md`, remove bullet points (asterisks/dashes) and bold formatting from skills section
5. **Resume Formatting**: Maintain standard bullet points and formatting in resume file

### 13.3 Step-by-Step Instructions
1. **Use command line to copy resume**: Execute the following command to copy the resume file from the job_applications_subproject folder to the current working folder:
   ```
   cp data/job_applications_subproject/Aviral_Garg_Resume.md data/job_applications_subproject/{company_name}/{job_title}/
   ```
   Where {company_name} and {job_title} are replaced with actual folder names (e.g., `10_Capgemini_Engineering/1_Artificial_Intelligence_Engineer/`)
2. **Extract skills**: Read skills section from the copied resume file in current working directory
3. **Integrate skills**: Add skills section to `pipeline_report.md` as new section with plain text formatting (no bullets, no bold)
4. **Format for pipeline report**: Remove asterisks, dashes, and bold formatting from skills section
5. **Continue with two files**: Pipeline report file and resume file for subsequent tasks

## Task_14: Project Title and Skills Integration

### 14.1 Task
Add project title to optimized summary and integrate project skills into resume skills section.

### 14.2 HIGH PRIORITY Requirements
1. **Project Title**: Give the project a clear, compelling title following resume project naming patterns
2. **Skills Integration Priority**: Follow strict priority order for skills addition
3. **Job Description First**: Prioritize skills explicitly mentioned in job requirements
4. **Project Skills Second**: Add supporting project skills that enhance job relevance
5. **No New Lines**: Integrate skills within existing skill categories without adding new bullet points
6. **Technical Focus**: Maintain focus on technical capabilities and frameworks used

### 14.3 Step-by-Step Instructions
1. **Add project title** to optimized summary in `pipeline_report.md`
2. **Read job description** from `Task_2_formatted_jd.md` to identify required skills
3. **Priority 1 - Job Description Skills**: Add skills explicitly mentioned in job requirements:
   - LangChain, CrewAI, Google's Agent Development Kit, Autogen (required frameworks)
   - Plotly, D3.js, Matplotlib (required charting libraries)
   - SQL (required for data lakes/warehouses)
   - Intent Recognition, Query Parsing (NLP techniques mentioned)
4. **Priority 2 - Supporting Project Skills**: Add project skills that enhance job relevance:
   - Additional databases (Redis, PostgreSQL, MongoDB, ClickHouse)
   - Additional cloud services that support the project
   - Additional development tools that demonstrate capability
5. **Enhance skills in pipeline report**: Add prioritized skills to Skills Section Integration in plain text format
6. **Keep resume unchanged**: Resume skills will be updated later in Task 16 with optimized content

## Task_15: Optimize Skills (<720 chars)

**Objective:** Optimize skills section to under 720 characters by removing least job-relevant skills.

**HIGH PRIORITY Requirements:**
- Under 720 characters total, job relevance priority, iterative removal
- **Optimize in Pipeline Report**: Perform optimization in plain text format in pipeline report first
- Preserve structure, strategic removal prioritizing job-mentioned skills
- Accurate character counting without formatting overhead

**Process:**
1. **Work in pipeline report**: Read skills from Skills Section Integration in `pipeline_report.md`
2. **Count characters**: Count only the plain text content (no bullets, asterisks, bold formatting)
3. **Iterative optimization**: If over 720, remove one least job-relevant skill at a time
4. **Recount after each removal**: Verify character count after each change
5. **Job relevance priority**: Preserve all job-mentioned technologies (LangChain, CrewAI, Google Agent Kit, Autogen, Plotly, D3.js, Matplotlib)
6. **Update pipeline report**: Keep optimized skills in Skills Section Integration
7. **Resume will be updated later**: Task 16 will transfer optimized skills to resume with proper formatting

**Priority:** Job-mentioned > Same category > Complementary > Unrelated

**Character Counting Note:** Plain text format ensures accurate counting without formatting characters that don't contribute to actual content length.

## Task_16: Integrate Resume Updates

**Objective:** Transfer optimized skills and project summary to resume with proper formatting.

**HIGH PRIORITY Requirements:**
- **Transfer optimized skills**: Copy optimized skills from pipeline report to resume with proper resume formatting
- Add optimized project as first project, maintain formatting consistency
- Preserve all other resume content and structure
- **Proper Punctuation**: Ensure all bullet points end with full stops (periods)

**Process:**
1. **Read optimized skills**: Get optimized skills from Skills Section Integration in `pipeline_report.md`
2. **Update resume skills**: Replace resume skills section with optimized content using proper resume formatting (bullets, bold)
3. **Read optimized project**: Get optimized project summary from `pipeline_report.md`
4. **Add project to resume**: Add project summary as first project in resume file
5. **Follow existing resume formatting**: Use bullets, bold formatting, proper punctuation
6. **Add full stops**: Ensure each bullet point ends with a period
7. **Verify consistency**: Ensure project title and content align with resume style

## Task_17: Analyze Resume Gaps

**Objective:** Compare final resume against job requirements, identify and rank remaining gaps.

**HIGH PRIORITY Requirements:**
- Comprehensive comparison, gap identification, priority ranking
- Strategic analysis considering hiring manager impact

**Process:**
1. Read updated resume file
2. Read job description from `Task_2_formatted_jd.md`
3. Analyze each job requirement against resume content
4. Identify gaps where resume inadequately addresses requirements
5. Rank gaps biggest to smallest by role importance and hiring impact
6. Add gap analysis section to `pipeline_report.md`

## Task_18: Finalize Pipeline Report Structure

**Objective:** Move final project summary and enhanced skills sections to the bottom of pipeline report.

**HIGH PRIORITY Requirements:**
- Reorganize `pipeline_report.md` for optimal structure
- Move final versions of project and skills to document end
- **Use Enhanced Skills**: Use the optimized skills section from resume file (includes project-specific technologies)
- Maintain all content while improving organization

**Process:**
1. Continue working with `pipeline_report.md`
2. Move optimized project summary section to bottom of document as "Final Project Summary"
3. **Read enhanced skills from resume file** (not from earlier pipeline report sections)
4. Add enhanced skills section to bottom as "Final Skills Section" with plain text formatting
5. Ensure skills include all project-specific technologies: LangChain, CrewAI, Google Agent Kit, Autogen, Plotly, D3.js, Matplotlib, Intent Recognition, Query Parsing, etc.
6. Ensure final structure: Analysis → Gap Analysis → Final Project → Final Skills
7. Verify all content preserved and enhanced skills are correctly included

