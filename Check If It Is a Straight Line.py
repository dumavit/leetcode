class Solution:
    def checkStraightLine(self, coordinates):
        (x1, y1), (x2, y2) = coordinates[0], coordinates[1]
        for (x, y) in coordinates[2:]:
            if (x-x1)*(y2-y1) != (y-y1)*(x2-x1):
                return False
        return True


print(Solution().checkStraightLine(
    [[2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(Solution().checkStraightLine(
    [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
