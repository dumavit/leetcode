from typing import List


class Solution:
    def sortArrayByParity(self, arr: List[int]) -> List[int]:
        left, right = 0, len(arr)-1

        while left < right:
            while left < right and arr[left] % 2 == 0:
                left += 1
            while right > left and arr[right] % 2 == 1:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        return arr



print(Solution().sortArrayByParity)
