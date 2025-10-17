# Archived Scripts

This directory contains scripts that are no longer compatible with the current repository structure.

## Archived Scripts

### `organize_assets.py` 
**Archived:** October 17, 2025  
**Reason:** Designed for nested `Company/Role/` folder structure. Repository now uses flat `Company__Role__Team/` naming convention.

**Original Purpose:** 
- Created `Role_RAW/` sibling folders for each role
- Moved raw assets (PDFs, audio, images, raw JDs) from role folders to RAW folders
- Cleaned up empty RAW folders

**Why Obsolete:** 
- Assumes nested directory structure no longer in use
- Iterates through company folders looking for nested role folders
- RAW folder naming logic incompatible with flat structure

---

### `restructure_raw_folders.py`
**Archived:** October 17, 2025  
**Reason:** Designed for nested `Company/Role/_RAW/` subfolder structure. Repository now uses flat naming.

**Original Purpose:**
- Found `_RAW/` subfolders within role folders
- Moved them to sibling folders at company level
- Deleted empty `_RAW/` subfolders

**Why Obsolete:**
- Assumes `Company/Role/_RAW/` nested structure
- Incompatible with current flat `Company__Role__Team/` naming
- No longer needed after folder restructure completed

---

## Current Repository Structure

As of October 17, 2025:

```
job_applications/
├── 2_Electronic_Arts__Full_Stack_Software_Engineer__ML_Cloud_Applications/
├── 9_Kardium__Senior_Software_Build_Engineer__Globe_System/
├── 13_Scribd__Software_Engineer_II__Backend_Plus_Pipelines/
└── 16_Cresta__Forward_Deployed_Engineer__AI_Agent/
```

**Pattern:** `{num}_{Company}__{Role}__{Team}`

See `job_applications/FOLDER_NAMING_CONVENTION.md` for details.

---

## Future Script Development

If creating new organizational scripts, reference:
- `/job_applications/FOLDER_NAMING_CONVENTION.md` - current naming rules
- Flat structure (single level, no nesting)
- Double underscore (`__`) separates logical components

