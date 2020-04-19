class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        sums = [[0 for j in range(m)] for i in range(n)]
        sums[0][0] = grid[0][0]
        for i in range(1, n):
            sums[i][0] = sums[i-1][0] + grid[i][0]
        for j in range(1, m):
            sums[0][j] = sums[0][j-1] + grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                sums[i][j] = grid[i][j] + min(sums[i-1][j], sums[i][j-1])

        return sums[-1][-1]


print(Solution().minPathSum([
    [1, 3, 2],
    [1, 5, 1],
    [4, 2, 1]
]))
