from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        l = 0
        w = []
        for r in range(len(s2)):
            w.append(s2[r])
            if r - l + 1 == k:
                if Counter(s1) == Counter(w):
                    return True
                w.pop(0)
                l += 1
        return False
