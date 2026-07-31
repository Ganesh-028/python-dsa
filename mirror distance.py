class Solution:
    def mirrorDistance(self, n: int) -> int:
        y = int(str(n)[::-1])
        return abs(n - y)
       
        

        
