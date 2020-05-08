# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        lookup = {}

        def dfs(node, level=0, parentVal=None):
            if node:
                if node.val in (x, y):
                    lookup[node.val] = (level, parentVal)
                dfs(node.left, level+1, node.val)
                dfs(node.right, level+1, node.val)
        dfs(root)
        return lookup[x][0] == lookup[y][0] and lookup[x][1] != lookup[y][1]
