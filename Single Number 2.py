class Solution(object):
    # def singleNumber(self, nums):
    #     return (3 * sum(set(nums)) - sum(nums)) / 2

    def singleNumber(self, nums):
        b1, b0 = 0, 0
        for num in nums:
            b0 = (b0 ^ num) & (~b1)
            b1 = (b1 ^ num) & (~b0)
        return b0


print(Solution().singleNumber([3, 3, 3, 6, 6, 6, 88, 8, 8, 8]))
