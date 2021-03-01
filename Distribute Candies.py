from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies = set()
        for cType in candyType:
            if cType not in candies:
                candies.add(cType)

        return min(len(candyType)//2, len(candies))


print(Solution().distributeCandies([1, 1, 2, 2, 3, 3,3,3,3,3,4,4,4,4,4,4]))
# print(len({1,2,3}))
