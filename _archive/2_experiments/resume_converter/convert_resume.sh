#!/bin/bash

# Resume Converter Script
# Converts the optimized Markdown resume to PDF, Word, or HTML format

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}📄 Resume Converter${NC}"
echo "Converting Markdown resume to professional formats..."
echo

# Check if we're in the right directory
if [[ ! -f "../OPTIMIZED_RESUME.md" ]]; then
    echo -e "${RED}❌ Error: OPTIMIZED_RESUME.md not found${NC}"
    echo "Please run this script from the project root directory"
    exit 1
fi

# Install dependencies if needed
echo -e "${YELLOW}📦 Checking dependencies...${NC}"

# Check if uv is available, otherwise use pip
if command -v uv &> /dev/null; then
    INSTALLER="uv pip install"
    echo "Using uv for package installation"
else
    INSTALLER="pip install"
    echo "Using pip for package installation"
fi

# Create and activate a virtual environment if not already active
if [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${YELLOW}🌱 Creating and activating virtual environment...${NC}"
    uv venv
    source .venv/bin/activate
fi

# Install Python dependencies from requirements.txt
echo -e "${YELLOW}📦 Installing Python dependencies from requirements.txt...${NC}"
uv pip install -r requirements.txt

# Check for system dependencies
echo -e "${YELLOW}🔧 Checking system dependencies...${NC}"

if ! command -v pandoc &> /dev/null; then
    echo -e "${YELLOW}⚠️  pandoc not found. Installing via Homebrew...${NC}"
    if command -v brew &> /dev/null; then
        brew install pandoc
    else
        echo -e "${RED}❌ Homebrew not found. Please install pandoc manually:${NC}"
        echo "Visit: https://pandoc.org/installing.html"
    fi
fi

echo

# Convert to all formats
echo -e "${GREEN}🚀 Converting resume to all formats...${NC}"
echo

python3 ./resume_converter.py docx ../OPTIMIZED_RESUME.md

echo
echo -e "${GREEN}✅ Conversion complete!${NC}"
echo
echo -e "${BLUE}📁 Generated files:${NC}"
echo "   • Word: data/job_applications_subproject/Aviral_Garg_Resume.docx"
echo
echo -e "${YELLOW}💡 Usage tips:${NC}"
echo "   • Word: Good for recruiters who need to edit/annotate"
echo
echo -e "${GREEN}🎉 Your professional resume is ready for job applications!${NC}"
