class Solution:
    def validIPAddress(self, IP: str) -> str:
        groups, separators = [], []
        isV4, isV6 = True, True
        v4Groups = IP.split('.')
        if v4Groups and len(v4Groups) == 4:
            if all([0 <= int(group) and int(group) < 256 for group in v4Groups]):
                return "IPv4"
        v6Groups = IP.split(':')

        return "Neither"


# print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(Solution().validIPAddress("192.168.1.0"))
