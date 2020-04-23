from math import log2, ceil

max_number = 2147483647


class Solution:
    def rangeBitwiseAnd2(self, m, n):
        if m == n:
            return m
        return n & m & (max_number - 2 ** ceil(log2(n-m))+1)


print(Solution().rangeBitwiseAnd(5, 5))
print(Solution().rangeBitwiseAnd2(5, 5))
# 0000001111101000
# 0000010000011011
