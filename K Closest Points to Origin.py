from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        squares = [+i*i+j*j for (i, j) in points]
        sorted_indexes = sorted((val, idx)
                                for (idx, val) in enumerate(squares))
        result = [points[idx] for (val, idx) in sorted_indexes[0:K]]
        return result


print(Solution().kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2))
