#!/usr/bin/env python3
"""
Organize job application assets by creating RAW sibling folders
and moving raw files (JDs, PDFs, audio, images) into them.

Structure:
  Company/Role/        (processed files for AI context)
  Company/Role_RAW/    (raw files, not for AI)
"""

import os
import shutil
from pathlib import Path

def organize_assets():
    """
    For each job application folder:
    1. Create Role_RAW/ sibling folder if it doesn't exist
    2. Move raw files (Task_1_raw_jd.txt, *.txt, PDFs, audio, images) from Role/ to Role_RAW/
    """
    base_dir = Path(__file__).resolve().parent.parent  # career-automation root
    job_applications_dir = base_dir / 'job_applications'
    
    if not job_applications_dir.exists():
        print(f"Error: {job_applications_dir} does not exist")
        return
    
    # File extensions to move to RAW folders
    ASSET_EXTENSIONS = {
        'pdf',  # PDF files (resumes, cover letters, JDs)
        'qta', 'wav', 'mp3', 'm4a',  # Audio files (interview recordings)
        'png', 'jpg', 'jpeg', 'gif', 'webp'  # Image files
    }
    
    # Filenames that should always be in RAW
    RAW_FILENAMES = {
        'Task_1_raw_jd.txt',
        '1_raw_jd.txt',
        'raw_jd.txt'
    }
    
    results = {
        'created_raw_folders': [],
        'moved_files': [],
        'already_has_raw': [],
        'no_assets_to_move': [],
        'deleted_empty_raw': []
    }
    
    # Find all job role folders (skip _RAW folders)
    for company_folder in sorted(job_applications_dir.iterdir()):
        if not company_folder.is_dir():
            continue
        
        # Skip special folders
        if company_folder.name.startswith('.'):
            continue
        
        for role_folder in sorted(company_folder.iterdir()):
            if not role_folder.is_dir():
                continue
            
            # Skip folders that are already _RAW folders
            if '_RAW_' in role_folder.name:
                continue
            
            print(f"\nProcessing: {company_folder.name}/{role_folder.name}")
            
            # Create sibling _RAW folder
            # e.g., "1_Software_Engineer" -> "1_RAW_Software_Engineer"
            role_name = role_folder.name
            raw_role_name = role_name.replace('_', '_RAW_', 1)  # Replace first underscore
            raw_role_folder = company_folder / raw_role_name
            
            # Create RAW folder if it doesn't exist
            if not raw_role_folder.exists():
                raw_role_folder.mkdir()
                results['created_raw_folders'].append(f"{company_folder.name}/{raw_role_name}")
                print(f"  ✓ Created {raw_role_name}/")
            else:
                results['already_has_raw'].append(f"{company_folder.name}/{role_name}")
                print(f"  • {raw_role_name}/ already exists")
            
            # Find and move asset files from role folder to RAW folder
            moved_count = 0
            for file in role_folder.iterdir():
                if not file.is_file():
                    continue
                
                # Check if file should be moved to RAW
                ext = file.suffix.lstrip('.').lower()
                should_move = (
                    ext in ASSET_EXTENSIONS or
                    file.name in RAW_FILENAMES or
                    file.name.endswith('_raw_jd.txt')
                )
                
                if should_move:
                    target = raw_role_folder / file.name
                    if not target.exists():
                        shutil.move(str(file), str(target))
                        moved_count += 1
                        print(f"  ✓ Moved {file.name} to {raw_role_name}/")
                    else:
                        print(f"  • {file.name} already in {raw_role_name}/")
            
            if moved_count > 0:
                results['moved_files'].append(f"{company_folder.name}/{role_name} ({moved_count} files)")
            else:
                # Check if RAW folder has files (means everything already moved)
                if len(list(raw_role_folder.iterdir())) > 0:
                    print(f"  • All asset files already in {raw_role_name}/")
                else:
                    results['no_assets_to_move'].append(f"{company_folder.name}/{role_name}")
                    print(f"  • No asset files to move")
    
    # Cleanup: Delete empty RAW folders
    print("\n" + "="*70)
    print("CLEANUP: Checking for empty RAW folders...")
    print("="*70)
    
    for company_folder in sorted(job_applications_dir.iterdir()):
        if not company_folder.is_dir():
            continue
        
        for folder in company_folder.iterdir():
            if not folder.is_dir():
                continue
            
            # Check if this is a RAW folder
            if '_RAW_' in folder.name:
                # Check if it's empty
                if not list(folder.iterdir()):
                    print(f"  ✓ Deleting empty: {company_folder.name}/{folder.name}")
                    folder.rmdir()
                    results['deleted_empty_raw'].append(f"{company_folder.name}/{folder.name}")
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"Created RAW folders: {len(results['created_raw_folders'])}")
    print(f"Folders with moved files: {len(results['moved_files'])}")
    print(f"Already had RAW folder: {len(results['already_has_raw'])}")
    print(f"No asset files to move: {len(results['no_assets_to_move'])}")
    print(f"Deleted empty RAW folders: {len(results['deleted_empty_raw'])}")
    
    if results['moved_files']:
        print(f"\nMoved files in:")
        for folder in results['moved_files']:
            print(f"  - {folder}")
    
    if results['created_raw_folders']:
        print(f"\nCreated RAW folders for:")
        for folder in results['created_raw_folders']:
            print(f"  - {folder}")
    
    if results['deleted_empty_raw']:
        print(f"\nDeleted empty RAW folders:")
        for folder in results['deleted_empty_raw']:
            print(f"  - {folder}")
    
    return results

if __name__ == '__main__':
    organize_assets()
