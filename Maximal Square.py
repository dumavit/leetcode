class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])

        max_square = 0
        C = [[0]*(m+1) for _ in range(n+1)]
        for j in range(1, m+1):
            for i in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    C[i][j] = min(C[i][j-1], C[i-1][j], C[i-1][j-1])+1
                    max_square = max(max_square, C[i][j])

        return max_square ** 2


print(Solution().maximalSquare([
    [1, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
]))
