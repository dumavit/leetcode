class Solution:
    def possibleBipartition(self, N: int, dislikes):
        # Check if the graph is bipartite
        red, blue = set(), set()
        neighbours_queue = []
        for (p1,p2) in dislikes:
            if p1 not in red and p1 not in blue:
                if p2 not in red and p2 not



print(Solution().possibleBipartition(
    N=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
