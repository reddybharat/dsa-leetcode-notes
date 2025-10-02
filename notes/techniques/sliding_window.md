# Sliding Window

## Core Concept
Sliding window is a technique for solving problems involving contiguous subarrays or substrings by maintaining a window that slides through the data.

## Key Properties
- **Efficiency**: O(n) time complexity for most problems
- **Space**: O(1) to O(k) where k is window size
- **Use case**: Contiguous subarray/substring problems
- **Principle**: Expand and contract window based on conditions

## Window Types

### 1. Fixed Size Window
- **Size**: Window size is constant
- **Movement**: Slide window by one position
- **Examples**: Maximum sum of subarray of size k

### 2. Variable Size Window
- **Size**: Window size changes based on conditions
- **Movement**: Expand or contract window
- **Examples**: Longest substring without repeating characters

## Common Patterns

### 1. Maximum Sum Subarray
- **Problem**: Find maximum sum of contiguous subarray
- **Window**: Variable size, expand when sum increases
- **Key**: Reset window when sum becomes negative

### 2. Longest Substring Without Repeating Characters
- **Problem**: Find longest substring with unique characters
- **Window**: Variable size, contract when duplicate found
- **Key**: Use hash map to track character positions

### 3. Minimum Window Substring
- **Problem**: Find minimum window containing all characters of target
- **Window**: Variable size, expand to include all characters
- **Key**: Contract from left when all characters included

### 4. Subarray with Given Sum
- **Problem**: Find subarray with specific sum
- **Window**: Variable size, expand when sum is less than target
- **Key**: Contract when sum exceeds target

## Implementation Strategies

### 1. Two Pointers
- **Left pointer**: Start of window
- **Right pointer**: End of window
- **Movement**: Move pointers based on conditions
- **Use case**: Most sliding window problems

### 2. Hash Map + Two Pointers
- **Hash map**: Track character/element frequencies
- **Pointers**: Define window boundaries
- **Use case**: Problems involving character counting

### 3. Deque (Double-ended Queue)
- **Purpose**: Maintain window with specific properties
- **Operations**: Add to end, remove from front
- **Use case**: Maximum/minimum in sliding window

## Key Tips & Tricks

### Window Expansion
- **When**: When current window doesn't meet criteria
- **How**: Move right pointer forward
- **Goal**: Include more elements to satisfy condition

### Window Contraction
- **When**: When current window exceeds criteria
- **How**: Move left pointer forward
- **Goal**: Remove elements to meet condition

### Window Maintenance
- **Update state**: Keep track of window properties
- **Check conditions**: Verify if window meets criteria
- **Record results**: Update answer when window is valid

### Edge Cases
- **Empty window**: Handle case when no valid window exists
- **Single element**: Window of size 1
- **All elements**: Window containing entire array

## Common Mistakes

1. **Wrong pointer movement**: Not updating pointers correctly
2. **State update errors**: Not maintaining window state properly
3. **Boundary conditions**: Off-by-one errors in pointer updates
4. **Missing edge cases**: Not handling empty or single element cases
5. **Inefficient updates**: Not optimizing state updates

## Optimization Techniques

### 1. State Optimization
- **Incremental updates**: Update state efficiently
- **Avoid recomputation**: Don't recalculate from scratch
- **Cache results**: Store frequently used values

### 2. Memory Optimization
- **Reuse variables**: Don't create new objects unnecessarily
- **Limit storage**: Only store necessary information
- **Clean up**: Remove unused data from window

### 3. Time Optimization
- **Early termination**: Stop when no better solution possible
- **Skip invalid windows**: Don't process obviously invalid cases
- **Batch operations**: Process multiple elements at once

## Problem-Solving Strategy

1. **Identify pattern**: Is it a sliding window problem?
2. **Define window**: What does the window represent?
3. **Set up pointers**: Initialize left and right pointers
4. **Define conditions**: When to expand/contract window?
5. **Maintain state**: Keep track of window properties
6. **Update result**: Record answer when window is valid

## Common Problems

### Easy
- Maximum Sum Subarray, Longest Substring Without Repeating Characters
- Subarray with Given Sum, Minimum Size Subarray Sum

### Medium
- Longest Substring with At Most K Distinct Characters
- Fruit Into Baskets, Subarray Product Less Than K

### Hard
- Minimum Window Substring, Longest Substring with At Most Two Distinct Characters
- Sliding Window Maximum, Subarray Sum Equals K

## Advanced Patterns

### 1. Monotonic Deque
- **Purpose**: Maintain window with monotonic properties
- **Use case**: Maximum/minimum in sliding window
- **Key**: Remove elements that can't be maximum/minimum

### 2. Prefix Sum + Hash Map
- **Purpose**: Find subarrays with specific sum
- **Use case**: Subarray sum problems
- **Key**: Use prefix sum to calculate subarray sums

### 3. Two Pointers + Hash Map
- **Purpose**: Track character/element frequencies
- **Use case**: Character counting problems
- **Key**: Maintain frequency map for window

## Related Concepts
- **Two Pointers**: Similar technique for different problems
- **Hash Map**: Often used with sliding window
- **Prefix Sum**: Alternative approach for sum problems
- **Dynamic Programming**: Sometimes combined with sliding window
