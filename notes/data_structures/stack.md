# Stack

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. Elements are added and removed from the same end, called the "top" of the stack.

## Key Concepts
- **LIFO**: Last In, First Out
- **Operations**: Push (add), Pop (remove), Peek/Top (view), IsEmpty
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n) where n is the number of elements

## Common Operations
```python
# Basic operations
stack = []
stack.append(item)        # Push
item = stack.pop()        # Pop
top = stack[-1]           # Peek/Top
is_empty = len(stack) == 0 # IsEmpty
```

## Implementation Options
1. **Array/List**: Simple but may need resizing
2. **Linked List**: Dynamic size, no resizing needed

## Common Patterns

### 1. Valid Parentheses
- Use stack to match opening and closing brackets
- Push opening brackets, pop when closing bracket matches

### 2. Expression Evaluation
- Infix to Postfix conversion
- Postfix expression evaluation
- Prefix expression evaluation

### 3. Monotonic Stack
- Maintain elements in sorted order
- Useful for finding next greater/smaller element

### 4. Undo Operations
- Keep track of previous states
- Browser history, text editor undo

## Example Problems
- Valid Parentheses
- Daily Temperatures
- Largest Rectangle in Histogram
- Evaluate Reverse Polish Notation
- Min Stack

## Advanced Patterns

### Monotonic Stack Pattern
```python
def nextGreaterElement(nums):
    stack = []
    result = [-1] * len(nums)
    
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            index = stack.pop()
            result[index] = num
        stack.append(i)
    
    return result
```

### Stack with Min/Max Tracking
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
    
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
```

## Time Complexities
- **Push**: O(1)
- **Pop**: O(1)
- **Peek**: O(1)
- **Search**: O(n)

## Space Complexity
- **Storage**: O(n) where n is the number of elements

## Common Mistakes
1. **Empty stack operations**: Always check if stack is empty before pop/peek
2. **Index errors**: Use proper bounds checking
3. **Memory leaks**: Clean up references when popping
4. **Stack overflow**: Be careful with recursive implementations

## Related Data Structures
- **Queue**: FIFO vs LIFO
- **Deque**: Double-ended operations
- **Priority Queue**: Ordered removal
