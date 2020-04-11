class Solution(object):
    def getNextChar(self, S, idx):
        skip_count = 0
        while idx >= 0:
            if S[idx] == '#':
                idx -= 1
                skip_count += 1
            elif skip_count:
                idx -= 1
                skip_count -= 1
            else:
                return (S[idx], idx)
        return ('', 0)

    def backspaceCompare(self, S, T):
        s, si = self.getNextChar(S, len(S) - 1)
        t, ti = self.getNextChar(T, len(T) - 1)
        while s or t:
            if s != t:
                return False
            s, si = self.getNextChar(S, si-1)
            t, ti = self.getNextChar(T, ti-1)
        return True


print(Solution().backspaceCompare("#######q####", "####wweqe######"))
