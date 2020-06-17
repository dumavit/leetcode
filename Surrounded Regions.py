class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if board and board[0]:
            N, M = len(board), len(board[0])
            visited = set()

            def dfs(board, i, j):
                if (i, j) not in visited and i >= 0 and i < N and j >= 0 and j < M and (i, j) and board[i][j] == 'O':
                    visited.add((i, j))
                    dfs(board, i+1, j)
                    dfs(board, i-1, j)
                    dfs(board, i, j+1)
                    dfs(board, i, j-1)

            for i in range(1, N-1):
                dfs(board, i, 0)
                dfs(board, i, M-1)
            for i in range(1, M-1):
                dfs(board, 0, i)
                dfs(board, N-1, i)
            for i in range(1, N-1):
                for j in range(1, M-1):
                    if board[i][j] == 'O' and (i, j) not in visited:
                        board[i][j] = 'X'
