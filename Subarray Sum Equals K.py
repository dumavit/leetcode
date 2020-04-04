class Solution(object):
    def subarraySum(self, nums, k):
        sums, s, res = {0: 1}, 0, 0

        for number in nums:
            s += number
            res += sums.get(s-k, 0)
            sums[s] = sums.get(s, 0) + 1

        return res
