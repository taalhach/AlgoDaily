"""
    2nd approach: char array

    Time    O(s+t)
    Space   O(52) -> O(1)
    44 ms, faster than 73.40%
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hs1 = 26*[0]
        hs2 = 26*[0]
        for c in s:
            idx = ord(c)-ord('a')
            hs1[idx] += 1
        for c in t:
            idx = ord(c)-ord('a')
            hs2[idx] += 1
        for i in range(26):
            if hs1[i] != hs2[i]:
                return False
        return True
