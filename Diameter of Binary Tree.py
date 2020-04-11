# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return max(left_height+right_height, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
