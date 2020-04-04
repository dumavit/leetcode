class Solution(object):
    def singleNumber(self, nums):
        xor_result = 0
        for number in nums:
            xor_result ^= number
        return xor_result


# one-liner
def singleNumber(self, nums):
    return reduce(lambda x, y: x ^ y, nums)


print(Solution().singleNumber([4, 1, 2, 1, 2]))
