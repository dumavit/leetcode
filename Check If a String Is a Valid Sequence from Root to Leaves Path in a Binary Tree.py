# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, n, arr, idx=0):
        return n and n.val == arr[idx] and (n.left == n.right == None if idx == len(arr) - 1 else self.isValidSequence(n.left, arr, idx+1) or self.isValidSequence(n.right, arr, idx+1))
