class Solution:
    def countSquares(self, matrix):
        count, n, m = 0, len(matrix), len(matrix[0])
        count += sum(matrix[0]) + sum(matrix[i][0] for i in range(1, n))
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j]:
                    min_neighbour = min(
                        matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])
                    matrix[i][j] = min_neighbour+1
                    count += matrix[i][j]
        return count


print(Solution().countSquares(
    [[0, 1, 1, 1],
     [1, 1, 1, 1],
     [0, 1, 1, 1]

     ]))
