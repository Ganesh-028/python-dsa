from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f = {}
        f = Counter(s)
        g = {}
        g = Counter(t)
        if f == g:
            return True
        else:
            return False
