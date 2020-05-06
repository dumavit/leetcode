from math import log2


class Solution:
    def findComplement(self, num: int) -> int:
        if not num:
            return 0
        res = 0
        for i in range(int(log2(num))+1):
            res += 2**i * ((num+1) % 2)
            num //= 2
        return res


print(Solution().findComplement(51))
