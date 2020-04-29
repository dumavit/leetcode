# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        self.max_sum = -float('inf')

        def getMaxPathSum(self, node):
            left = getMaxPathSum(self, node.left) if node.left else 0
            right = getMaxPathSum(self, node.right) if node.right else 0
            max_single = max(node.val, node.val+max(left, right))
            self.max_sum = max(self.max_sum, left+right+node.val, max_single)
            return max_single

        getMaxPathSum(self, root)
        return self.max_sum


root = TreeNode(-2)
rootleft = TreeNode(6)
root.left = rootleft

rootleftleft = TreeNode(0)
rootleftright = TreeNode(-6)
rootleft.left = rootleftleft
rootleft.right = rootleftright

print(Solution().maxPathSum(root))
