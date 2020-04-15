class Solution:
    def productExceptSelf(self, nums):
        right_dir = [1]
        left_dir = [1]
        l = len(nums)
        for i in range(l):
            right_dir.append(right_dir[-1]*nums[i])
            left_dir.append(left_dir[-1]*nums[l-i-1])
        return [right_dir[i]*left_dir[-i-2] for i in range(l)]


print(Solution().productExceptSelf([1, 2, 3, 4, 5]))
