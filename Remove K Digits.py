class Solution(object):
    def removeKdigits(self, num, k):
        for _ in range(k):
            size = len(num)
            index = 0
            while index+1<size and num[index] <= num[index+1]:
                index+=1
            num = num[0:index]+ num[index+1:]
        return num.lstrip('0') or '0'
