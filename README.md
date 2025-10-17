# Career Automation

Systematic approach to job applications with AI-powered interview prep, resume optimization, and comprehensive tracking.

## Repository Structure

### 📁 job_applications/
All job applications organized by company (17 companies total). Each company has numbered role folders with:
- **Processed folders** (for AI context): Job descriptions (formatted), interview prep guides, transcripts & analysis
- **RAW folders** (not for AI): Original job descriptions, PDFs, audio files, resumes & cover letters

**Example:** 
- `job_applications/13_Scribd/1_Software_Engineer_II_Backend_Data_pipelines/` (processed)
- `job_applications/13_Scribd/1_RAW_Software_Engineer_II_Backend_Data_pipelines/` (raw files)

### 📚 _references/
Guidance documents and instructions:
- `commit_message_guidance.md` - Git commit standards
- `CURSOR_CONTEXT_NOTES.md` - AI assistant context
- `INTERVIEW_LEARNINGS_MASTER.md` - Interview insights
- `META_INSTRUCTIONS_Prep_Guide_Creation.md` - Prep guide templates
- `PREP_GUIDES_REFERENCE.md` - Reference materials

### ⚙️ _scripts/
Automation tools:
- `organize_assets.py` - Organize PDFs, audio files into _RAW folders
- `restructure_raw_folders.py` - Move _RAW subfolders to company-level siblings
- `add_date_suffix.py` - Add date prefixes to files for chronological sorting
- `change_pdf_metadata.py` - PDF metadata modification
- `convert_qta_to_wav.py` - Audio format conversion

### ✅ _todo/
Task tracking:
- `todo.md` - Active tasks
- `todo_archive.md` - Completed tasks

### 🎯 _initiatives/
Active projects for improving the career automation process:
- `1_Learning_About_Aviral_Garg/` - User profiling and sorted QA methodology
- `2_Repository_Context_Optimization/` - Token reduction and AI context efficiency

### 🗄️ _archive/
Historical project files and experiments (not actively used).

## File Organization

**RAW vs Processed:**
- **Processed folders** (for AI context): Markdown prep guides, formatted JDs, interview notes, analysis
- **RAW folders** (not for AI): PDFs, audio files, raw job descriptions, images, resumes

This separation improves AI context management - processed folders contain only AI-consumable content.

## Usage

Each job application follows a systematic pipeline:
1. Raw JD capture → `[Company]/[Role_RAW]/Task_1_raw_jd.txt`
2. Formatted JD → `[Company]/[Role]/Task_2_formatted_jd.md`
3. Interview prep guides (numbered markdown files in processed folder)
4. Transcripts and analysis (processed folder)
5. Audio/PDFs → `[Company]/[Role_RAW]/`

## Technologies

- Python automation scripts
- Markdown for documentation
- Git for version control

