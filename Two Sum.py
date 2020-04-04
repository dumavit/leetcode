class Solution(object):
    def twoSum(self, nums, target):
        memo = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in memo:
                return [memo[diff], index]
            memo[value] = index


print(Solution().twoSum([2, 7, 11, 15], 9))
