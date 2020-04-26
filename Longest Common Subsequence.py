class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n, m = len(text1), len(text2)

        C = [[0]*(m+1) for _ in range(n+1)]
        for j in range(1, m+1):
            for i in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    C[i][j] = C[i-1][j-1] + 1
                else:
                    C[i][j] = max(C[i-1][j], C[i][j-1])
        return C[-1][-1]


print(Solution().longestCommonSubsequence(
    text2="abcdenbbbbbb", text1="lmbcdfff"))
