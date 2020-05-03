class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = {}
        for char in magazine:
            store[char] = store.get(char, 0) + 1
        for char in ransomNote:
            if store.get(char, 0) > 0:
                store[char] -= 1
            else:
                return False
        return True
