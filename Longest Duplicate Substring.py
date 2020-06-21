class Solution:
    def longestDupSubstring(self, S: str) -> str:
        dp = [0]*(len(S)+1)
        start, end, max_len = 0, 0, 0
        for i in range(len(S)):
            for j in range(i+1, len(S)):
                if S[i] == S[j]:
                    new_length = dp[i] + 1
                    dp[i+1] = new_length
                    if new_length > max_len:
                        start, end = j-new_length+1, j+1
                        max_len = end-start
        return S[start:end]


print(Solution().longestDupSubstring("abcdabcd"))
