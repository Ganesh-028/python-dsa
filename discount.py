class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        x =[]
        if len(discounts) < len(prices):
            for i in range(len(discounts)):
                y = (prices[i]*(100-discounts[i]))/100
                x.append(y)
        else:
            for i in range(len(prices)):
                y = (prices[i]*(100-discounts[i]))/100
                x.append(y)
        sumx = 0
        sumi =0 
        for i in range(len(x)):
            sumx += x[i]
        if len(x) < len(prices):
            for i in range(len(x),len(prices)):
                sumi += prices[i]
        return sumx + sumi
        ©leetcode
