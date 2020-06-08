from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount+1):
                if i >= c:
                    dp[i] += dp[i-c]
        return dp[-1]


print(Solution().change(amount=5, coins=[1, 2, 5]))
