class Solution(object):
    def moveZeroes(self, nums):
        shift = 0
        curr_index = 0
        size = len(nums)
        while curr_index < size:
            if curr_index + shift < size:
                shifted_number = nums[curr_index+shift]
                if shifted_number:
                    nums[curr_index] = shifted_number
                    curr_index += 1
                else:
                    shift += 1
            else:
                nums[curr_index] = 0
                curr_index += 1


inp = [0, 0, 0, 0, 0, 5, 0, 24]
Solution().moveZeroes(inp)
print(inp)
