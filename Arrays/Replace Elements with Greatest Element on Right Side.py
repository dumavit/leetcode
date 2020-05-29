from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_elem = -1
        for i in range(len(arr)-1, -1, -1):
            curr_elem = arr[i]
            arr[i] = max_elem
            max_elem = max(max_elem, curr_elem)
        return arr


print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))
