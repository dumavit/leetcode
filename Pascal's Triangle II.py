class Solution:
    def getRow(self, rowIndex):
        row, next_row = [], []
        for i in range(1, rowIndex+2):
            next_row = [1]
            for j in range(1, i-1):
                next_row.append(row[j]+row[j-1])
            if i > 1:
                next_row.append(1)
            row = next_row
        return row


print(Solution().getRow(5))
