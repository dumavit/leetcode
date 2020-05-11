class Solution:
    def findJudge(self, N, trust):
        trusts = [0] * N
        for (a, b) in trust:
            trusts[a-1] -= 1
            trusts[b-1] += 1
        found = N-1 in trusts
        return trusts.index(N-1)+1 if found else -1


print(Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
