class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        g =[]
        for i in nums:
            if i % 2 == 0:
                g.append(0)
            else:
                g.append(1)
        g.sort()
        return g

        
