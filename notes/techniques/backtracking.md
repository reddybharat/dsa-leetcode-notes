# Backtracking

## Overview

Backtracking is a systematic way to explore all possible solutions to a problem by building solutions incrementally and abandoning a path as soon as it's determined that the path cannot lead to a valid solution.

## Key Characteristics

1. **Incremental Construction**: Build solutions step by step
2. **Pruning**: Abandon invalid paths early
3. **Undo Operations**: Backtrack when a path doesn't work
4. **Systematic Exploration**: Try all possibilities systematically

## General Template

```python
def backtrack(parameters):
    # Base case: found a complete solution
    if is_complete_solution():
        add_to_results()
        return
    
    # Base case: invalid path
    if is_invalid_path():
        return
    
    # Try all possible choices
    for choice in get_possible_choices():
        # Make the choice
        make_choice(choice)
        
        # Recurse with the choice
        backtrack(updated_parameters)
        
        # Undo the choice (backtrack)
        undo_choice(choice)
```

## Common Patterns

### 1. Combination Problems
- Find all combinations that meet certain criteria
- Example: Combination Sum, Subsets

### 2. Permutation Problems
- Find all arrangements of elements
- Example: Permutations, N-Queens

### 3. Path Finding
- Find all paths in a graph/tree
- Example: Path Sum, Word Search

## Key Techniques

### 1. State Management
- Keep track of current state
- Use parameters to pass state between recursive calls
- Consider what needs to be passed vs. what can be computed

### 2. Pruning Strategies
- **Constraint Pruning**: Stop when constraints are violated
- **Bound Pruning**: Stop when bounds are exceeded
- **Duplicate Pruning**: Avoid exploring duplicate states

### 3. Choice Ordering
- Order choices to avoid duplicates
- Process in a consistent order
- Consider sorting input for better pruning

## Common Mistakes

1. **Forgetting to backtrack**: Always undo your choices
2. **Not copying results**: Use deep copy for mutable objects
3. **Wrong base cases**: Handle all termination conditions
4. **Inefficient pruning**: Add constraints early
5. **Duplicate solutions**: Use proper ordering/constraints

## Time Complexity

- **Worst Case**: O(b^d) where b is branching factor, d is depth
- **With Pruning**: Often much better than worst case
- **Space**: O(d) for recursion stack

## Example: Combination Sum

```python
def combinationSum(candidates, target):
    result = []
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])  # Make a copy
            return
        
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()  # Backtrack
    
    backtrack(0, [], target)
    return result
```

## Optimization Tips

1. **Sort input**: Often helps with pruning
2. **Early termination**: Stop as soon as constraints are violated
3. **Memoization**: Cache results for repeated subproblems
4. **Iterative approach**: Use stack instead of recursion for deep problems
5. **Constraint propagation**: Use constraints to reduce search space

## Related Problems

- **Combination Problems**: Combination Sum, Subsets, Subset Sum
- **Permutation Problems**: Permutations, N-Queens, Sudoku
- **Path Problems**: Word Search, Path Sum, Generate Parentheses
- **Partition Problems**: Palindrome Partitioning, Partition Equal Subset Sum
