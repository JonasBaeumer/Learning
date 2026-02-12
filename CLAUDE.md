# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Personal learning repository for algorithm practice, coding challenges, and skill development. Contains standalone solutions without a build system or test framework.

## Repository Structure

```
AdventOfCode2025/     # Daily Advent of Code 2025 puzzles (day1.py, day2.py, etc.)
DSAndAlgos/           # Data structures & algorithms practice
  ├── neetcodeB75/    # NeetCode Blind 75 problem set
  ├── datadog/        # Datadog interview preparation problems
  └── LeetCode/       # General LeetCode problems, organized by topic
      └── Graphs/     # Graph-specific problems (Union-Find, DFS/BFS)
React/Scrimba/        # React learning projects
go/                   # Go learning directory (currently empty)
```

## Code Conventions

### Solution Format

Solutions follow a consistent pattern with:
- Class-based implementations for LeetCode-style problems
- Inline complexity analysis comments (Runtime, Space complexity)
- Multiple approaches shown (naive vs optimized)
- Detailed docstrings explaining the problem and approach

Example pattern:
```python
# Use a dict to keep store of what we have already seen
# Runtime: O(n)
# Spacetime: O(n)

class Solution:
    def methodName(self, ...):
        # Implementation
```

### Problem Files

- File names include problem number and title (e.g., `721_account_merge.py`)
- Complex problems include extensive comments explaining:
  - Problem description
  - Approach and algorithm choice
  - Questions/challenges encountered
  - Time/space complexity analysis
- Test cases often embedded directly in files (e.g., `test_accounts = [...]`)

### Advent of Code Solutions

- Solutions may contain hardcoded file paths to input files
- Use regex for parsing structured input
- Include explanatory comments about the algorithm approach
- Often contain helper functions with docstrings

## Running Code

All Python files are standalone scripts. Execute with:
```bash
python3 <filename>.py
```

No build system, test runner, or package manager configured. Each file is self-contained.

## Key Algorithms & Patterns

This repository focuses heavily on:
- **Graph algorithms**: Union-Find (DSU), DFS/BFS, connected components
- **Dynamic programming**: Multiple DP problems with memoization patterns
- **Data structures**: Trees (BST, binary trees), LinkedLists, Tries
- **String algorithms**: Sliding window, two pointers
- **Backtracking**: Search problems and constraint satisfaction

Graph problems in `DSAndAlgos/LeetCode/Graphs/` demonstrate Union-Find implementations with path compression.
