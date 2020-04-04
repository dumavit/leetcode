class Solution(object):
    def singleNumber(self, nums):
        s = set()
        for number in nums:
            if number in s:
                s.remove(number)
            else:
                s.add(number)
        return list(s)


print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))
