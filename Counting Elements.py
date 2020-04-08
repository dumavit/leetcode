class Solution(object):
    def countElements(self, arr):
        d = {}
        for number in arr:
            d[number] = d.get(number, 0) + 1
        return len([number for number in arr if number+1 in d])


print(Solution().countElements([1, 1, 2]))
