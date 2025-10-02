# DFS and BFS Traversals in Binary Trees

## Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking. There are three common types of DFS traversals for binary trees:

### 1. Inorder Traversal (Left, Root, Right)
- Visits the left subtree, then the root, then the right subtree.
- For Binary Search Trees (BSTs), this returns values in sorted order.

### 2. Preorder Traversal (Root, Left, Right)
- Visits the root first, then the left subtree, then the right subtree.
- Useful for copying the tree or prefix notation.

### 3. Postorder Traversal (Left, Right, Root)
- Visits the left subtree, then the right subtree, then the root.
- Useful for deleting the tree or postfix notation.

#### Example Tree
```
     1
    / \
   2   3
  / \   \
 4   5   6
```
- Inorder:   4, 2, 5, 1, 3, 6
- Preorder:  1, 2, 4, 5, 3, 6
- Postorder: 4, 5, 2, 6, 3, 1

## Breadth-First Search (BFS)
BFS (level order) visits nodes level by level from left to right. It uses a queue to keep track of nodes at each level.

- BFS: 1, 2, 3, 4, 5, 6

---
For code examples, see the corresponding Python files in the `code/` directory.
