from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x = Counter(jewels)
        y = Counter(stones)
        count = 0
        for i in list(x.keys()):
            if i in y:
                count += y[i]
        return count
            


        
