from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        sorted_points = points.sort(key=lambda p: p[0]*p[0]+p[1]*p[1])
        return sorted_points[0:K]


print(Solution().kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2))
