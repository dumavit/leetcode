class Solution(object):
    def sumOfSquaredDigits(self, number):
        s = 0
        while number:
            digit = number % 10
            s += digit ** 2
            number /= 10
        return s

    def isHappy(self, n):
        sums_set = set()
        while True:
            s = self.sumOfSquaredDigits(n)
            if s == 1:
                return True
            if s in sums_set:
                return False
            sums_set.add(s)
            n = s


print Solution().isHappy(33)
