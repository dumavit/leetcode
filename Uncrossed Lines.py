class Solution:
    def maxUncrossedLines(self, A, B):
        n, m, i, j = len(A), len(B), 0, 0
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                best = dp[i-1][j-1]
                if A[i-1] == B[j-1]:
                    best += 1
                dp[i][j] = max(best, dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


print(Solution().maxUncrossedLines([1, 4, 2], B=[1, 2, 4]))
