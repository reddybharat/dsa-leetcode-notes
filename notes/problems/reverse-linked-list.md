# Reverse Linked List

**LeetCode Problem:** [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

**Difficulty:** Easy

## Problem Statement

Given the head of a singly linked list, reverse the list, and return the reversed list.

### Examples

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**
```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**
```
Input: head = []
Output: []
```

## Approach

### Iterative Approach
- Use three pointers: `prev`, `current`, and `next`
- Traverse the list and reverse the links
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

### Recursive Approach
- Recursively reverse the rest of the list
- Update the current node's next pointer
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) due to recursion stack

## Key Insights

1. **Iterative is more space-efficient** - O(1) vs O(n) for recursive
2. **Three-pointer technique** - prev, current, next
3. **Handle edge cases** - empty list, single node
4. **Update pointers carefully** - avoid losing references

## Common Mistakes

1. **Losing reference to next node** - always store `next` before changing pointers
2. **Not handling empty list** - check if head is None
3. **Incorrect pointer updates** - order of operations matters
4. **Forgetting to return new head** - return the last node (which becomes new head)

## Related Problems

- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## Code Template

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
```

## Practice Tips

1. **Draw the process** - visualize how pointers change
2. **Test with different sizes** - empty, single, multiple nodes
3. **Understand the three-pointer dance** - prev, current, next
4. **Practice both approaches** - iterative and recursive
