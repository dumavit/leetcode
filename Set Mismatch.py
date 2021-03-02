import math


class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        a = n*(n+1)/2-sum(nums)
        b = math.factorial(n)/math.prod(nums)
        y = a/(b-1)
        x = y*b
        return [round(y), round(x)]


print(Solution().findErrorNums([28, 17, 16, 27, 24, 15, 29, 30, 8, 19, 10,
                                21, 6, 14, 22, 3, 23, 25, 7, 15, 2, 11, 5, 1, 26, 4, 12, 20, 9, 13, 18]))
