from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        jumps = [float('inf')]*size
        jumps[0] = 0
        for i in range(size):
            for j in range(1, nums[i]+1):
                if i+j < size:
                    jumps[i+j] = min(jumps[i+j], jumps[i]+1)
        return jumps[-1]


print(Solution().jump([5, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 8, 9, 5, 3, 7, 2, 1, 8, 2, 3, 8, 9, 4, 7, 6, 2, 5, 2,
                       7, 0, 6, 9, 9, 7, 3, 6, 3, 4, 8, 6, 4, 3, 3, 2, 7, 8, 5, 8, 6, 0]))
