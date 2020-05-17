class Solution:
    def findAnagrams(self, s, p):
        len_s, len_p = len(s), len(p)
        p_hash, s_hash = [0] * 26, [0]*26
        result = []
        for char in p:
            p_hash[ord(char)-97] += 1
        for char in s[:len_p-1]:
            s_hash[ord(char)-97] += 1
        for i in range(len_p-1, len_s):
            s_hash[ord(s[i])-97] += 1
            if i-len_p >= 0:
                s_hash[ord(s[i-len_p])-97] -= 1
            if s_hash == p_hash:
                result.append(i+1-len_p)
        return result


print(Solution().findAnagrams('cbaebabacd', 'abc'))
