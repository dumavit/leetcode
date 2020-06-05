from random import random


class Solution:

    def __init__(self, w: List[int]):
        self.length = sum(w)
        self.sums = [w[0]]
        for weight in w[1:]:
            self.sums.append(self.sums[-1]+weight)

    def pickIndex(self) -> int:
        r = int(random()*self.length)
        for index, s in enumerate(self.sums):
            if r < 0:
                return index


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 4, 5, 6, 7])
for i in range(10):
    print(obj.pickIndex())
