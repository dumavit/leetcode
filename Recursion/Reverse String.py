class Solution(object):
    def reverseString(self, s):
        if s:
            tail = s.pop()
            self.reverseString(s).insert(0, tail)
        return s


print(Solution().reverseString(["h", "e", "l", "l", "o"]))
