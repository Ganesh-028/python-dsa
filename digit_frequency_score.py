from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        x = Counter(str(n))
        sumi = 0
        for i in list(x.keys()):
            sumi += int(i) * x[i]
        return sumi
        
        
