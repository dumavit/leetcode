class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        shifted_nums = []
        for idx, num in enumerate(arr):
            shifted_nums.append(num)
            if num == 0:
                shifted_nums.append(num)
            arr[idx] = shifted_nums[idx]
            
        