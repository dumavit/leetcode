from typing import List


# class Solution:
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         sorted_people = sorted(people, key=lambda x: x[0])
#         result = [None]*len(people)
#         for (h, k) in sorted_people:
#             idx, places = 0, k
#             while places > 0 or result[idx] != None:
#                 if result[idx] is None or result[idx][0] >= h:
#                     places -= 1
#                 idx += 1
#             result[idx] = [h, k]
#         return result


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

print(Solution().reconstructQueue(
    [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
