class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            left = nums[l]
            right = nums[r]
            m = int((l+r)/2)
            median = nums[m]
            if median == target:
                return m

            l, r = (m+1, r) if (median > target and right >= target and right < median) or (
                median <= target and (left > target or left < median)) else (l, m-1)
        return -1


for i in range(11, 18):
    print(Solution().search(
        [11, 12, 13, 14, 15, 16, 17, 3, 4, 5, 6, 7, 8, 9, 10], i))
for i in range(3, 11):
    print(Solution().search(
        [11, 12, 13, 14, 15, 16, 17, 3, 4, 5, 6, 7, 8, 9, 10], i))
