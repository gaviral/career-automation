#!/usr/bin/env python3
"""
Organize job application assets by creating _ASSETS folders
and moving raw job descriptions into them.
"""

import os
import shutil
from pathlib import Path

def organize_assets():
    """
    For each job application folder:
    1. Create _ASSETS subfolder
    2. Move Task_1_raw_jd.txt into _ASSETS/
    """
    base_dir = Path(__file__).parent
    
    # Find all job application folders
    # Pattern: <number>_<company>/<number>_<role>/
    job_folders = []
    
    for company_folder in base_dir.iterdir():
        if not company_folder.is_dir():
            continue
        
        # Skip special folders
        if company_folder.name.startswith('.') or company_folder.name.startswith('_'):
            continue
            
        # Check if it's a numbered company folder
        if not company_folder.name.split('_')[0].isdigit():
            continue
            
        # Find job subfolders
        for job_folder in company_folder.iterdir():
            if job_folder.is_dir() and not job_folder.name.startswith('.') and not job_folder.name.startswith('_'):
                # Check if it's a numbered job folder
                if job_folder.name.split('_')[0].isdigit():
                    job_folders.append(job_folder)
    
    print(f"Found {len(job_folders)} job application folders")
    
    # File extensions to move to _ASSETS
    ASSET_EXTENSIONS = {
        'pdf',  # PDF files (resumes, cover letters, JDs)
        'qta', 'wav', 'mp3', 'm4a',  # Audio files (interview recordings)
        'png', 'jpg', 'jpeg', 'gif', 'webp'  # Image files
    }
    
    results = {
        'created': [],
        'moved_files': [],
        'already_exists': [],
        'skipped': []
    }
    
    for job_folder in sorted(job_folders):
        print(f"\nProcessing: {job_folder.relative_to(base_dir)}")
        
        # Create _ASSETS folder
        assets_folder = job_folder / '_ASSETS'
        if not assets_folder.exists():
            assets_folder.mkdir()
            results['created'].append(str(job_folder.relative_to(base_dir)))
            print(f"  ✓ Created _ASSETS folder")
        else:
            results['already_exists'].append(str(job_folder.relative_to(base_dir)))
            print(f"  • _ASSETS folder already exists")
        
        # Find and move asset files
        moved_count = 0
        for file in job_folder.iterdir():
            if not file.is_file():
                continue
                
            # Check if file extension matches asset types
            ext = file.suffix.lstrip('.').lower()
            if ext in ASSET_EXTENSIONS or file.name == 'Task_1_raw_jd.txt':
                target = assets_folder / file.name
                if not target.exists():
                    shutil.move(str(file), str(target))
                    moved_count += 1
                    print(f"  ✓ Moved {file.name} to _ASSETS/")
                else:
                    print(f"  • {file.name} already in _ASSETS/")
        
        if moved_count > 0:
            results['moved_files'].append(f"{job_folder.relative_to(base_dir)} ({moved_count} files)")
        else:
            if len(list(assets_folder.iterdir())) > 0:
                print(f"  • All asset files already moved")
            else:
                results['skipped'].append(str(job_folder.relative_to(base_dir)))
                print(f"  • No asset files to move")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Created _ASSETS folders: {len(results['created'])}")
    print(f"Folders with moved files: {len(results['moved_files'])}")
    print(f"Already had _ASSETS: {len(results['already_exists'])}")
    print(f"No asset files to move: {len(results['skipped'])}")
    
    if results['moved_files']:
        print(f"\nMoved files in:")
        for folder in results['moved_files']:
            print(f"  - {folder}")
    
    return results

if __name__ == '__main__':
    organize_assets()

