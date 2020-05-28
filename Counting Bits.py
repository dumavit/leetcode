class Solution:
    def countBits(self, num):
        result = [0]
        offset = 1
        for i in range(1, num+1):
            if offset*2 == i:
                offset *= 2
            result.append(result[i-offset]+1)
        return result

print(Solution().countBits(20))
