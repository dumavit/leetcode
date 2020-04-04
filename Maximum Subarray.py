class Solution(object):
    # def maxSubArray(self, nums):
    #     max_sum = nums[0]
    #     next_sum = nums[0]
    #     for number in nums[1:]:
    #         next_sum = number if next_sum < 0 else next_sum + number
    #         if next_sum > max_sum:
    #             max_sum = next_sum
    #     return max_sum

    def maxSubArray(self, nums):
        max_sum = nums[0]
        next_sum = nums[0]
        for number in nums[1:]:
            next_sum = number if next_sum < 0 else next_sum + number
            if next_sum > max_sum:
                max_sum = next_sum
        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
