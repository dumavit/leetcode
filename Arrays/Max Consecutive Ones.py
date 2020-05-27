class Solution:
    def findMaxConsecutiveOnes(self, nums):
        local_max, global_max = 0, 0
        for num in nums:
            if num:
                local_max += 1
                global_max = max(global_max, local_max)
            else:
                local_max = 0

        return global_max
