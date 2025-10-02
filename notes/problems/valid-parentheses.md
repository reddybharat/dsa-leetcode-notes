# Valid Parentheses

**LeetCode 20** | **Difficulty: Easy** | **Category: Stack**

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
```

## Approach: Stack

### Intuition
Use a stack to keep track of opening brackets. When we encounter a closing bracket, we check if it matches the most recent opening bracket.

### Algorithm
1. Create a mapping of closing brackets to their corresponding opening brackets
2. Use a stack to store opening brackets
3. For each character:
   - If it's an opening bracket, push it onto the stack
   - If it's a closing bracket:
     - If stack is empty or the top doesn't match, return false
     - Otherwise, pop the matching opening bracket
4. Return true if stack is empty (all brackets matched)

### Complexity Analysis

- **Time Complexity**: O(n) - We visit each character once
- **Space Complexity**: O(n) - In the worst case, all characters are opening brackets

## Key Insights

1. **Stack is perfect for matching problems** - LIFO property ensures we match the most recent opening bracket
2. **Hash map for quick lookup** - O(1) time to check if a character is a closing bracket and find its match
3. **Edge cases to consider**:
   - Empty string (valid)
   - Only opening brackets (invalid)
   - Only closing brackets (invalid)
   - Mismatched brackets (invalid)

## Related Problems

- [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)
- [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)
- [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

## Practice Tips

1. **Visualize the stack** - Draw out the stack state for each character
2. **Test edge cases** - Empty string, single character, all opening, all closing
3. **Think about the invariant** - At any point, the stack should only contain unmatched opening brackets
