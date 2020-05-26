class Solution:
    def climbStairs(self, N):
        cache = {0: 0, 1: 1, 2: 2}

        def climb(n):
            if n in cache:
                return cache[n]
            result = climb(n-1) + climb(n-2)
            cache[n] = result
            return result

        return climb(N)


print(Solution().climbStairs(30))
