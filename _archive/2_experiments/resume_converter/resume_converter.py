#!/usr/bin/env python3
"""
Resume Converter - Convert Markdown resume to PDF, Word, or HTML formats
Usage: python resume_converter.py [format] [input_file] [output_file]
Formats: pdf, docx, html
"""

import argparse
import os
import sys
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import pypandoc
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("\nTo install dependencies, run:")
        print("pip install pypandoc")
        print("\nFor PDF conversion, also install wkhtmltopdf:")
        print("macOS: brew install wkhtmltopdf")
        print("Ubuntu: sudo apt-get install wkhtmltopdf")
        return False

def markdown_to_docx(md_file, docx_file):
    """Convert Markdown to Word document using pypandoc"""
    import pypandoc
    
    try:
        pypandoc.convert_file(md_file, 'docx', outputfile=docx_file)
        print(f"✅ Word document created: {docx_file}")
    except Exception as e:
        print(f"❌ Word conversion failed: {e}")
        print("Make sure pandoc is installed:")
        print("macOS: brew install pandoc")
        print("Ubuntu: sudo apt-get install pandoc")

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown resume to various formats')
    parser.add_argument('format', choices=['pdf', 'docx', 'html', 'all'], 
                       help='Output format (pdf, docx, html, or all)')
    parser.add_argument('input_file', nargs='?', 
                       default='data/job_applications_subproject/OPTIMIZED_RESUME.md',
                       help='Input Markdown file (default: OPTIMIZED_RESUME.md)')
    parser.add_argument('output_file', nargs='?', 
                       help='Output file name (optional, will auto-generate if not provided)')
    
    args = parser.parse_args()
    
    # Check if input file exists
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"❌ Input file not found: {args.input_file}")
        sys.exit(1)
    
    # Generate output filename if not provided
    if args.output_file:
        output_base = Path(args.output_file).stem
        output_dir = Path(args.output_file).parent
    else:
        output_base = "Aviral_Garg_Resume"
        output_dir = Path("data/job_applications_subproject/")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    formats = ['docx']
    
    for fmt in formats:
        output_file = output_dir / f"{output_base}.{fmt}"
        
        if fmt == 'docx':
            markdown_to_docx(input_path, output_file)

if __name__ == "__main__":
    main()
