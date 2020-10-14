# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode, level=0, res=1) -> int:
        if not root:
            return res
        return self.countNodes(root.right, level=level+1, res=res+2**level)
