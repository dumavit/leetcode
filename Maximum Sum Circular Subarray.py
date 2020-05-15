class Solution:
    def maxSubarraySumCircular(self, A):
        local_max, global_max = 0, -float('inf')
        local_min, global_min = float('inf'), float('inf')
        total = 0

        for number in A:
            local_max = max(local_max+number, number)
            global_max = max(local_max, global_max)
            local_min = min(local_min+number, number)
            global_min = min(local_min, global_min)
            total += number
        print(global_max, global_min, total)
        return max(global_max, total-global_min) if global_max > 0 else global_max


print(Solution().maxSubarraySumCircular([-2, -3, -1]))
