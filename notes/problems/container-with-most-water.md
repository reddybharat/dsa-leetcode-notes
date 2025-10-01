# Container With Most Water

**Problem:**
Given n non-negative integers `heights` where each element represents a point at coordinate (i, heights[i]), n vertical lines are drawn such that the two endpoints of the line i is at (i, heights[i]) and (i, 0). Find two lines, which together with the x-axis forms a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Example:**
```
Input: heights = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (container) is 49.
```

## Approach
- Use two pointers, one at the beginning and one at the end of the array.
- Calculate the area between the lines at the two pointers.
- Move the pointer at the shorter line inward, since the area is limited by the shorter line.
- Repeat until the pointers meet. This gives the maximum area efficiently.

## Complexity
- Time: O(n)
- Space: O(1)
