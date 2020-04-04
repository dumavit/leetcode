class Solution(object):
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) / 2


print(Solution().singleNumber([3, 3, 3, 6, 6, 6, 88, 8, 8, 8]))
