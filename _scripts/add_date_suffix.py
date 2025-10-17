#!/usr/bin/env python3
"""
Add creation date suffix to files without modifying existing names.
Adds date before file extension: file.pdf -> file_2024_10_17.pdf
"""

import os
import time
from pathlib import Path

def add_date_suffix(directory):
    """Add creation date suffix to all files in directory."""
    dir_path = Path(directory)
    
    if not dir_path.exists():
        print(f"Directory not found: {directory}")
        return
    
    results = {'renamed': [], 'skipped': []}
    
    for file in dir_path.iterdir():
        if not file.is_file():
            continue
        
        # Get file creation time
        creation_time = os.path.getctime(file)
        date_str = time.strftime("%Y_%m_%d", time.localtime(creation_time))
        
        # Split filename and extension
        name_parts = file.stem
        extension = file.suffix
        
        # Check if file already has date suffix at the end
        if name_parts.endswith(date_str):
            results['skipped'].append(f"{file.name} (already has date)")
            print(f"  • Skipped: {file.name} (already has date)")
            continue
        
        # Create new filename with date suffix
        new_name = f"{name_parts}_{date_str}{extension}"
        new_path = file.parent / new_name
        
        # Check if target file already exists
        if new_path.exists():
            results['skipped'].append(f"{file.name} (target exists)")
            print(f"  • Skipped: {file.name} (target exists: {new_name})")
            continue
        
        # Rename file
        file.rename(new_path)
        results['renamed'].append(f"{file.name} → {new_name}")
        print(f"  ✓ Renamed: {file.name} → {new_name}")
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Renamed: {len(results['renamed'])}")
    print(f"Skipped: {len(results['skipped'])}")
    
    return results

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        # Default to _archive/3_resumes/ if no argument provided
        base_dir = Path(__file__).parent.parent
        directory = base_dir / '_archive' / '3_resumes'
    
    print(f"Processing directory: {directory}\n")
    add_date_suffix(directory)

