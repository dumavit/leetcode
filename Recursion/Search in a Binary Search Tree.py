# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left if root.val > val else root.right, val)
