#!/bin/bash

# Test script for all Project Scott iterations
# Tests each iteration with sample questions to verify functionality

echo "========================================"
echo "Testing All Project Scott Iterations"
echo "========================================"
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

test_count=0
pass_count=0

# Test function
test_iteration() {
    local iteration=$1
    local question=$2
    local expected_keyword=$3
    
    echo "Testing $iteration..."
    cd "$iteration"
    
    output=$(python3 scott.py "$question" 2>&1)
    
    if echo "$output" | grep -q "$expected_keyword"; then
        echo -e "${GREEN}✓ PASS${NC}: $iteration"
        ((pass_count++))
    else
        echo -e "${RED}✗ FAIL${NC}: $iteration"
        echo "Output: $output"
    fi
    
    ((test_count++))
    cd ..
    echo ""
}

# Test Iteration 1
test_iteration "iteration_01_hello_world" \
    "What is the RGB for unicorn red?" \
    "acknowledging your question"

# Test Iteration 2
test_iteration "iteration_02_documentation_lookup" \
    "What is the RGB for unicorn red?" \
    "255, 20, 147"

# Summary
echo "========================================"
echo "Test Summary: $pass_count/$test_count passed"
echo "========================================"

if [ $pass_count -eq $test_count ]; then
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed.${NC}"
    exit 1
fi

