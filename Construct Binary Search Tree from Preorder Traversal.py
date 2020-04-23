# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insert(self, root, val):
        curr, prev = root, None
        while curr:
            prev, curr = curr, curr.left if curr.val > val else curr.right
        if prev.val > val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)

    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder.pop(0))
        for val in preorder:
            self.insert(root, val)
        return root


print(Solution().bstFromPreorder([8, 5, 1, 7, 10, 12]))
