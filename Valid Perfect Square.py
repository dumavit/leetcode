class Solution:
    def isPerfectSquare(self, num):
        l, med, r = 0, 0, num
        while l <= r:
            med = (l+r)//2
            squared = med**2
            if squared == num:
                return True
            l, r = (l, med-1) if squared > num else (med+1, r)
        return False


for i in range(10000):
    # print(i**2)
    print(Solution().isPerfectSquare(i**2))
# print(Solution().isPerfectSquare(25))
