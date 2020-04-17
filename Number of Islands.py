class Solution:
    def visitIsland(self, grid, i, j, n, m):
        queue = [[i, j]]
        while queue:
            node_i, node_j = queue.pop()
            if node_i-1 >= 0 and grid[node_i-1][node_j] == '1':
                grid[node_i-1][node_j] = 0
                queue.append([node_i-1, node_j])
            if node_i+1 < n and grid[node_i+1][node_j] == '1':
                grid[node_i+1][node_j] = 0
                queue.append([node_i+1, node_j])
            if node_j-1 >= 0 and grid[node_i][node_j-1] == '1':
                grid[node_i][node_j-1] = 0
                queue.append([node_i, node_j-1])
            if node_j + 1 < m and grid[node_i][node_j+1] == '1':
                grid[node_i][node_j+1] = 0
                queue.append([node_i, node_j+1])

    def numIslands(self, grid):
        if not grid:
            return 0
        islands = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands += 1
                    self.visitIsland(grid, i, j, n, m)
        return islands


print(Solution().numIslands([["1", "0", "1", "1", "1"],
                             ["1", "0", "1", "0", "1"],
                             ["1", "1", "1", "0", "1"]]))
