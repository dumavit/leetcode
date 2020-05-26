class Solution:
    def removeDuplicates(self, nums):
        idx = 0
        while idx < len(nums)-1:
            if nums[idx] == nums[idx+1]:
                nums.pop(idx)
            else:
                idx += 1
        return len(nums)
