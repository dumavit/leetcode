class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = sum(hash(char) for char in s1)
        s2_hash = sum(hash(char) for char in s2[:len(s1)])
        if s1_hash == s2_hash:
            return True
        for index, char in enumerate(s2[len(s1):]):
            s2_hash += hash(char) - hash(s2[index])
            if s2_hash == s1_hash:
                return True
        return False


print(Solution().checkInclusion("ab", "zbidbaaooo"))
