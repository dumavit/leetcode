from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros_count, idx = 0, 0
        while zeros_count+idx < len(nums):
            nnext = nums[idx+zeros_count]
            if nnext:
                nums[idx] = nnext
                idx += 1
            else:
                zeros_count += 1
        for i in range(len(nums)-zeros_count, len(nums)):
            nums[i] = 0
        return nums


print(Solution().moveZeroes([0, 1, 0, 3, 12, 0,0, 4,5]))
