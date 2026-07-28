from collections import Counter
class Solution:
    def maxDistinct(self, s: str) -> int:
        x = Counter(s)
        g = list(x.keys())
        c = len(g)
        return c
        


        
