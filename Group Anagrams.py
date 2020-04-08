from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for word in strs:
            d["".join(sorted(word))].append(word)
        return d.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
