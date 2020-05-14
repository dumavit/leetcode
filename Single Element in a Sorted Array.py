class Solution:
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = 2*((l + r) // 4)
            l, r = (mid+2, r) if nums[mid] == nums[mid+1] else (l, mid)
        return nums[l]


print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 10, 12, 13, 13]))
