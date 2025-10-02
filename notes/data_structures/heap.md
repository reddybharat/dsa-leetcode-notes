# Heap and Priority Queue

A heap is a complete binary tree that satisfies the heap property. A priority queue is an abstract data type that can be implemented using a heap.

## Key Concepts

### Heap Properties
- **Complete Binary Tree**: All levels filled except possibly the last
- **Heap Property**: 
  - **Min-Heap**: Parent ≤ children (root is minimum)
  - **Max-Heap**: Parent ≥ children (root is maximum)
- **Array Representation**: Parent at index i, children at 2i+1 and 2i+2

### Priority Queue Operations
- **Insert**: O(log n)
- **Extract Min/Max**: O(log n)
- **Peek**: O(1)
- **Decrease Key**: O(log n)

## Heap Operations

### Heapify Up (Bubble Up)
```python
def heapify_up(heap, index):
    parent = (index - 1) // 2
    if parent >= 0 and heap[index] < heap[parent]:  # Min-heap
        heap[index], heap[parent] = heap[parent], heap[index]
        heapify_up(heap, parent)
```

### Heapify Down (Bubble Down)
```python
def heapify_down(heap, index, size):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2
    
    if left < size and heap[left] < heap[smallest]:
        smallest = left
    
    if right < size and heap[right] < heap[smallest]:
        smallest = right
    
    if smallest != index:
        heap[index], heap[smallest] = heap[smallest], heap[index]
        heapify_down(heap, smallest, size)
```

## Common Patterns

### 1. Top K Elements
- Use min-heap of size k for largest k elements
- Use max-heap of size k for smallest k elements

### 2. Merge K Sorted Lists
- Use heap to always get the minimum element from all lists

### 3. Find Median from Data Stream
- Use two heaps: max-heap for smaller half, min-heap for larger half

### 4. Dijkstra's Algorithm
- Use min-heap to always process the closest unvisited node

## Implementation Examples

### Min-Heap Implementation
```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_up(self, index):
        parent = self.parent(index)
        if parent >= 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)
    
    def heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)
```

### Python's heapq Module
```python
import heapq

# Min-heap operations
heap = []
heapq.heappush(heap, item)      # Insert
item = heapq.heappop(heap)      # Extract min
item = heap[0]                  # Peek (don't remove)

# For max-heap, negate values
max_heap = []
heapq.heappush(max_heap, -item)  # Insert
item = -heapq.heappop(max_heap)  # Extract max
```

## Common Problems

### 1. Top K Frequent Elements
```python
def topKFrequent(nums, k):
    from collections import Counter
    import heapq
    
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

### 2. Merge K Sorted Lists
```python
def mergeKLists(lists):
    import heapq
    
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
```

### 3. Find Median from Data Stream
```python
class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negate values)
        self.large = []  # min-heap
    
    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    
    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]
```

## Time Complexities
- **Insert**: O(log n)
- **Extract Min/Max**: O(log n)
- **Peek**: O(1)
- **Build Heap**: O(n)
- **Heap Sort**: O(n log n)

## Space Complexity
- **Storage**: O(n) where n is the number of elements

## Common Mistakes
1. **Index confusion**: Remember 0-based vs 1-based indexing
2. **Heap property violation**: Always maintain heap property after operations
3. **Empty heap operations**: Check if heap is empty before extracting
4. **Max-heap implementation**: Use negative values or custom comparator

## Related Data Structures
- **Binary Search Tree**: Different structure, similar operations
- **Balanced BST**: Similar time complexity, different implementation
- **Fibonacci Heap**: Advanced heap with better amortized performance
