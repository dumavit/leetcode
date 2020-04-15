class Solution:
    def stringShift(self, s, shift):
        shift_sum = sum(amount if d else -amount for d, amount in shift)
        return ''.join(s[(i-shift_sum) % len(s)] for i in range(len(s)))


print(Solution().stringShift(s="abcdefg",
                             shift=[[1, 1], [1, 1], [0, 2], [1, 3]]))
