class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = []
        y = extraCandies
        for i in range(len(candies)):
            if (candies[i]) + y < max(candies):
                x.append(False)
            else:
                x.append(True)
        return x
        
