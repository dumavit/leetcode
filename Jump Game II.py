class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        visited = [False] * size
        jumps = [[float('inf')]*size for i in range(size)]
        queue = [0]
        while queue:
            node = queue.pop()
            print('node', node)
            neighbours = 



print(Solution().canJump([[2,3,1,1,4,0,0,1,2,1,5,0,0,1,2]]))