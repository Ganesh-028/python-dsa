class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        for i in range(len(str(n))):
            temp = n%10
            digits.append(temp)
            n = n //10
        z = max(digits)
        digits.remove(z)
        y = max(digits)
        return z*y

        
