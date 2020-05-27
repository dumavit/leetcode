class Solution:
    
    def sortedSquares(self, A: List[int]) -> List[int]:
        positives = [num for num in A if num>=0]
        negatives = [abs(num) for num in A if num<0][::-1]
        
        def mergeSort(a, b):
            res, i, j = [], 0,0
            while i<len(a) and j<len(b):
                ai, bj = a[i], b[j]
                if ai>bj:
                    res.append(bj)
                    j+=1
                else:
                    res.append(ai)
                    i += 1
            while i < len(a):
                res.append(a[i])
                i+= 1
            while j < len(b):
                res.append(b[j])
                j += 1
                    
            return res
            
        return [i**2 for i in mergeSort(positives, negatives)]
        
