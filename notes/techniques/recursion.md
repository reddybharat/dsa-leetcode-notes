# Recursion

## Core Concept
Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem.

## Key Components

### 1. Base Case
- **Purpose**: Stop the recursion
- **Rule**: Must be reachable and not call itself
- **Examples**: Empty list, single element, target found

### 2. Recursive Case
- **Purpose**: Break problem into smaller subproblems
- **Rule**: Must make progress toward base case
- **Examples**: Process current element, recurse on rest

### 3. Recursive Call
- **Purpose**: Solve smaller instance
- **Rule**: Must be closer to base case
- **Examples**: Smaller array, reduced problem size

## Common Patterns

### 1. Tree Traversal
- **Inorder**: Left → Root → Right
- **Preorder**: Root → Left → Right
- **Postorder**: Left → Right → Root
- **Key**: Handle null nodes as base case

### 2. List Processing
- **Head-Recursive**: Process first element, recurse on rest
- **Tail-Recursive**: Process last element, recurse on rest
- **Key**: Handle empty list as base case

### 3. Divide and Conquer
- **Split**: Divide problem into smaller parts
- **Conquer**: Solve each part recursively
- **Combine**: Merge results
- **Examples**: Merge sort, binary search

### 4. Backtracking
- **Try**: Make a choice
- **Recurse**: Explore with that choice
- **Backtrack**: Undo choice if it doesn't work
- **Examples**: N-Queens, Sudoku solver

## Recursion Types

### 1. Direct Recursion
- Function calls itself directly
- **Example**: Fibonacci, factorial

### 2. Indirect Recursion
- Function A calls function B, which calls function A
- **Example**: Mutual recursion

### 3. Tail Recursion
- Recursive call is the last operation
- **Optimization**: Can be converted to iterative
- **Example**: Factorial with accumulator

### 4. Head Recursion
- Recursive call is the first operation
- **Example**: Print list in reverse order

## Key Tips & Tricks

### Base Case Design
- **Think simple**: What's the smallest problem?
- **Handle edge cases**: Empty inputs, single elements
- **Avoid infinite recursion**: Ensure base case is reachable

### Recursive Case Design
- **Make progress**: Each call should be closer to base case
- **Simplify problem**: Break into smaller subproblems
- **Maintain invariants**: Keep problem properties intact

### Parameter Design
- **Pass necessary state**: Include all required information
- **Avoid global variables**: Use parameters instead
- **Consider return values**: What should each call return?

### Memory Management
- **Stack overflow**: Be aware of recursion depth
- **Tail recursion**: Optimize when possible
- **Iterative conversion**: Convert when stack is deep

## Common Mistakes

1. **Missing base case**: Infinite recursion
2. **Wrong base case**: Not handling edge cases
3. **No progress**: Recursive call doesn't reduce problem size
4. **Stack overflow**: Too deep recursion
5. **Wrong parameters**: Not passing necessary state

## Optimization Techniques

### 1. Memoization
- **Purpose**: Cache results to avoid recomputation
- **Use case**: Overlapping subproblems
- **Example**: Fibonacci with memoization

### 2. Tail Recursion
- **Purpose**: Convert to iterative loop
- **Benefit**: Avoid stack overflow
- **Example**: Factorial with accumulator

### 3. Iterative Conversion
- **Purpose**: Replace recursion with iteration
- **Use case**: Deep recursion, performance critical
- **Method**: Use stack to simulate recursion

### 4. Dynamic Programming
- **Purpose**: Replace recursion with table
- **Use case**: Overlapping subproblems
- **Example**: Fibonacci with DP

## Problem-Solving Strategy

1. **Identify pattern**: Is it a recursive problem?
2. **Find base case**: What's the simplest case?
3. **Define recursive case**: How to break into subproblems?
4. **Design parameters**: What state is needed?
5. **Implement carefully**: Handle edge cases
6. **Optimize if needed**: Add memoization or convert to iterative

## Common Problems

### Easy
- Factorial, Fibonacci, Sum of digits
- Count down, Print numbers

### Medium
- Tree traversals, List operations
- Tower of Hanoi, Permutations

### Hard
- N-Queens, Sudoku solver
- Path finding, Game trees

## Recursion vs Iteration

### When to Use Recursion
- **Natural fit**: Problem has recursive structure
- **Tree/graph problems**: Natural recursive traversal
- **Divide and conquer**: Split into subproblems
- **Backtracking**: Explore all possibilities

### When to Use Iteration
- **Performance critical**: Avoid function call overhead
- **Deep recursion**: Prevent stack overflow
- **Simple loops**: When iteration is more natural
- **Memory constraints**: When stack space is limited

## Advanced Concepts

### 1. Mutual Recursion
- Functions call each other
- **Example**: Even/odd functions
- **Use case**: Complex state machines

### 2. Nested Recursion
- Recursive call contains another recursive call
- **Example**: Ackermann function
- **Use case**: Complex mathematical functions

### 3. Recursive Data Structures
- Structures that contain themselves
- **Examples**: Trees, linked lists
- **Use case**: Natural recursive processing

## Related Concepts
- **Dynamic Programming**: Optimized recursion
- **Backtracking**: Recursive exploration
- **Divide and Conquer**: Recursive problem solving
- **Tree algorithms**: Natural recursive structure
