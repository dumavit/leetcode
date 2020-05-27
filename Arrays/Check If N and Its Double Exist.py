class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        options = set()
        for num in arr:
            if num in options:
                return True
            options.add(num*2)
            if num % 2 == 0:
                options.add(num / 2)
        return False
