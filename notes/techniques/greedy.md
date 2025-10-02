# Greedy Algorithms

## Core Concept
Greedy algorithms make locally optimal choices at each step, hoping to find a global optimum. They never reconsider previous choices.

## Key Properties
- **Local optimization**: Make best choice at each step
- **No backtracking**: Never reconsider previous decisions
- **Hope for global optimum**: Local choices lead to global solution
- **Efficiency**: Often O(n log n) due to sorting

## When Greedy Works

### 1. Greedy Choice Property
- **Definition**: Global optimum can be reached by making locally optimal choices
- **Example**: Activity selection, fractional knapsack
- **Key**: Prove that greedy choice is safe

### 2. Optimal Substructure
- **Definition**: Optimal solution contains optimal solutions to subproblems
- **Example**: Minimum spanning tree, shortest path
- **Key**: Problem can be broken into smaller problems

### 3. No Future Dependencies
- **Definition**: Current choice doesn't affect future choices
- **Example**: Coin change (with standard denominations)
- **Key**: Past decisions don't constrain future decisions

## Common Greedy Patterns

### 1. Activity Selection
- **Problem**: Select maximum number of non-overlapping activities
- **Greedy choice**: Always select activity with earliest finish time
- **Proof**: If optimal solution doesn't include earliest finish, we can replace

### 2. Fractional Knapsack
- **Problem**: Fill knapsack with maximum value
- **Greedy choice**: Always take item with highest value/weight ratio
- **Proof**: If optimal solution doesn't include highest ratio item, we can replace

### 3. Minimum Spanning Tree (MST)
- **Kruskal's**: Sort edges by weight, add if no cycle
- **Prim's**: Start with any vertex, add minimum weight edge
- **Proof**: Cut property ensures optimality

### 4. Huffman Coding
- **Problem**: Create optimal prefix code
- **Greedy choice**: Always merge two least frequent characters
- **Proof**: Optimal solution must have this property

### 5. Coin Change (Standard Denominations)
- **Problem**: Make change with minimum coins
- **Greedy choice**: Always use largest denomination first
- **Note**: Only works with standard coin systems

## Key Tips & Tricks

### Problem Analysis
- **Identify greedy choice**: What's the locally optimal decision?
- **Prove correctness**: Why does greedy choice lead to optimal solution?
- **Handle edge cases**: What happens with special inputs?

### Implementation Strategy
- **Sort if needed**: Often need to sort by some criteria
- **Process in order**: Make greedy choices in sorted order
- **Track state**: Keep track of current solution state

### Common Pitfalls
- **Not all problems are greedy**: Some require dynamic programming
- **Wrong greedy choice**: Not all locally optimal choices work
- **Missing edge cases**: Handle special cases carefully

## Greedy vs Dynamic Programming

### When to Use Greedy
- **Local optimization works**: Greedy choice leads to global optimum
- **No overlapping subproblems**: Each choice is independent
- **Efficient solution**: Greedy is often faster than DP

### When to Use DP
- **Overlapping subproblems**: Same subproblems solved multiple times
- **Optimal substructure**: Solution depends on optimal solutions to subproblems
- **Greedy doesn't work**: Local optimization doesn't lead to global optimum

## Common Problems

### Easy
- Activity Selection, Fractional Knapsack
- Minimum Number of Coins, Gas Station

### Medium
- Minimum Spanning Tree, Shortest Path
- Job Scheduling, Task Assignment

### Hard
- Huffman Coding, Set Cover
- Traveling Salesman (approximation)

## Advanced Concepts

### 1. Exchange Argument
- **Purpose**: Prove greedy choice is optimal
- **Method**: Show that any optimal solution can be transformed to include greedy choice
- **Use case**: Activity selection, MST algorithms

### 2. Cut Property
- **Purpose**: Prove edge belongs to MST
- **Method**: Show that edge is minimum weight edge across some cut
- **Use case**: Kruskal's and Prim's algorithms

### 3. Matroid Theory
- **Purpose**: General framework for greedy algorithms
- **Definition**: Structure that generalizes linear independence
- **Use case**: Proving correctness of greedy algorithms

## Problem-Solving Strategy

1. **Identify pattern**: Is it a greedy problem?
2. **Find greedy choice**: What's the locally optimal decision?
3. **Prove correctness**: Why does greedy choice work?
4. **Handle edge cases**: What are the special cases?
5. **Implement efficiently**: Sort if needed, process in order
6. **Test thoroughly**: Verify with different inputs

## Common Mistakes

1. **Wrong greedy choice**: Not all locally optimal choices work
2. **Missing proof**: Greedy choice might not be optimal
3. **Edge cases**: Not handling special inputs
4. **Implementation errors**: Wrong sorting or processing order
5. **Over-optimization**: Making unnecessary optimizations

## Optimization Tips

### 1. Sorting Optimization
- **Use appropriate sorting**: Choose best sorting algorithm
- **Sort only what's needed**: Don't sort unnecessary data
- **Stable sort**: When order of equal elements matters

### 2. Data Structure Optimization
- **Use heaps**: For dynamic minimum/maximum
- **Use sets**: For fast membership testing
- **Use arrays**: When indices are important

### 3. Algorithm Optimization
- **Early termination**: Stop when no better solution possible
- **Skip invalid choices**: Don't process obviously bad choices
- **Batch processing**: Process multiple elements at once

## Related Concepts
- **Dynamic Programming**: Alternative approach for optimization
- **Backtracking**: When greedy doesn't work
- **Graph algorithms**: Many greedy algorithms on graphs
- **Sorting**: Often required for greedy algorithms
