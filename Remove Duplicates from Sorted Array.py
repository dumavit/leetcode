class Solution:
    def removeDuplicates(self, nums):
        cc = 0
        for i in range(1, len(nums)):
            if nums[cc] != nums[i]:
                cc += 1
                nums[cc] = nums[i]
        return cc + 1
