# HashMap (Hash Table)

A hash map is a data structure that implements an associative array abstract data type, using a hash function to compute an index into an array of buckets or slots.

## Key Concepts

### Hash Function
- Maps keys to array indices
- Should be deterministic and uniform
- Common hash functions: division method, multiplication method

### Collision Resolution
1. **Chaining**: Store multiple elements in the same bucket using linked lists
2. **Open Addressing**: Find next available slot when collision occurs
   - Linear Probing: h(k, i) = (h(k) + i) mod m
   - Quadratic Probing: h(k, i) = (h(k) + i²) mod m
   - Double Hashing: h(k, i) = (h₁(k) + i·h₂(k)) mod m

### Load Factor
- α = n/m where n is number of elements, m is table size
- When α > threshold (usually 0.75), resize and rehash

## Operations
- **Insert**: O(1) average, O(n) worst case
- **Delete**: O(1) average, O(n) worst case  
- **Search**: O(1) average, O(n) worst case

## Common Patterns

### 1. Two Sum Problem
```python
def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []
```

### 2. Frequency Counting
```python
from collections import Counter

# Count frequencies
freq = Counter(nums)

# Manual counting
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
```

### 3. Group Anagrams
```python
def groupAnagrams(strs):
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
```

### 4. Subarray Sum
```python
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # sum -> count
    
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
```

## Advanced Patterns

### 1. LRU Cache
```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                self._remove_tail()
            
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
```

### 2. Design HashMap
```python
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        bucket = self.buckets[self._hash(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def get(self, key):
        bucket = self.buckets[self._hash(key)]
        for k, v in bucket:
            if k == key:
                return v
        return -1
    
    def remove(self, key):
        bucket = self.buckets[self._hash(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
```

## Python Dictionary Features

### Default Dictionary
```python
from collections import defaultdict

# Default value for missing keys
dd = defaultdict(list)
dd['key'].append('value')  # No KeyError

# Default factory functions
dd_int = defaultdict(int)
dd_set = defaultdict(set)
```

### Counter
```python
from collections import Counter

counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(counter)  # Counter({'a': 3, 'b': 2, 'c': 1})

# Most common elements
print(counter.most_common(2))  # [('a', 3), ('b', 2)]
```

### OrderedDict
```python
from collections import OrderedDict

# Maintains insertion order
od = OrderedDict()
od['first'] = 1
od['second'] = 2
```

## Common Problems

### 1. Valid Anagram
```python
def isAnagram(s, t):
    return Counter(s) == Counter(t)
```

### 2. Group Shifted Strings
```python
def groupStrings(strings):
    groups = {}
    for s in strings:
        key = tuple((ord(s[i]) - ord(s[0])) % 26 for i in range(len(s)))
        groups.setdefault(key, []).append(s)
    return list(groups.values())
```

### 3. Longest Substring Without Repeating Characters
```python
def lengthOfLongestSubstring(s):
    char_map = {}
    start = 0
    max_len = 0
    
    for end, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = end
        max_len = max(max_len, end - start + 1)
    
    return max_len
```

## Time Complexities
- **Average Case**: O(1) for all operations
- **Worst Case**: O(n) for all operations (due to collisions)
- **Space**: O(n) where n is the number of key-value pairs

## Common Mistakes
1. **Hash collision handling**: Understand your collision resolution strategy
2. **Mutable keys**: Don't use mutable objects as keys
3. **Hash function quality**: Poor hash functions lead to clustering
4. **Load factor**: Monitor and resize when necessary
5. **Memory usage**: Hash tables can use more memory than expected

## Optimization Tips
1. **Good hash function**: Distribute keys uniformly
2. **Appropriate size**: Choose table size to minimize collisions
3. **Load factor**: Keep load factor below 0.75
4. **Hash code caching**: Cache hash codes for expensive computations
5. **Custom hash functions**: For specific data types

## Related Data Structures
- **Set**: Hash table without values
- **TreeMap**: Ordered key-value pairs
- **Trie**: For string-based keys
- **Bloom Filter**: Probabilistic data structure
