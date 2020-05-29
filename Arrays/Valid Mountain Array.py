from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = -1
        for i in range(1, len(arr)-1):
            prev, curr, nnext = arr[i-1], arr[i], arr[i+1]
            if curr > prev and curr > nnext:
                peak = i
                break

        return peak != -1 and all(arr[i] < arr[i+1] for i in range(0, peak)) and all(arr[i] > arr[i+1] for i in range(peak, len(arr)-1))


print(Solution().validMountainArray([4, 5, 3, 2, 1]))
