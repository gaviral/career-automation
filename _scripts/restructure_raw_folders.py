#!/usr/bin/env python3
"""
Restructure job application folders to separate raw files at company level.

Before:
  Company/Role/_RAW/   (raw files inside role folder)
  Company/Role/*.md    (processed files)

After:
  Company/Role/        (only processed files)
  Company/Role_RAW/    (only raw files, sibling to Role/)
"""

import os
import shutil
from pathlib import Path

def restructure_raw_folders():
    """
    For each job role folder with _RAW subfolder:
    1. Create sibling folder with _RAW_ prefix
    2. Move contents of _RAW/ to sibling folder
    3. Delete empty _RAW/ subfolder
    """
    base_dir = Path(__file__).resolve().parent.parent  # career-automation root
    companies_dir = base_dir / 'companies'
    
    if not companies_dir.exists():
        print(f"Error: {companies_dir} does not exist")
        return
    
    results = {
        'processed': [],
        'skipped': [],
        'errors': []
    }
    
    # Find all job role folders with _RAW subfolders
    for company_folder in sorted(companies_dir.iterdir()):
        if not company_folder.is_dir():
            continue
        
        # Skip special folders
        if company_folder.name.startswith('.') or company_folder.name == '_archive':
            continue
        
        for role_folder in sorted(company_folder.iterdir()):
            if not role_folder.is_dir():
                continue
            
            # Skip folders that already are _RAW folders
            if '_RAW_' in role_folder.name:
                continue
            
            raw_subfolder = role_folder / '_RAW'
            if not raw_subfolder.exists() or not raw_subfolder.is_dir():
                results['skipped'].append(str(role_folder.relative_to(companies_dir)))
                continue
            
            # Check if _RAW has any files
            raw_files = list(raw_subfolder.iterdir())
            if not raw_files:
                print(f"  • {role_folder.name}: _RAW is empty, deleting...")
                raw_subfolder.rmdir()
                results['skipped'].append(str(role_folder.relative_to(companies_dir)))
                continue
            
            # Create sibling _RAW folder name
            # e.g., "2_Full_Stack_Engineer" -> "2_RAW_Full_Stack_Engineer"
            role_name = role_folder.name
            raw_role_name = role_name.replace('_', '_RAW_', 1)  # Replace first underscore
            raw_role_folder = company_folder / raw_role_name
            
            try:
                # Create the sibling _RAW folder
                raw_role_folder.mkdir(exist_ok=False)
                
                # Move all files from _RAW/ to sibling folder
                moved_count = 0
                for item in raw_subfolder.iterdir():
                    target = raw_role_folder / item.name
                    shutil.move(str(item), str(target))
                    moved_count += 1
                
                # Delete empty _RAW subfolder
                raw_subfolder.rmdir()
                
                print(f"  ✓ {role_folder.name}: Moved {moved_count} files to {raw_role_name}/")
                results['processed'].append({
                    'role': str(role_folder.relative_to(companies_dir)),
                    'raw_folder': str(raw_role_folder.relative_to(companies_dir)),
                    'files': moved_count
                })
                
            except Exception as e:
                error_msg = f"{role_folder.name}: {str(e)}"
                print(f"  ✗ Error: {error_msg}")
                results['errors'].append(error_msg)
                # Clean up if partially created
                if raw_role_folder.exists() and not list(raw_role_folder.iterdir()):
                    raw_role_folder.rmdir()
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"Successfully restructured: {len(results['processed'])} role folders")
    print(f"Skipped (no _RAW or empty): {len(results['skipped'])}")
    print(f"Errors: {len(results['errors'])}")
    
    if results['processed']:
        print(f"\nRestructured folders:")
        for item in results['processed']:
            print(f"  - {item['role']} → {item['raw_folder']} ({item['files']} files)")
    
    if results['errors']:
        print(f"\nErrors encountered:")
        for error in results['errors']:
            print(f"  - {error}")
    
    return results

if __name__ == '__main__':
    restructure_raw_folders()

