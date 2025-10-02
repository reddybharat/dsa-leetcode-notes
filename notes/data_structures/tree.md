# Tree Data Structures

Trees are hierarchical data structures with a root node and child nodes. This covers Binary Trees (BT) and Binary Search Trees (BST).

## Tree Basics

### Tree Properties
- **Root**: Top node with no parent
- **Leaf**: Node with no children
- **Height**: Longest path from root to leaf
- **Depth**: Distance from root to a node
- **Degree**: Number of children a node has

### Binary Tree Properties
- Each node has at most 2 children
- Left child and right child
- Can be empty (null)

### Binary Search Tree Properties
- Left subtree < root < right subtree
- All nodes in left subtree < root
- All nodes in right subtree > root
- No duplicate values (typically)

## Tree Node Definition
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Tree Traversals

### 1. Inorder Traversal (Left, Root, Right)
```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Iterative version
def inorder_iterative(root):
    result = []
    stack = []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result
```

### 2. Preorder Traversal (Root, Left, Right)
```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

# Iterative version
def preorder_iterative(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
```

### 3. Postorder Traversal (Left, Right, Root)
```python
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# Iterative version
def postorder_iterative(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return result[::-1]  # Reverse to get correct order
```

### 4. Level Order Traversal (BFS)
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

## Binary Search Tree Operations

### 1. Search
```python
def search_bst(root, val):
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)

# Iterative version
def search_bst_iterative(root, val):
    current = root
    
    while current:
        if current.val == val:
            return current
        elif val < current.val:
            current = current.left
        else:
            current = current.right
    
    return None
```

### 2. Insert
```python
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    
    return root

# Iterative version
def insert_bst_iterative(root, val):
    if not root:
        return TreeNode(val)
    
    current = root
    while True:
        if val < current.val:
            if not current.left:
                current.left = TreeNode(val)
                break
            current = current.left
        else:
            if not current.right:
                current.right = TreeNode(val)
                break
            current = current.right
    
    return root
```

### 3. Delete
```python
def delete_bst(root, val):
    if not root:
        return root
    
    if val < root.val:
        root.left = delete_bst(root.left, val)
    elif val > root.val:
        root.right = delete_bst(root.right, val)
    else:
        # Node to delete found
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # Node has two children
        # Find inorder successor (smallest in right subtree)
        min_node = find_min(root.right)
        root.val = min_node.val
        root.right = delete_bst(root.right, min_node.val)
    
    return root

def find_min(root):
    while root.left:
        root = root.left
    return root
```

## Common Tree Problems

### 1. Validate Binary Search Tree
```python
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))
```

### 2. Lowest Common Ancestor
```python
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left or right
```

### 3. Maximum Depth
```python
def max_depth(root):
    if not root:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### 4. Path Sum
```python
def has_path_sum(root, target_sum):
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == target_sum
    
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))
```

### 5. Serialize and Deserialize
```python
def serialize(root):
    def preorder(node):
        if not node:
            return ['null']
        return [str(node.val)] + preorder(node.left) + preorder(node.right)
    
    return ','.join(preorder(root))

def deserialize(data):
    def build():
        val = next(vals)
        if val == 'null':
            return None
        
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node
    
    vals = iter(data.split(','))
    return build()
```

## Advanced Tree Concepts

### 1. Balanced Binary Tree
```python
def is_balanced(root):
    def height(node):
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        if left_height == -1 or right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return height(root) != -1
```

### 2. Tree Diameter
```python
def diameter_of_binary_tree(root):
    def height(node):
        nonlocal max_diameter
        
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        max_diameter = max(max_diameter, left_height + right_height)
        
        return 1 + max(left_height, right_height)
    
    max_diameter = 0
    height(root)
    return max_diameter
```

### 3. Construct Tree from Traversals
```python
def build_tree_from_preorder_inorder(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    root_index = inorder.index(root_val)
    
    root.left = build_tree_from_preorder_inorder(
        preorder[1:root_index+1],
        inorder[:root_index]
    )
    root.right = build_tree_from_preorder_inorder(
        preorder[root_index+1:],
        inorder[root_index+1:]
    )
    
    return root
```

## Time Complexities

### BST Operations
- **Search**: O(log n) average, O(n) worst case
- **Insert**: O(log n) average, O(n) worst case
- **Delete**: O(log n) average, O(n) worst case

### Tree Traversals
- **All traversals**: O(n) where n is number of nodes

### Space Complexity
- **Recursive traversals**: O(h) where h is height
- **Iterative traversals**: O(n) for worst case

## Common Mistakes
1. **Null checks**: Always check if node is None
2. **BST property**: Maintain BST property during operations
3. **Memory leaks**: Clean up references when deleting nodes
4. **Stack overflow**: Use iterative approach for deep trees
5. **Incorrect traversal**: Understand the difference between traversals

## Related Data Structures
- **Heap**: Complete binary tree with heap property
- **Trie**: Tree for string operations
- **Segment Tree**: Tree for range queries
- **Fenwick Tree**: Binary indexed tree for prefix sums
