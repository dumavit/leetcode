class Solution(object):
    def canJump(self, nums):
        curr = 1
        for num in nums:
            if not curr:
                return False
            curr = max(curr-1, num)
        return True


print(Solution().canJump([1, 1, 1, 1, 0]))
