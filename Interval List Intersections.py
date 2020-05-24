class Solution:
    def intervalIntersection(self, A, B):
        n, m, i, j, result = len(A), len(B), 0, 0, []
        while i < n and j < m:
            a_start, a_end = A[i]
            b_start, b_end = B[j]
            if b_end < a_start or b_start > a_end:
                i, j = (i+1, j) if b_start > a_end else (i, j+1)
            else:
                result.append([max(a_start, b_start), min(a_end, b_end)])
                i, j = (i+1, j) if b_end > a_end else (i, j+1)
        return result


print(Solution().intervalIntersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]],  [[1, 5], [8, 12], [15, 24], [25, 26]]))
