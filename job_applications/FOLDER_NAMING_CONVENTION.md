# Folder Naming Convention

## Structure

Each job application folder follows this pattern:

```
{number}_{Company}__{Role}__{Specialization}
```

### Components:

1. **Number Prefix** (`{number}_`)
   - Sequential numbering for organization
   - Allows easy ordering and reference
   - Example: `2_`, `13_`, `16_`

2. **Company Name** (`{Company}`)
   - Official company name in PascalCase or with underscores for spaces
   - Immediately follows the number prefix
   - Example: `Electronic_Arts`, `Scribd`, `Cresta`, `Kardium`

3. **Role Title** (`__{Role}`)
   - Separated from company by double underscore `__`
   - Main position title
   - Example: `Full_Stack_Software_Engineer`, `Senior_Software_Build_Engineer`

4. **Specialization/Team** (`__{Specialization}`)
   - Additional double underscore `__` separator
   - Specific team, technology focus, or specialization
   - Example: `ML_Cloud_Applications`, `Backend_Data_Pipelines`, `AI_Agent`

## Examples:

```
job_applications/
├── 2_Electronic_Arts__Full_Stack_Software_Engineer__ML_Cloud_Applications/
├── 9_Kardium__Senior_Software_Build_Engineer/
├── 13_Scribd__Software_Engineer_II__Backend_Data_Pipelines/
└── 16_Cresta__Forward_Deployed_Engineer__AI_Agent/
```

## Benefits:

- **Flat structure**: No nested company/role folders
- **Scannable**: All applications visible at one level
- **Parseable**: Double underscore clearly separates logical components
- **Sortable**: Number prefix allows custom ordering
- **Descriptive**: Full context in folder name alone

## Legacy Structure (Deprecated):

Previous nested structure:
```
{number}_{Company}/{number}_{Role}/
```

This has been flattened for improved navigation and clarity.

