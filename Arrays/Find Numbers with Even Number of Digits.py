class Solution:
    def getNumberOfDigits(self, num):
        res = 0
        while num:
            res += 1
            num //= 10
        return res

    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if self.getNumberOfDigits(num) % 2 == 0:
                result += 1
        return result
