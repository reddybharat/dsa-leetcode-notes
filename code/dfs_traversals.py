class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. Inorder Traversal (Left, Root, Right)
def inorder_traversal(root):
    """
    Inorder traversal visits the left subtree, then the root, then the right subtree.
    For BSTs, this returns values in sorted order.
    """
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result

# 2. Preorder Traversal (Root, Left, Right)
def preorder_traversal(root):
    """
    Preorder traversal visits the root first, then the left subtree, then the right subtree.
    Useful for copying the tree or prefix notation.
    """
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result

# 3. Postorder Traversal (Left, Right, Root)
def postorder_traversal(root):
    """
    Postorder traversal visits the left subtree, then the right subtree, then the root.
    Useful for deleting the tree or postfix notation.
    """
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(root)
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

    print("Inorder:", inorder_traversal(root))      # [4, 2, 5, 1, 3, 6]
    print("Preorder:", preorder_traversal(root))    # [1, 2, 4, 5, 3, 6]
    print("Postorder:", postorder_traversal(root))  # [4, 5, 2, 6, 3, 1]
