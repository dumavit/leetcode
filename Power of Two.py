class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power, number = 0, n
        while number > 1:
            power += 1
            number /= 2
        return 2**power == n


print(Solution().isPowerOfTwo(64))
