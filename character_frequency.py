from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        x = Counter(s)
        y = len(set(x.values()))
        if y==1:
            return True
        else:
            return False       
            
            


        
