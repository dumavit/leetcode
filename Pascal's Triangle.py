class Solution:
    def generate(self, numRows):
        if not numRows:
            return []
        result = [[1]]
        for i in range(1, numRows):
            result.append([1])
            for j in range(i-1):
                result[i].append(result[i-1][j]+result[i-1][j+1])
            result[i].append(1)
        return result


print(Solution().generate(0))
