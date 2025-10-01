# Two Pointer Technique

## When to use
- Problems with arrays/lists where you need to find pairs, subarrays, or optimize something.
- Useful when you can scan from both ends or from different directions.

## Basic steps
- Place one pointer at the start, one at the end.
- While they don't meet:
    - Do the required calculation (like area, sum, etc).
    - Move the pointer(s) based on the problem's rule (often move the one at the smaller value).
- Stop when pointers meet.

## Example problem links and complexity changes
- [Container With Most Water](https://leetcode.com/problems/container-with-most-water/):
    - Find max area between two lines.
    - Time complexity: O(n) (much faster than checking all pairs, which is O(n^2)).
- Many other problems use this trick for efficient solutions.
