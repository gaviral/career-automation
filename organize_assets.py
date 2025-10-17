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
    
    results = {
        'created': [],
        'moved': [],
        'already_exists': [],
        'no_raw_jd': []
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
        
        # Move Task_1_raw_jd.txt
        raw_jd = job_folder / 'Task_1_raw_jd.txt'
        if raw_jd.exists():
            target = assets_folder / 'Task_1_raw_jd.txt'
            if not target.exists():
                shutil.move(str(raw_jd), str(target))
                results['moved'].append(str(job_folder.relative_to(base_dir)))
                print(f"  ✓ Moved Task_1_raw_jd.txt to _ASSETS/")
            else:
                print(f"  • Task_1_raw_jd.txt already in _ASSETS/")
        else:
            results['no_raw_jd'].append(str(job_folder.relative_to(base_dir)))
            print(f"  • No Task_1_raw_jd.txt found")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Created _ASSETS folders: {len(results['created'])}")
    print(f"Moved raw JD files: {len(results['moved'])}")
    print(f"Already had _ASSETS: {len(results['already_exists'])}")
    print(f"No raw JD to move: {len(results['no_raw_jd'])}")
    
    return results

if __name__ == '__main__':
    organize_assets()

