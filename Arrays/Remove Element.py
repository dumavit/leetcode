class Solution:
    def removeElement(self, nums: List[int], val: int):
        size, deleted_count, curr_index = len(nums), 0, 0
        while curr_index + deleted_count < size:
            nums[curr_index] = nums[curr_index + deleted_count]
            if nums[curr_index + deleted_count] == val:
                deleted_count += 1
            else:
                curr_index += 1
        return size - deleted_count
