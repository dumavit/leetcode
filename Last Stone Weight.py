class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            biggest = stones.pop()
            next_biggest = stones.pop()
            if biggest > next_biggest:
                stones.append(biggest-next_biggest)
        return stones[0]
