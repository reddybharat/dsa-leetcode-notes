# Combination Sum

**Problem:**
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. The same number may be chosen from `candidates` an unlimited number of times.

**Example:**
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
```

## Approach
- Use backtracking to explore all possible combinations.
- At each step, make two choices: include current candidate (can reuse) or skip to next.
- Prune invalid paths early when sum exceeds target.
- Process candidates in order to avoid duplicate combinations.

## Complexity
- Time: O(2^target)
- Space: O(target)
