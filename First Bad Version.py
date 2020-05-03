# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        l, r = 0, n-1
        while r >= l:
            med = (l+r) // 2
            l, r = (l, med - 1) if isBadVersion(med) else (med+1, r)
        return l
