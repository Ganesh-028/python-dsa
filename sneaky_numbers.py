from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        g =[]
        for i in list(x.keys()):
            if x[i] > 1:
                g.append(i)
        return g

        
