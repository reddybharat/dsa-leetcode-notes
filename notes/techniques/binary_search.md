# Binary Search

## Core Concept
Binary search is an efficient algorithm for finding a target value in a sorted array by repeatedly dividing the search space in half.

## Key Properties
- **Prerequisite**: Array must be sorted
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1) iterative, O(log n) recursive
- **Principle**: Eliminate half of the search space in each iteration

## Basic Binary Search
- **Target**: Find exact match for target value
- **Return**: Index of target, or -1 if not found
- **Pattern**: Compare middle element, eliminate half, repeat

## Common Variations

### 1. Find First Occurrence
- **Problem**: Find leftmost index of target
- **Key**: When target found, continue searching left
- **Use case**: Duplicate elements, find insertion point

### 2. Find Last Occurrence
- **Problem**: Find rightmost index of target
- **Key**: When target found, continue searching right
- **Use case**: Range queries, count occurrences

### 3. Find Insertion Position
- **Problem**: Where to insert target to maintain sorted order
- **Key**: Find first position where element >= target
- **Use case**: Inserting into sorted array

### 4. Search in Rotated Array
- **Problem**: Search in array that's rotated around a pivot
- **Key**: One half is always sorted, determine which half to search
- **Use case**: Rotated sorted arrays

## Binary Search Patterns

### 1. Exact Match
- Standard binary search for exact target
- Return index or -1

### 2. Lower Bound
- Find first position where element >= target
- Useful for insertion point

### 3. Upper Bound
- Find first position where element > target
- Useful for range queries

### 4. Peak Element
- Find peak in mountain array
- Compare with neighbors to determine direction

## Key Tips & Tricks

### Loop Invariants
- **Left boundary**: All elements to the left are < target
- **Right boundary**: All elements to the right are >= target
- **Maintain**: These invariants throughout the search

### Mid Calculation
- **Standard**: mid = (left + right) // 2
- **Overflow safe**: mid = left + (right - left) // 2
- **Avoid**: Integer overflow in very large arrays

### Termination Conditions
- **Standard**: while left <= right
- **Alternative**: while left < right (different return logic)
- **Choose**: Based on problem requirements

### Return Values
- **Found**: Return index of target
- **Not found**: Return -1 or insertion point
- **Consistent**: Use same pattern throughout

## Common Mistakes

1. **Off-by-one errors**: Wrong loop conditions or mid calculations
2. **Integer overflow**: Use safe mid calculation
3. **Wrong comparison**: Not handling equality correctly
4. **Infinite loops**: Not updating left/right properly
5. **Wrong return**: Returning wrong value when not found

## Advanced Patterns

### 1. Search in 2D Matrix
- **Problem**: Search in row-wise and column-wise sorted matrix
- **Key**: Start from top-right corner, eliminate row or column
- **Time**: O(m + n) where m×n is matrix size

### 2. Search in Infinite Array
- **Problem**: Search in unbounded sorted array
- **Key**: Find bounds first, then binary search
- **Approach**: Double the search space until target is within bounds

### 3. Find Peak Element
- **Problem**: Find peak in mountain array
- **Key**: Compare with neighbors, go towards higher side
- **Edge cases**: Handle array boundaries

### 4. Search in Rotated Sorted Array
- **Problem**: Search in array rotated around pivot
- **Key**: One half is always sorted, determine which half
- **Duplicates**: Handle duplicate elements carefully

## Optimization Tips

### 1. Early Termination
- Check if target is within array bounds
- Handle edge cases before main loop
- Use sentinel values when possible

### 2. Space Optimization
- Use iterative approach to avoid recursion overhead
- Reuse variables when possible
- Avoid creating new arrays

### 3. Time Optimization
- Use bit manipulation for mid calculation
- Cache frequently accessed values
- Consider data structure optimizations

## Problem-Solving Strategy

1. **Identify pattern**: Is it a binary search problem?
2. **Check prerequisites**: Is the array sorted?
3. **Define search space**: What are the bounds?
4. **Choose variation**: Exact match, lower bound, upper bound?
5. **Implement carefully**: Handle edge cases and termination
6. **Test thoroughly**: Verify with different inputs

## Common Problems

### Easy
- Binary Search, Search Insert Position
- First Bad Version, Sqrt(x)

### Medium
- Search in Rotated Sorted Array, Find Peak Element
- Search for Range, Find Minimum in Rotated Array

### Hard
- Median of Two Sorted Arrays, Search in 2D Matrix
- Find Kth Smallest Element, Split Array Largest Sum

## Related Concepts
- **Sorting**: Binary search requires sorted data
- **Two Pointers**: Sometimes combined with binary search
- **Divide and Conquer**: Binary search is a form of D&C
- **Tree Traversal**: Similar to binary search in BST
