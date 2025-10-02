from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs_traversal(root):
    """
    BFS (level order) visits nodes level by level from left to right.
    Uses a queue to keep track of nodes at each level.
    """
    result = []
    if not root:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Example usage:
if __name__ == "__main__":
    # Construct the following binary tree:
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))

    print("BFS:", bfs_traversal(root))              # [1, 2, 3, 4, 5, 6]
