class Solution:
    def findMaxLength(self, nums):
        d = {0: 0}
        key, maxL = 0, 0
        for i in range(len(nums)):
            key += nums[i] or -1
            if key not in d:
                d[key] = i+1
            else:
                maxL = max(maxL, i+1-d[key])
        return maxL


print(Solution().findMaxLength([0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]))
