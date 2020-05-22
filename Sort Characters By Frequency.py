class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        return ''.join(i[0]*i[1] for i in sorted(counter.items(), key=lambda x: -x[1]))


print(Solution().frequencySort('asbacac'))
