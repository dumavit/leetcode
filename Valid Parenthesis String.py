class Solution:
    def checkValidString(self, s):
        low, high = 0, 0
        for char in s:

            if char == '(':
                low += 1
                high += 1
            if char == ')':
                high -= 1
                if low > 0:
                    low -= 1

            if char == '*':
                high += 1
                if low > 0:
                    low -= 1
            if high < 0:
                return False
        return not low


# (())*)
# (**))
print(Solution().checkValidString("(*(*"))
