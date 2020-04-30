# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, node, arr, idx=0):
        if node and node.val == arr[idx]:
            if idx == len(arr) - 1:
                return node.left is None and node.right is None
            return self.isValidSequence(node.left, arr, idx+1) or self.isValidSequence(node.right, arr, idx+1)
        return False
