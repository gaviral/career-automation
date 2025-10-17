# Career Automation

Systematic approach to job applications with AI-powered interview prep, resume optimization, and comprehensive tracking.

## Repository Structure

### 📁 _companies/
All job applications organized by company (17 companies total). Each company has numbered role folders with:
- Job descriptions (raw & formatted)
- Interview prep guides
- Transcripts & analysis
- Resumes & cover letters in `_ASSETS/` subfolder

**Example:** `_companies/13_Scribd/1_Software_Engineer_II_Backend_Data_pipelines/`

### 📚 _reference/
Guidance documents and instructions:
- `commit_message_guidance.md` - Git commit standards
- `CURSOR_CONTEXT_NOTES.md` - AI assistant context
- `INTERVIEW_LEARNINGS_MASTER.md` - Interview insights
- `META_INSTRUCTIONS_Prep_Guide_Creation.md` - Prep guide templates
- `PREP_GUIDES_REFERENCE.md` - Reference materials

### ⚙️ _scripts/
Automation tools:
- `organize_assets.py` - Organize PDFs, audio files into _ASSETS folders
- `change_pdf_metadata.py` - PDF metadata modification
- `convert_qta_to_wav.py` - Audio format conversion

### ✅ _todo/
Task tracking:
- `todo.md` - Active tasks
- `todo_archive.md` - Completed tasks

### 🗄️ _archive/
Historical project files and experiments (not actively used).

## File Organization

**Assets vs Prep Materials:**
- **Prep materials** (top-level): Markdown prep guides, notes, analysis
- **Assets** (_ASSETS/ subfolder): PDFs, audio files, raw job descriptions, images

This separation improves AI context management and file navigation.

## Usage

Each job application follows a systematic pipeline:
1. Raw JD capture → `_ASSETS/Task_1_raw_jd.txt`
2. Formatted JD → `Task_2_formatted_jd.md`
3. Interview prep guides (numbered files)
4. Transcripts and analysis
5. Final materials (resumes/cover letters) → `_ASSETS/`

## Technologies

- Python automation scripts
- Markdown for documentation
- Git for version control

