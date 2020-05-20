# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        self.result = None
        self.counter = 0

        def traverse(self, node):
            if self.result is None:
                if node.left:
                    traverse(self, node.left)
                self.counter += 1
                if self.counter == k:
                    self.result = node.val
                if node.right:
                    traverse(self, node.right)

        traverse(self, root)
        return self.result

# print(Solution().kthSmallest(root, 3))
