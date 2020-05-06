class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for idx, char in enumerate(s):
            if counter.get(char) == 1:
                return idx
        return -1
