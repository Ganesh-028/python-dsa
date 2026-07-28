from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x = Counter(nums)
        sum = 0
        for i in list(x.keys()):
            y = x[i]
            sum += y * (y-1) // 2
        return sum




        
