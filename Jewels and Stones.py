class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        result = 0
        for stone in S:
            if stone in jewels:
                result += 1
        return result
