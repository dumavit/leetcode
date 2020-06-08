from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        visited, jumps = [False] * size, [float('inf')]*size
        queue, jumps[0] = [0], 0
        print(len(nums))
        op = 0
        while queue:
            node = queue.pop(0)
            visited[node] = True
            for neighbour in range(node+1, min(node+nums[node]+1, len(nums))):
                op += 1
                if not visited[neighbour]:
                    queue.append(neighbour)
                jumps[neighbour] = min(jumps[neighbour], jumps[node]+1)
        print(op)
        return jumps[-1]


print(Solution().jump([5, 8, 1, 1,1,1,1,1,1,1,1,2,3,1, 8, 9, 5, 3, 7, 2, 1, 8, 2, 3, 8, 9, 4, 7, 6, 2, 5, 2,
                      7, 0, 6, 9, 9, 7, 3, 6, 3, 4, 8, 6, 4, 3, 3, 2, 7, 8, 5, 8, 6, 0]))
