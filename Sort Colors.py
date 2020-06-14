from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        zeroIndex, twoIndex, currIndex = 0, len(nums)-1, 0

        for _ in range(len(nums)):
            if nums[currIndex] == 0:
                nums[currIndex], nums[zeroIndex] = nums[zeroIndex], nums[currIndex]
                zeroIndex += 1
                currIndex += 1
            elif nums[currIndex] == 2:
                nums[twoIndex], nums[currIndex] = nums[currIndex], nums[twoIndex]
                twoIndex -= 1
            else:
                currIndex += 1
        return nums


print(Solution().sortColors([1, 2, 0, 2, 2, 1, 1, 1, 2, 0, 0, 1, 1, 0, 0, 1, 2, 0, 1, 2, 2, 2,
                             2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]))
