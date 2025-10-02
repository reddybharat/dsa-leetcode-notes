# Sorting Algorithms

## Key Concepts

### Comparison-Based Sorts
- **Bubble Sort**: O(n²) - Compare adjacent elements, swap if needed
- **Selection Sort**: O(n²) - Find minimum, swap with current position
- **Insertion Sort**: O(n²) - Insert each element in correct position
- **Merge Sort**: O(n log n) - Divide and conquer, stable
- **Quick Sort**: O(n log n) average, O(n²) worst - Partition around pivot
- **Heap Sort**: O(n log n) - Build heap, extract max repeatedly

### Non-Comparison Sorts
- **Counting Sort**: O(n + k) - Count frequencies, stable
- **Radix Sort**: O(d × (n + k)) - Sort by digits, stable
- **Bucket Sort**: O(n + k) - Distribute into buckets, sort each

## When to Use Which

### Small Arrays (n < 50)
- **Insertion Sort**: Simple, stable, good for nearly sorted data
- **Selection Sort**: Minimal swaps, good when writes are expensive

### General Purpose
- **Merge Sort**: Guaranteed O(n log n), stable, good for linked lists
- **Quick Sort**: Fastest average case, in-place, not stable
- **Heap Sort**: Guaranteed O(n log n), in-place, not stable

### Special Cases
- **Counting Sort**: When range is small (0 to k)
- **Radix Sort**: When keys have fixed width (integers, strings)
- **Bucket Sort**: When data is uniformly distributed

## Important Properties

### Stability
- **Stable**: Merge Sort, Insertion Sort, Bubble Sort, Counting Sort, Radix Sort
- **Unstable**: Quick Sort, Heap Sort, Selection Sort

### In-Place
- **In-place**: Quick Sort, Heap Sort, Insertion Sort, Selection Sort
- **Not in-place**: Merge Sort, Counting Sort, Radix Sort

## Key Tips & Tricks

### Quick Sort Optimization
- Use median-of-three for pivot selection
- Switch to insertion sort for small subarrays (n < 10)
- Use 3-way partitioning for duplicate elements

### Merge Sort Optimization
- Use insertion sort for small arrays
- Check if already sorted before merging
- Use iterative version to avoid recursion overhead

### Heap Sort Tips
- Build max-heap in O(n) time using bottom-up approach
- Extract elements from heap in O(log n) each

## Common Patterns

### Sort by Multiple Criteria
1. Sort by primary key first
2. Use stable sort for secondary key
3. Or use custom comparator

### Partial Sorting
- Use **Quick Select** for kth smallest element
- Use **Heap** for top k elements
- Use **Partial Sort** for first k sorted elements

### External Sorting
- Use **Merge Sort** for large files
- Divide into chunks that fit in memory
- Merge sorted chunks

## Time Complexities

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| Radix | O(d × n) | O(d × n) | O(d × n) | O(n + k) | Yes |

## Common Mistakes

1. **Choosing wrong algorithm**: Consider data size, stability, space constraints
2. **Not handling duplicates**: Some algorithms perform poorly with many duplicates
3. **Memory constraints**: Use in-place algorithms when memory is limited
4. **Stability requirements**: Don't use unstable sorts when order matters
5. **Integer overflow**: Be careful with large numbers in counting sort

## Optimization Tips

1. **Hybrid approaches**: Combine algorithms (e.g., introsort = quicksort + heapsort)
2. **Early termination**: Stop when array is sorted
3. **Adaptive algorithms**: Use insertion sort for nearly sorted data
4. **Cache efficiency**: Consider memory access patterns
5. **Parallel sorting**: Use multiple threads for large datasets

## Related Concepts
- **Searching**: Binary search requires sorted data
- **Median finding**: Use quick select algorithm
- **Top K problems**: Use heap or partial sort
- **External sorting**: For data larger than memory
