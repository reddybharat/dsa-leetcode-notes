# Dynamic Programming

## Core Concept
Dynamic Programming (DP) solves complex problems by breaking them into simpler subproblems and storing solutions to avoid redundant calculations.

## Key Principles

### 1. Optimal Substructure
- Solution to a problem contains solutions to its subproblems
- Example: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)

### 2. Overlapping Subproblems
- Same subproblems are solved multiple times
- Example: Fibonacci(5) requires Fibonacci(3) multiple times

## Two Approaches

### Top-Down (Memoization)
- Start with the main problem
- Use recursion with memoization
- Cache results to avoid recomputation

### Bottom-Up (Tabulation)
- Start with base cases
- Build up to the main problem
- Use iterative approach with table

## Common DP Patterns

### 1. Fibonacci Sequence
- **Base cases**: F(0) = 0, F(1) = 1
- **Recurrence**: F(n) = F(n-1) + F(n-2)
- **Time**: O(n), **Space**: O(1) with optimization

### 2. Climbing Stairs
- **Problem**: Ways to reach top with 1 or 2 steps
- **Pattern**: Similar to Fibonacci
- **Key insight**: Ways(n) = Ways(n-1) + Ways(n-2)

### 3. House Robber
- **Problem**: Maximum money without robbing adjacent houses
- **Recurrence**: rob(i) = max(rob(i-1), rob(i-2) + nums[i])
- **Base cases**: rob(0) = nums[0], rob(1) = max(nums[0], nums[1])

### 4. Longest Common Subsequence (LCS)
- **Problem**: Find longest common subsequence between two strings
- **Recurrence**: 
  - If chars match: LCS(i,j) = 1 + LCS(i-1,j-1)
  - If chars don't match: LCS(i,j) = max(LCS(i-1,j), LCS(i,j-1))

### 5. Edit Distance
- **Problem**: Minimum operations to convert string A to string B
- **Operations**: Insert, Delete, Replace
- **Recurrence**: 
  - If chars match: dp[i][j] = dp[i-1][j-1]
  - If chars don't match: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

### 6. Knapsack Problem
- **0/1 Knapsack**: Each item can be used at most once
- **Unbounded Knapsack**: Each item can be used multiple times
- **Recurrence**: dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])

## DP Problem Categories

### 1. 1D DP
- **Examples**: Fibonacci, Climbing Stairs, House Robber
- **Pattern**: dp[i] depends on previous states
- **Space optimization**: Often reducible to O(1)

### 2. 2D DP
- **Examples**: LCS, Edit Distance, Unique Paths
- **Pattern**: dp[i][j] depends on previous states
- **Common optimizations**: Space reduction, rolling array

### 3. Interval DP
- **Examples**: Matrix Chain Multiplication, Palindrome Partitioning
- **Pattern**: Solve for all intervals of length k, then k+1, etc.

### 4. Tree DP
- **Examples**: Binary Tree Maximum Path Sum, House Robber III
- **Pattern**: Post-order traversal, return multiple values

## Key Tips & Tricks

### State Definition
- **Be precise**: What does dp[i] represent?
- **Include all necessary information**: Don't lose important state
- **Keep it simple**: Avoid over-complicating state

### Transition Formula
- **Think about dependencies**: What previous states affect current state?
- **Consider all cases**: Handle all possible transitions
- **Optimize**: Look for patterns to simplify

### Base Cases
- **Handle edge cases**: Empty arrays, single elements
- **Initialize properly**: Set up initial values correctly
- **Boundary conditions**: Check array bounds

### Space Optimization
- **Rolling array**: Use only necessary previous states
- **In-place updates**: Modify array in place when possible
- **State compression**: Use bit manipulation for small state spaces

## Common Mistakes

1. **Wrong state definition**: Not capturing all necessary information
2. **Incorrect base cases**: Missing or wrong initial conditions
3. **Wrong transition**: Not considering all dependencies
4. **Index errors**: Off-by-one errors in array access
5. **Over-optimization**: Premature space optimization making code complex

## Optimization Techniques

### 1. Space Optimization
- Use rolling arrays for 2D DP
- Compress state space when possible
- Use bit manipulation for small states

### 2. Time Optimization
- Avoid redundant calculations
- Use mathematical formulas when possible
- Consider iterative vs recursive approaches

### 3. Memory Optimization
- Release unused memory
- Use generators for large sequences
- Consider external storage for very large problems

## Problem-Solving Strategy

1. **Identify the pattern**: Is it DP? Look for optimal substructure
2. **Define state**: What does dp[i] represent?
3. **Find recurrence**: How does current state depend on previous states?
4. **Set base cases**: Handle edge cases and initial conditions
5. **Implement**: Choose top-down or bottom-up approach
6. **Optimize**: Reduce space/time complexity if needed

## Common DP Problems

### Easy
- Fibonacci, Climbing Stairs, House Robber
- Min Cost Climbing Stairs, Tribonacci

### Medium
- Longest Increasing Subsequence, Edit Distance
- Coin Change, Word Break, Unique Paths

### Hard
- Longest Common Subsequence, Edit Distance
- Knapsack variants, Matrix Chain Multiplication

## Related Concepts
- **Greedy**: Sometimes DP can be optimized to greedy
- **Backtracking**: DP can replace backtracking for optimization
- **Graph algorithms**: Shortest path problems often use DP
- **Combinatorics**: Counting problems often use DP
